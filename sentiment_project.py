import streamlit as st
from textblob import TextBlob
st.sidebar.title("about us")
st.sidebar.text("""we are students at Ducat &
learning machine learning.
""")

st.sidebar.title("contact us")
st.sidebar.text("""Sonu @ 11111
Monu @ 22222
Chintu @ 3333
""")

st.title("Sentiment Analysis Project")

text=st.text_input("**enter text**")
btn=st.button("predict")

if btn:
    blob=TextBlob(text)
    sen=blob.sentiment[0]
    if sen<0:
        st.error("Negative Sentiment")
        st.image("neg_senti.jpg")
    elif sen>0:
        st.success("Positive Sentiment")
        st.image("pos_senti.jpg")
    else:
        st.warning("Neutral Sentiment")
        st.image("neutral_senti.jpg")



