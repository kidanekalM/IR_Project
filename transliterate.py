from romanization_values import romanization2 as romanization

def transliterate(word):
    transliterated_text = ''
    for char in word:
        if char in romanization:
            transliterated_text += romanization[char]
        else:
            transliterated_text += char
    return transliterated_text
romanization_reversed = {v: k for k, v in romanization.items()}

def reverse_transliterate(word):
    transliterated_text = ''
    i = 0
    while i < len(word):
        match_found = False
        for length in range(2, 0, -1):  # Check substrings of length 2 and 1
            if word[i:i+length] in romanization_reversed:
                transliterated_text += romanization_reversed[word[i:i+length]]
                i += length
                match_found = True
                break
        if not match_found:
            transliterated_text += word[i]
            i += 1
    return transliterated_text

################################################
