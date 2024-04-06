from dotenv import load_dotenv
import os
from openai import OpenAI

# Load the .env file
load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url=os.environ.get("GROQ_BASE_URL")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Create a 7 day menu for a family of three. We want to mostly eat vegetarian and high protein. The menu should be easy to prepare and be toddler friendly",
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)


