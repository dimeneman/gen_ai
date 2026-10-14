import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

messages = [
    SystemMessage(content="You're a funny AI assistant.")
]

while True:

    user = input("You: ")

    if user == "0":
        break

    messages.append(HumanMessage(content=user))
    response = llm.invoke(messages)

    # Display to the user
    print("Gemini:", response.text)

    # Store the complete message
    messages.append(response)