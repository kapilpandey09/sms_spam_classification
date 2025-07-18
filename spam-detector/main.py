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
    text = text.lower()
    text = word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stop_words and i not in string.punctuation:
            y.append(i)
    
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
            
    return " ".join(y)


# import model 
# Inject custom CSS for text input


tfidf = pickle.load(open('./spam-detector/vectorizer.pkl', 'rb'))
model = pickle.load(open('./spam-detector/model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")


st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: black;
        color: white;
        border: 1px solid white;
        padding: 0.5em 2em;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        transition: 0.3s;
    }

    div.stButton > button:first-child:hover {
        background-color: #333;
        color: yellow;
        border-color: yellow;
    }
    </style>
""", unsafe_allow_html=True)

input_sms = st.text_input("Enter your message:")



if st.button('🚀 Predict'):
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]

    if result == 1:
        st.markdown('<h2 style="color:red;">🚫 Spam</h2>', unsafe_allow_html=True)
    else:
        st.markdown('<h2 style="color:lightgreen;">✅ Not Spam</h2>', unsafe_allow_html=True)
