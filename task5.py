import streamlit as st
# import os
from transformers import pipeline
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
 
# Pick model
model_name = "google/pegasus-xsum"

# Load pretrained tokenizer
pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)
pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

st.title("Text Summarizer")

file = st.file_uploader("Upload your txt file here",[".txt"],accept_multiple_files=False)

if file:
    # with open(file, "rb+") as f:
    txt = file.read()
    st.text_area("Text Before Summary",txt)

    summarizer = pipeline(
    "summarization", 
    model=model_name, 
    tokenizer=pegasus_tokenizer, 
    framework="pt"
    )
 
    summary = summarizer(txt, min_length=100, max_length=500)
    
    st.text_area("Summarized Text",summary[0]["summary_text"])