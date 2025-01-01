
def tokenizer( string_document,sentence_sep="።",word_sep=" "):
    string_document = string_document.replace('0',"")
    string_document = string_document.replace('1',"")
    string_document = string_document.replace('2',"")
    string_document = string_document.replace('3',"")
    string_document = string_document.replace('4',"")
    string_document = string_document.replace('5',"")
    string_document = string_document.replace('6',"")
    string_document = string_document.replace('7',"")
    string_document = string_document.replace('8',"")
    string_document = string_document.replace('9',"")
    string_document = string_document.replace('-',"")
    sentences = string_document.split(sentence_sep)
    words = []
    for sentence in sentences:
        words += sentence.split(word_sep)

    return words





print(tokenizer("ዘጻድቃን ዘኃጥኣን 1234567765800መዝሙር። ዘዳዊት ብፁዕ ብእሲ4567890 ምክረ ረሲዓን ፍኖተ9876543 ኃጥኣን። መንበረ መስተሳልቃን ሕገ እግዚአብሔር ሥምረቱ መዕልተ ሌሊተ። ዕፅ ሙሓዘ ማይ ፍሬሃ በጊዜሃ መሬት ነፍስ ምድር ምክረ ጻድቃን ፍኖቶሙ ኃጥኣን"))




