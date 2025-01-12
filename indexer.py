import re
from collections import defaultdict
from psalms_notes import psalms_notes
from tokenizer import tokenizer
import math
from collections import defaultdict
def create_index_with_weights(stemmed_tokens):
    
    inverted_index = {}
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
            # if (inverted_index[token]):
            try:
                inverted_index[token].append((doc_id,freq))
            except:
                inverted_index.setdefault(token,[(doc_id,freq)])
            

            doc_freq[token] += 1
            doc_length[doc_id] += freq

    for token, postings in inverted_index.items():
        idf = math.log(num_docs / (1 + doc_freq[token]))
        for i, (doc_id, freq) in enumerate(postings):
            tf = freq / doc_length[doc_id]
            postings[i] = (doc_id, tf * idf)
    return inverted_index

