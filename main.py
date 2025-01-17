import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from inverted_index import inverted_index

from psalms_notes import psalms_notes
from tokenizer import tokenizer
from stopword import remove_stopwords
from stemmer import stem_list
from collections import defaultdict
from indexer import create_index_with_weights
from matching import matching
#corpus collection > Tokenization > stopowrd removal > stemmer > Weighted Index > Remove terms > Query > UI  
def preprocess():
    stemmed_tokens =[]
    # count = 0
    for psalm in psalms_notes:
        tokens = tokenizer(psalm['text'])
        stopword_removed_token = remove_stopwords(tokens)
        stemmed_token = stem_list(stopword_removed_token)

        stemmed_tokens.append({'doc_id':psalm['doc_id'],'tokens':stemmed_token})

    inverted_index = create_index_with_weights(stemmed_tokens)

    with open('inverted_index.py','w', encoding='utf-8') as file:
        file.write(f"inverted_index = {inverted_index}")
     
    return inverted_index

preprocess()

result = subprocess.run(['streamlit', 'run', 'ui.py'], capture_output=True, text=True)

print(result.stdout)

