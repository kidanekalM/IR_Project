import streamlit as st

# Mock search function
def perform_search(query):
    psalms_notes = [
        {'doc_id': 1, 'text': 'Psalms 1: "Lorem ipsum dolor sit amet..."'},
        {'doc_id': 2, 'text': 'Psalms 2: "Consectetur adipiscing elit..."'},
        {'doc_id': 3, 'text': 'Psalms 3: "Sed do eiusmod tempor incididunt..."'},
        {'doc_id': 4, 'text': 'Psalms 4: "Ut labore et dolore magna aliqua..."'},
        {'doc_id': 5, 'text': 'Psalms 5: "Ut enim ad minim veniam...'},
        # Add more documents here
    ]
    # Return documents containing the query
    results = [note for note in psalms_notes if query.lower() in note['text'].lower()]
    # st.write(f"Found {len(results)} results")  # Debug line to check the number of results
    return results

# Set the title of the app
# st.header('ግእዝ')

# Search input
query = st.text_input('ግእዝን ፈልግ')

if query:
    # Perform search
    results = perform_search(query)

    # Display results
    st.write(f" ክመዝገብ '{query}':")
    for result in results:
        with st.expander(f"Document {result['doc_id']}"):
            st.write(result['text'])
 
