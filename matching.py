import math
from collections import defaultdict
import numpy as np

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
    return dot_product / (norm_v1 * norm_v2)

def match_query_with_tfidf(query, inverted_index):
    # Tokenize the query
    query_tokens = query.split()
    
    # Initialize query vector
    query_vector = np.zeros(len(inverted_index))
    
    # Find all relevant documents and calculate their scores
    doc_scores = defaultdict(float)
    token_index = {token: idx for idx, token in enumerate(inverted_index.keys())}
    
    for token in query_tokens:
        if token in inverted_index:
            for doc_id, tfidf in inverted_index[token]:
                doc_scores[doc_id] += tfidf
            query_vector[token_index[token]] = 1
    
    # Calculate cosine similarity for each document
    similarities = []
    for doc_id, score in doc_scores.items():
        doc_vector = np.array([tfidf for token, postings in inverted_index.items() for doc, tfidf in postings if doc == doc_id])
        similarity = cosine_similarity(query_vector, doc_vector)
        similarities.append((doc_id, similarity))
    
    # Sort by similarity in descending order
    sorted_docs = sorted(similarities, key=lambda x: x[1], reverse=True)
    
    return sorted_docs

# Example usage
inverted_index = defaultdict(
    list, 
    {'token1': [(1, 0.1), (2, 0.2)], 'token2': [(1, 0.3), (3, 0.4)]}
)
query = "token1 token2"

results = match_query_with_tfidf(query, inverted_index)
for doc_id, similarity in results:
    print(f"Document {doc_id}: Similarity {similarity}")
