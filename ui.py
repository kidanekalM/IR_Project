import streamlit as st
from matching import matching
from stemmer import stem_list
from tokenizer import tokenizer
from psalms_notes import psalms_notes
from stopword import remove_stopwords
from inverted_index import inverted_index
from evaluation import precision, recall,f1
# Assuming these functions are defined elsewhere in your code
def preprocess_query(query):
    return stem_list(remove_stopwords(tokenizer(query)))

def perform_search(query):
    results = matching(preprocess_query(query), inverted_index)
    return results

query = st.text_input('በግእዝ ፈልግ',key="query_input")

# Initialize a counter for relevant documents
total_rel_input = st.sidebar.empty()
relevant_counter = st.sidebar.empty()  # Placeholder for the counter display
precision_disp = st.sidebar.empty()  # Placeholder for the counter display
recall_disp = st.sidebar.empty()  # Placeholder for the counter display
f1_disp = st.sidebar.empty()  # Placeholder for the counter display
relevant_count = 0
topRelevant = 10
if query:
    results = perform_search(query)
    results = results[:topRelevant]
    retrieved_count = len(results)
    st.write(f"ከመዝገብ '{query}':")
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
            total_relevant =  int(total_rel_input.text_input("Total Relevant",value=150,key=f'total_rel_input{doc_id}'))
            precision_disp.text(f"Precision: {(precision(relevant_count,retrieved_count))*100}%")
            recall_disp.text(f"Recall  : {(recall(relevant_count,total_relevant))*100}%")
            f1_disp.text(f"f1 - measure : {(f1(relevant_count,retrieved_count,total_relevant))}")

            # Update styling based on relevance
            expander_style = "border: 3px solid lightgreen; border-radius:5px; padding:.5rem;" if relevant else "border-radius:5px; padding:.5rem; border: 1px solid black;"

            # Streamlit doesn't directly support custom CSS at the component level,
            # use Markdown for the container style
            with st.expander(f" {note['text'][:20]}...  (Similarity: {similarity:.4f})",
                             expanded=False):
                st.markdown(f"<div style='{expander_style}'>{note['text']}</div>", unsafe_allow_html=True)
