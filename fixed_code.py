import os
import openai

# Initialize the client with Groq
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

# Example instruction and operating system
instruction = "go and get the weather in san francisco"
operating_system = "macOS"

# Fixed code with correct model name and properly formatted f-string
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # Corrected model name
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": f"""The user has requested this from a computer use llm: {instruction}.
It is your job to figure out the steps to complete the task.
Write me a detailed plan, that includes everything that the llm has to do to achieve this.
The operating system is {operating_system}."""}
        ]}
    ]
)

print(response.choices[0].message.content)

# You can assign the response to a variable if needed
# plan = response.choices[0].message.content 