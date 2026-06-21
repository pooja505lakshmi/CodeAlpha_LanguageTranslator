import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translator")
st.write("Translate text instantly into multiple languages")

text = st.text_area("Enter Text")

target = st.selectbox(
    "Translate To",
    ["tamil", "hindi", "french", "english","telugu","malayalam","kannada","german","spanish","japanese","korean","chinese","viatnamese"]
)

if st.button("Translate"):

    if text == "":
        st.warning("Please enter some text")
    else:
        translated = GoogleTranslator(
            source="auto",
            target=target
        ).translate(text)

        st.success(translated)
    
