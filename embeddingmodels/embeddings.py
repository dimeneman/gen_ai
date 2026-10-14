import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

"""An embedding model converts text into a list of numbers (a vector) that captures its meaning."""
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

vector = embeddings.embed_query("How good is Breaking Bad?")

print(len(vector))
print(vector[:10])  # First 10 dimensions