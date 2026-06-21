import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

st.title("🌍 AI Language Translator")

st.write("Translate text instantly into multiple languages.")

text = st.text_area("Enter Text")

target = st.selectbox(
    "Translate To",
    [
        "english",
        "tamil",
        "hindi",
        "telugu",
        "malayalam",
        "kannada",
        "french",
        "german",
        "spanish",
        "japanese",
        "korean",
        "chinese"
    ]
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

        st.subheader("📋 Copy Translation")
        st.text_area(
            "Translated Text",
            translated,
            height=100
        )

        st.subheader("🔊 Listen to Translation")

        tts = gTTS(text=translated, lang="en")

        tts.save("translation.mp3")

        audio_file = open("translation.mp3", "rb")

        st.audio(audio_file.read(), format="audio/mp3")