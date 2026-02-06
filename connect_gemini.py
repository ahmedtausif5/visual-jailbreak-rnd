import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: API Key not found.")
    exit()

client = genai.Client(api_key=api_key)

print("Sending message to Gemini...")

try:
    response = client.models.generate_content(
        model="gemini-flash-latest", 
        contents="Hello! Are you online?"
    )
    
    print("\nSuccess! Gemini replied:")
    print("-" * 30)
    print(response.text)
    print("-" * 30)

except Exception as e:
    print(f"\nError: Could not connect. Reason: {e}")