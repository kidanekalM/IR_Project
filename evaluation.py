
def precision(relevant_docs, retrieved_docs):
    if retrieved_docs == 0:
        return 0
    return relevant_docs / retrieved_docs
def recall(relevant_docs, retrieved_docs):
    return  0