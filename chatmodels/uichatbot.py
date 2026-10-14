import os
from dotenv import load_dotenv
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

st.title("Gemini Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You're a funny AI assistant.")
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user = st.chat_input("Type your message...")

if user:

    st.session_state.messages.append(
        HumanMessage(content=user)
    )

    response = llm.invoke(st.session_state.messages)

    st.session_state.messages.append(response)

    st.session_state.chat_history.append(("You", user))
    st.session_state.chat_history.append(("Gemini", response.text))

for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.write(message)