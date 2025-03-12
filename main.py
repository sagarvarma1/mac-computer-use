import os
import openai
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

response = client.chat.completions.create(
  model="llama-3.3-70b-versatile",
  messages=[
    {"role": "system", "content": "You are a travel agent. Be descriptive and helpful."},
    {"role": "user", "content": "Tell me the top 3 things to do in San Francisco"},
  ]
)

print(response.choices[0].message.content)