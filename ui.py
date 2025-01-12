import streamlit as st
from inverted_index import inverted_index
from psalms_notes import psalms_notes
from matching import matching

def perform_search(query):
    # Use the matching function to get results based on the query and inverted index
    results = matching(query, inverted_index)
    return results

query = st.text_input('ግእዝን ፈልግ')

if query:
    results = perform_search(query)

    st.write(f" ክመዝገብ '{query}':")
    for doc_id, similarity in results:
        # Find the corresponding note for the document ID
        note = next((note for note in psalms_notes if note['doc_id'] == doc_id), None)
        if note:
            with st.expander(f"Document {doc_id} (Similarity: {similarity:.4f})"):
                st.write(note['text'])