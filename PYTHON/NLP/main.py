import streamlit as st
import pandas as pd
import nltk

# Use Streamlit's page navigation with radio buttons
# page = st.sidebar.radio("Select Projects", ["ASCII Value Checker", "ABC"])

tab1, tab2, tab3, tab4,tab5 = st.tabs(["Check word ASCII", "Word Tokenizer", "Sentence Tokenizer","what computer see","Capitalize"])

with tab1:
    st.title("Check ASCII value")
    value = str(st.text_input("Enter any value"))
    button = st.button("Check ASCII value")
    if button and value:
        f = f"Ascii value of {value} is {ord(value)}"
        st.text(f)

    st.divider()

    with st.expander("Know More"):
        # Create a DataFrame of ASCII characters and their values
        ascii_data = {'Character': [chr(i) for i in range(33, 127)],
                      'ASCII Value': [i for i in range(33, 127)]}
        df = pd.DataFrame(ascii_data)

        # Display the DataFrame in Streamlit
        st.dataframe(df)

with tab2:
    st.title("NLTK word tokenizer")
     
    data=st.chat_input("Enter the long text to tokenize into the words")
    if data:
        list_token=nltk.word_tokenize(data)
        st.text(list_token)
with tab3:
    st.title("Sentence tokenizer")
    data2=st.chat_input("Enter the paragraph...")
    if data2:
        st.text(nltk.sent_tokenize(data2))

with tab4:
    st.title("Convert sentences into ASCII")
    data3=st.text_input("Enter sentences")
    li=[{char: ord(char)} for char in data3]
    button_sen=st.button("Check ASCII")
    if button_sen:
        st.text(li)
with tab5:
    st.title("Capitalize your sentence")
    uncap_text=str(st.text_input("Enter your sentence..."))
    if uncap_text:
        final_capitalized_text=uncap_text[0].upper()+uncap_text[1:].lower()
    button_cap=st.button("Capitalize")
    if button_cap:
        st.text(final_capitalized_text)