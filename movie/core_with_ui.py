import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.write("Enter a movie description and let Gemini extract the important details.")

# -----------------------------
# Prompt Template
# -----------------------------
template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert movie information extraction assistant. "
        "Extract only the information explicitly mentioned in the description. "
        "If any field is missing, write 'Not Mentioned'."
    ),
    (
        "human",
        """
Extract the following information:

- Movie Name
- Genre
- Director
- Cast
- Rating
- Runtime
- Language
- Short Summary

Movie Description:
{movie_description}
"""
    )
])

# -----------------------------
# User Input
# -----------------------------
description = st.text_area(
    "Movie Description",
    height=220,
    placeholder="Paste a movie description here..."
)

# -----------------------------
# Button
# -----------------------------
if st.button("Extract Information"):

    if not description.strip():
        st.warning("Please enter a movie description.")
        st.stop()

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite"
    )

    prompt = template.invoke({
        "movie_description": description
    })

    with st.spinner("Analyzing movie..."):

        response = llm.invoke(prompt)

    st.success("Extraction Complete!")

    st.markdown("## 📄 Extracted Information")

    st.markdown(response.text)