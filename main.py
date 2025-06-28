import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    api_key = load_api_key()
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="What are the best project management tools for remote teams in 2025?",
    )
    print(response.text)


def load_api_key():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is not set in environment variables.")
        sys.exit(1)
    return api_key


if __name__ == "__main__":
    main()
