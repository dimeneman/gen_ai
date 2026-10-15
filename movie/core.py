import os
from google import genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# for better visualization in terminal
from rich.console import Console
from rich.panel import Panel

console = Console()
load_dotenv()


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



description = input("Give the movie description: ")
final_prompt = template.invoke({"movie_description": description})


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

response = llm.invoke(final_prompt)

print()

console.print(
    Panel(
        response.text,
        title="🎬 Movie Information",
        border_style="green"
    )
)