import re
from collections import defaultdict

def create_index(docs):
    inverted_index = {}
    for doc_id, text in enumerate(docs):
        tokens = preprocess_text(text)
        for token in tokens:
            if token not in inverted_index:
                inverted_index[token] = []
            inverted_index[token].append(doc_id)
    return inverted_index

# Create the index
index = create_index(docs)
print(dict(index))
