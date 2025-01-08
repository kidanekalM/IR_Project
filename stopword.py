from psalms_notes import psalms_notes
from psalms_notes import psalms_notes
from tokenizer import tokenizer

stopwords=[
    "ውስተ",
    "እግዚአብሔር",
    "እስመ",
    "ከመ",
    '',
    'Psalms'
]

def remove_stopwords(tokens):
    # return ' '.join([word for word in text.split() if word not in stopwords])
    for stopword in stopwords:
        while stopword in tokens:
            tokens.remove(stopword) 
    return tokens

# print (remove_stopwords(psalms_notes[0]['text']))
# print(psalms_notes[0]['text'])
tokens  = tokenizer(psalms_notes[0]['text'])
print(tokens)
print(remove_stopwords(tokens))