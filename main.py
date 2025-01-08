import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from psalms_notes import psalms_notes
from tokenizer import tokenizer
from stopword import remove_stopwords
from stemmer import stem_list

#corpus collection > Tokenization > stopowrd removal > stemmer > Weighted Index > Remove terms > Query > UI  

stemmed_token=[]
for psalm in psalms_notes:
    # print(psalm['text'])
    tokens = tokenizer(psalm['text'])
    stopword_removed_token = remove_stopwords(tokens)
    stemmed_token = stem_list(stopword_removed_token)
    break
    # print(tokens)
    # print(stopword_removed_token)
print("stemmed", stemmed_token)