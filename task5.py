import streamlit as st
# import os
from transformers import pipeline

# Pick model
summarizer = pipeline("summarization",model= "t5-base",tokenizer="t5-base",framework="pt")

st.title("Text Summarizer")

file = st.file_uploader("Upload your txt file here",[".txt"],accept_multiple_files=False)

if file:
    # with open(file, "rb+") as f:
    txt = file.read()
    st.text_area("Text Before Summary",txt)

    # summarizer = pipeline(
    # "summarization", 
    # model=model_name, 
    # tokenizer=pegasus_tokenizer, 
    # framework="pt"
    # )
 
    summary = summarizer(txt, min_length=100, max_length=500,do_sample = False)
    
    st.text_area("Summarized Text",summary[0]["summary_text"])