import numpy as np
from collections import defaultdict

def cosine_similarity(v1, v2):
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    if norm_v1 == 0 or norm_v2 == 0:  # Corrected condition to avoid division by zero
        return 0.0
    
    dot_product = np.dot(v1, v2)
    return dot_product / (norm_v1 * norm_v2)

def matching(query_tokens, inverted_index):
    query_vector = np.zeros(len(inverted_index))
    doc_scores = defaultdict(float)
    
    # Create a token index to map tokens to their indices
    token_index = {token: idx for idx, token in enumerate(inverted_index.keys())}

    # Build the query vector
    for token in query_tokens:
        if token in inverted_index:
            for doc_id, tfidf in inverted_index[token]:
                doc_scores[doc_id] += tfidf
            query_vector[token_index[token]] = 1  # Represents presence of the token in the query

    similarities = []
    
    # Calculate cosine similarity for each document
    for doc_id, score in doc_scores.items():
        doc_vector = np.zeros(len(inverted_index))  # Initialize doc_vector with zeros
        
        # Build the document vector based on tf-idf values
        for token, postings in inverted_index.items():
            for doc, tfidf in postings:
                if doc == doc_id:
                    doc_vector[token_index[token]] = tfidf  # Assign tf-idf to the respective index
        
        similarity = cosine_similarity(query_vector, doc_vector)
        similarities.append((doc_id, similarity))

    sorted_docs = sorted(similarities, key=lambda x: x[1], reverse=True)
    return sorted_docs