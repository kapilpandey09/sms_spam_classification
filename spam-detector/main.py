import streamlit as st
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

# Download required resources once
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

st.markdown("""
    <style>
            
    div.stButton > button:first-child {
            
        background-color: black;
        color: white/50;
        border: 1px solid white;
        padding: 0.5em 2em;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        transition: 0.3s;
}
    .stApp {
        background-color: black;
        color: white;
    }

    .css-1cpxqw2 edgvbvh3 {  /* headings */
        color: white;
    }

    input {
        background-color: #333;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)


def transform_text(text):
    import string
    import re

    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for word in text:
        if word.isalnum() and word not in stopwords.words('english') and word not in string.punctuation:
            y.append(ps.stem(word))
    return " ".join(y)

# Streamlit UI
st.title("Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    transformed = transform_text(input_sms)
    vector_input = cv.transform([transformed])
    result = model.predict(vector_input)[0]
    if result == 1:
        st.error("This is a SPAM message!")
    else:
        st.success("This is NOT a spam message.")
