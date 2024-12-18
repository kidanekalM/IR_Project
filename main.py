from stemmer import stem
while True:
    word = input("Enter a word to be stemmed: ")
    print(stem(word))
    print(len(stem(word)))
