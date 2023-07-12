import streamlit as st
import openai
from PyPDF2 import PdfFileReader
import os

def extract_text_from_pdf(pdf_path):
    pdf = PdfFileReader(pdf_path)
    number_of_pages = pdf.getNumPages()
    texts = []
    for page_number in range(number_of_pages):
        page = pdf.getPage(page_number)
        text = page.extractText()
        texts.append(text)
    return texts

def split_text(text, length):
    words = text.split(' ')
    return [' '.join(words[i:i+length]) for i in range(0, len(words), length)]

def summarize_text(openai_api_key, text):
    openai.api_key = openai_api_key

    split_texts = split_text(text, 3500)
    summaries = []

    for text in split_texts:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Read and summarize each chapter with the most unique and helpful points, into a numbered list of key points and takeaways. The text is: {text}",
            max_tokens=500
        )
        summaries.append(response['choices'][0]['text'])

    return summaries

st.title("Book Summarizer")

# Input for OpenAI API key
openai_api_key = st.text_input("Enter OpenAI API key", type="password")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None and openai_api_key:
    with st.spinner('Extracting text...'):
        extracted_text = extract_text_from_pdf(uploaded_file)

    with st.spinner('Summarizing...'):
        summarized_texts = summarize_text(openai_api_key, extracted_text)

    for i, summary in enumerate(summarized_texts):
        st.write(f"Summary {i+1}:")
        st.write(summary)

