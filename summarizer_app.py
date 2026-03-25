from transformers import pipeline
import streamlit as st

# Load summarization model
summarizer = pipeline("summarization")

# App title
st.title("AI Text Summarizer")

st.write("Enter text below and get instant summary:")

# Text input box
input_text = st.text_area("Enter your text here", height=200)

# Button
if st.button("Summarize"):
    if input_text.strip() != "":
        summary = summarizer(input_text, max_length=150, min_length=40, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text!")
