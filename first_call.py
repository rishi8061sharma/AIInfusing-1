# pip install python-dotenv
# pip install openai
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Load .env from the same folder as this Python file
load_dotenv(Path(__file__).resolve().parent / ".env")

# Read Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Check your .env file."
    )

client = Groq(api_key=api_key)

MODEL = "openai/gpt-oss-120b"

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a witty lovely guide."},
        {"role": "user",   "content": "Suggest one thing to do in Bangalore."},
    ],
)
print(response.choices[0].message.content)


# now OpenAI() finds the key automatically — no key in your code 🎉