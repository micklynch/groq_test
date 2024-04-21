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
            "content": "Create a 7 day menu for a family of three. We want to mostly eat vegetarian and high protein but can include meat on some days. There should be leftovers that can be used for lunch on subsequent days. The menu should be easy and quick to prepare, and be toddler friendly. The output should be a menu, a list of ingredients and preparation instructions.",
        }
    ],
    # model="mixtral-8x7b-32768",
    model="llama3-70b-8192",
)

# Write the output to a markdown file
def write_to_markdown(text, filename):
    with open(filename, 'w') as f:
        f.write(text)

menu = chat_completion.choices[0].message.content
write_to_markdown(menu, "menu.md")
