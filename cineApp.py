import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# Load environment variables
load_dotenv()

# Initialize model
model = ChatMistralAI(
    model="mistral-small-2506"
)

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
        """
You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful structured information from a movie paragraph.

Rules:
- Do NOT add explanations
- Do NOT add extra commentary
- Follow the exact format
- If information is missing → write NULL
- Keep summary short (2–3 lines max)
- Do NOT guess unknown facts

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Main Cast:
Music Composer:
Setting/Location:
Plot:
Themes:
Key Concepts:
Ratings:
Notable Features:

Short Summary:
"""
        ),
        ("human",
        """
Extract information from this paragraph:

{paragraph}
"""
        )
    ]
)

# ----------- UI -------------

st.set_page_config(page_title="Movie Info Extractor", layout="centered")

st.title("🎬 Movie Information Extractor")
st.markdown("Enter a movie paragraph and extract structured information.")

# Input box
para = st.text_area("Enter Movie Paragraph:", height=200)

# Button
if st.button("Extract Information"):
    if para.strip() == "":
        st.warning("Please enter a paragraph.")
    else:
        with st.spinner("Processing..."):
            final_prompt = prompt.invoke({"paragraph": para})
            response = model.invoke(final_prompt)

        st.subheader("📊 Extracted Information")
        st.text(response.content)