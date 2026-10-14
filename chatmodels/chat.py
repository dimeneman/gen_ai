from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)
model="gemini-3.5-flash-lite"
print("Client created")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="How good is breaking bad."
)

print(response.text)