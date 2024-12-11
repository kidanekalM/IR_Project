from transliterate import transliterate, reverse_transliterate
from nouns import nouns
from affixes import prefix, suffix, infix

def stem(word):
    word = transliterate(word)

    for pre in prefix:
        if word.startswith(pre):
            word = word[len(pre):]
            break
    
    for suf in suffix:
        if word.endswith(suf):
            word = word[:-len(suf)]
            break
    
    for inf in infix:
        if inf in word:
            word = word.replace(inf, "")
            break
    
    word = reverse_transliterate(word)
    
    return word

stemmed_nouns = [stem(noun) for noun in (nouns[0]).split(" ")]

print(stemmed_nouns)