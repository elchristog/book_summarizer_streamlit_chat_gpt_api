import streamlit as st
import openai
from PyPDF2 import PdfReader
import os

def extract_text_from_pdf(pdf_path):
    pdf = PdfReader(pdf_path)
    number_of_pages = len(pdf.pages)
    texts = []
    for page_number in range(number_of_pages):
        page = pdf.pages[page_number]
        text = page.extract_text()
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
st.write("Remember to copy and paste the summary in your word file to read it calmly")
# Input for OpenAI API key
openai_api_key = st.text_input("Enter OpenAI API key", type="password")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None and openai_api_key:
    with st.spinner('Extracting text...'):
        extracted_texts = extract_text_from_pdf(uploaded_file)

    with st.spinner('Summarizing...'):
        all_summaries = ""
        for i, extracted_text in enumerate(extracted_texts):
            summaries = summarize_text(openai_api_key, extracted_text)

            start_page = i + 1
            end_page = i + len(summaries)

            for j, summary in enumerate(summaries):
                summary_title = f"Summary {i+1}-{j+1}"
                st.title(summary_title)
                st.write(summary)
                st.write(f"Pages used: {start_page} to {end_page}")
                all_summaries += f"{summary_title}\n\n{summary}\n\n"

        # Download button
        if all_summaries:
            with open("summaries.txt", "w", encoding="utf-8") as file:
                file.write(all_summaries)
            st.download_button(
                label="Download Summaries",
                data=all_summaries,
                file_name="summaries.txt",
                mime="text/plain"
            )
