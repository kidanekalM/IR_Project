from transliterate import transliterate, reverse_transliterate
from affixes import prefix, suffix, infix
from exceptions import exceptions

def stem_list(list_of_words):
    stemmed_list = []
    for word in list_of_words:
        stemword,rootword = stem(word)
        stemmed_list.append(stemword)
    return stemmed_list
def stem(word):
    word = transliterate(word)
    # print(word)
    
    for suf in suffix:
        if word.endswith(suf):
            word = word[:-len(suf)]
            # print("suf",word)
            
    for pre in prefix:
        if word.startswith(pre):
            word = word[len(pre):]
            # print("pre",word)
            
    if word in exceptions.keys():
        word = exceptions[word]
    root = word
    for inf in infix:
        # if inf in word:
        root = root.replace(inf, "")
        # print(word,)
    
    stemWord = reverse_transliterate(word)
    rootWord = reverse_transliterate(root)
    
    return stemWord,rootWord

def measure_accuracy(stemmer, nouns, correct_stems): 
    predicted_stems = [transliterate(stemmer(noun)) for noun in nouns] 
    transliterated_correct_stems = [transliterate(stem) for stem in correct_stems] 
    for predicted, correct in zip(predicted_stems, transliterated_correct_stems):
        print(predicted, correct)
    correct_count = sum([1 for predicted, correct in zip(predicted_stems, transliterated_correct_stems) if predicted == correct])
    accuracy = correct_count / len(nouns)
    return accuracy

# stemmed_nouns = [stem(noun) for noun in (nouns[0]).split(" ")]
# stemmed_true = [ "ጻድቅ", "ኃጥእ", "መዝሙር", "ዳዊት", "ብፁዕ", "ብእስ", "ምክር", "ረሲዓ", "ፍኖት", "ኃጥእ", "መንበር", "መስተሳልቅ", "ሕግ", "እግዚአብሔር", "ሥምር", "መዕልት", "ሌሊት", "ዕፅ", "ሙሓዝ", "ማይ", "ፍሬ", "ጊዜ", "መሬት", "ነፍስ", "ምድር", "ምክር", "ጻድቅ", "ፍኖት", "ኃጥእ"]

# print(measure_accuracy(stem, nouns[0].split(" "), stemmed_true))
# print(stemmed_nouns)




# while True:
    # word = input("Enter a word to be stemmed: ")
    # print(stem(word))
    # print(len(stem(word)))



