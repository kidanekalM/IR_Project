
import re
def tokenizer( string_document,sentence_sep="።",word_sep=" "):

    string_document = re.sub(r'[0-9\-]', '', string_document)

    sentences = string_document.split(sentence_sep)
    words = []
    for sentence in sentences:
        words += sentence.split(word_sep)

    return words





print(tokenizer("ዘጻድቃን ዘኃጥኣን 1234567765800መዝሙር። ዘዳዊት ብፁዕ ብእሲ4567890 ምክረ ረሲዓን ፍኖተ9876543 ኃጥኣን። መንበረ መስተሳልቃን ሕገ እግዚአብሔር ሥምረቱ መዕልተ ሌሊተ። ዕፅ ሙሓዘ ማይ ፍሬሃ በጊዜሃ መሬት ነፍስ ምድር ምክረ ጻድቃን ፍኖቶሙ ኃጥኣን"))




