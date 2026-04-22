from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

from langchain_mistralai import ChatMistralAI


model = ChatMistralAI(
    model="mistral-small-2506")

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

para= input("Give me a movie paragraph: ")

final_prompt = prompt.invoke(
    {"paragraph": para}
)

response = model.invoke(final_prompt)

print(response.content)