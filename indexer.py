import re
from collections import defaultdict
from psalms_notes import psalms_notes
from tokenizer import tokenizer
import math
from collections import defaultdict
def create_index(docs):
    inverted_index = {}
    for doc_id, doc in enumerate(docs):
        tokens = tokenizer(doc['text'])
        # print(type(text))
        for token in tokens:
            if token not in inverted_index:
                inverted_index[token] = []
            inverted_index[token].append(doc_id)
    return inverted_index

# Create the index  
index = create_index(psalms_notes)
# print(dict(index))


##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def create_index_with_weights(stemmed_tokens):
    
    inverted_index = defaultdict(list)
    doc_freq = defaultdict(int)
    doc_length = defaultdict(int)
    num_docs = len(stemmed_tokens)
    for item in  stemmed_tokens:
        doc_id = item['doc_id']
        tokens = item['tokens']
        term_freq = defaultdict(int)
        for token in tokens:
            term_freq[token] += 1
        
        for token, freq in term_freq.items():
            inverted_index[token].append((doc_id, freq))
            doc_freq[token] += 1
            doc_length[doc_id] += freq

    for token, postings in inverted_index.items():
        idf = math.log(num_docs / (1 + doc_freq[token]))
        for i, (doc_id, freq) in enumerate(postings):
            tf = freq / doc_length[doc_id]
            postings[i] = (doc_id, tf * idf)

    return inverted_index


# Dummy tokenizer function for demonstration purposes
# def tokenizer(text):
    # return text.lower().split()

# index = create_index_with_weights(psalms_notes)
# for word, postings in index.items():
    # print(f"{word}: {postings}\n")
def create_index(stemmed_tokens):
    inverted_index='.git'
    doc_freq = defaultdict(int)
    term_freq = defaultdict(int)
    inverted_index = defaultdict(list)
    for doc_id, stemmed_token in stemmed_tokens:
        
        for token in stemmed_token:
            term_freq[token] += 1
            doc_freq[token] = stemmed_tokens
            inverted_index[token].append(doc_id)
