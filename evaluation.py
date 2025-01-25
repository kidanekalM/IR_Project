
def precision(relevant_docs, retrieved_docs):
    if retrieved_docs == 0:
        return 0
    return relevant_docs / retrieved_docs
def recall(relevant_docs, total_rel):
    if total_rel == 0:
        return 0
    return relevant_docs/total_rel
def f1(relevant_docs,retrieved_docs,total_rel):
    p = precision(relevant_docs,retrieved_docs)
    r =  recall(relevant_docs,total_rel)
    if (p+r) == 0:
        return 0
    return (2*p*r)/(p+r)