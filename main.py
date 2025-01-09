import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from psalms_notes import psalms_notes
from tokenizer import tokenizer
from stopword import remove_stopwords
from stemmer import stem_list
from collections import defaultdict
from indexer import create_index_with_weights
#corpus collection > Tokenization > stopowrd removal > stemmer > Weighted Index > Remove terms > Query > UI  

stemmed_tokens =[]
count = 0
for psalm in psalms_notes:
    # print(psalm['text'])
    tokens = tokenizer(psalm['text'])
    stopword_removed_token = remove_stopwords(tokens)
    stemmed_token = stem_list(stopword_removed_token)
    stemmed_tokens.append({'doc_id':psalm['doc_id'],'tokens':stemmed_token})
    # stemmed_tokens['doc_id'] = psalm['doc_id']

    # stemmed_tokens[stemmed_tokens['doc_id']['tokens']] = stemmed_token
    if count > 5:
        break
    count += 1 
print(stemmed_tokens)
print("Weighted ",create_index_with_weights(stemmed_tokens))
    # print(tokens)
    # print(stopword_removed_token)
# print("prodess " , stemmed_tokens)