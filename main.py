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
# count = 0
for psalm in psalms_notes:
    tokens = tokenizer(psalm['text'])
    stopword_removed_token = remove_stopwords(tokens)
    stemmed_token = stem_list(stopword_removed_token)

    stemmed_tokens.append({'doc_id':psalm['doc_id'],'tokens':stemmed_token})

inverted_index = create_index_with_weights(stemmed_tokens)

# with open('inverted_index.py','w', encoding='utf-8') as file:
    # file.write(f"inverted_index = {inverted_index}")
     
    # if count > 1:  break; count += 1 

from inverted_index import inverted_index
print(inverted_index['ወሬዛ'])

