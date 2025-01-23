import streamlit as st
from inverted_index import inverted_index
from psalms_notes import psalms_notes
from matching import matching
from tokenizer import tokenizer
from stemmer import stem_list
from stopword import remove_stopwords
from evaluation import precision, recall

# Assuming these functions are defined elsewhere in your code
def preprocess_query(query):
    return stem_list(remove_stopwords(tokenizer(query)))

def perform_search(query):
    results = matching(preprocess_query(query), inverted_index)
    return results

query = st.text_input('ግእዝ')

# Initialize a counter for relevant documents
relevant_counter = st.sidebar.empty()  # Placeholder for the counter display
precision_disp = st.sidebar.empty()  # Placeholder for the counter display
recall_disp = st.sidebar.empty()  # Placeholder for the counter display
relevant_count = 0

if query:
    results = perform_search(query)
    retrieved_count = len(results)
    st.write(f"ክመዝገብ '{query}':")
    for doc_id, similarity in results:
        note = next((note for note in psalms_notes if note['doc_id'] == doc_id), None)
        if note:
            # Calculate key for relevant checkboxes and create corresponding state variable
            key_checkbox = f'relevant_{doc_id}_checkbox'
            relevant = st.checkbox(f'Relevant', key=key_checkbox)

            # If a document is marked as relevant, increment the relevant count
            if relevant:
                relevant_count += 1

            # Display the counter
            relevant_counter.text(f"Relevant Documents: {relevant_count}")
            precision_disp.text(f"Precision: {(precision(relevant_count,retrieved_count))*100}%")
            recall_disp.text(f"Recall Not yet calculated : {(precision(relevant_count,retrieved_count))*100}%")

            # Update styling based on relevance
            expander_style = "border: 3px solid green;" if relevant else "border: 1px solid black;"

            # Streamlit doesn't directly support custom CSS at the component level,
            # use Markdown for the container style
            with st.expander(f"Document {doc_id} (Similarity: {similarity:.4f})",
                             expanded=True):
                st.markdown(f"<div style='{expander_style}'>{note['text']}</div>", unsafe_allow_html=True)
