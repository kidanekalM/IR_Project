from psalms_notes import psalms_notes

stopwords=[
    "ውስተ",
    "እግዚአብሔር",
    "እስመ",
    "ከመ",
    '',
    'Psalms'
]

def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word not in stopwords])

print (remove_stopwords(psalms_notes[0]['text']))
print(psalms_notes[0]['text'])