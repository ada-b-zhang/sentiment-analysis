import streamlit as st
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

st.title("💜 Sentiment Analysis App 💜")
st.subheader("Enter text below to find out if it's Positive or Negative!")

st.markdown("### 🖊️ Type whatever you want:")
user_input = st.text_area("", placeholder="Enter your text here...")

if st.button("💡 Analyze Sentiment"):
    if user_input.strip():
        result = sentiment_analyzer(user_input)[0]
        label = result['label']
        score = result['score']

        if label == "POSITIVE":
            st.success(f"😃 The sentiment is **Positive** with a confidence of {score:.2f}.")
        else:
            st.error(f"😭 The sentiment is **Negative** with a confidence of {score:.2f}.")
    else:
        st.warning("⚠️ Please enter some text to analyze.")
