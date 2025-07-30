import streamlit as st
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer,PorterStemmer
# from nltk.corpus import wordnet

# Use Streamlit's page navigation with radio buttons
# page = st.sidebar.radio("Select Projects", ["ASCII Value Checker", "ABC"])

tab1, tab2, tab3, tab4,tab5,tab6 = st.tabs(["Text to ASCII", "Word Tokenizer", "Sentence Tokenizer","what computer see","Capitalize","Lemmatization/Stemming"])

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
with tab6:
    st.title("Stemming")
    st.info("Stemming is a text normalization technique in NLP where words are reduced to their root form by removing suffixes and prefixes, often resulting in non-dictionary words.")
    nltk.download("omw-1.4")
    nltk.download("wordnet")
    
    with st.form("Stemming Form"):
        data_stem = st.text_input("Enter the word")
        submitted_stem = st.form_submit_button("Convert")
    if submitted_stem and data_stem:
        stem=PorterStemmer()
        st.success("Stemmed Sentence:")
        st.write(stem.stem(data_stem))



    st.markdown("<br>", unsafe_allow_html=True)
    st.title("Lemmatization")
    st.info("Lemmatization is a text normalization technique in NLP where a word is reduced to its base or dictionary form, known as the lemma.")
    
    with st.form("lemmatization_form"):
        data_lemma = st.text_input("Enter the word")
        submitted = st.form_submit_button("Convert")
    if submitted and data_lemma:
        lem=WordNetLemmatizer()
        st.success("Lemmatized Sentence:")
        st.write(lem.lemmatize(data_lemma))
# with tab7:
#     st.title("Synonyms and Antonyms Finder")
#     import nltk
#     from nltk.corpus import wordnet
#     nltk.download('wordnet')

#     word = st.text_input("Enter a word to find synonyms and antonyms")
#     if word:
#         synonyms = set()
#         antonyms = set()
#         for syn in wordnet.synsets(word):
#             for lemma in syn.lemmas():
#                 synonyms.add(lemma.name())
#                 if lemma.antonyms():
#                     for ant in lemma.antonyms():
#                         antonyms.add(ant.name())
#         st.write("Synonyms:", ", ".join(sorted(synonyms)) if synonyms else "None found")
#         st.write("Antonyms:", ", ".join(sorted(antonyms)) if antonyms else "None found")
