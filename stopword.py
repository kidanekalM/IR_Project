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
    for stopword in stopwords:
        while stopword in tokens:
            tokens.remove(stopword) 
    return tokens

# tokens  = tokenizer(psalms_notes[0]['text'])
# print(tokens)
# print(remove_stopwords(tokens))