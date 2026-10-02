"""
gemini_hello.py

A tiny script that calls the Gemini API with retry/backoff and basic error
handling. Built as the Phase 0 milestone exercise for the AI Mastery roadmap:
practicing virtual environments, git/GitHub, API calls, JSON/HTTP concepts,
and API key hygiene together in one small, real project.
"""

import os
import time

from dotenv import load_dotenv
from google import genai

# Load variables from a local .env file into the environment.
# .env itself is never committed (see .gitignore) -- only .env.example is.
load_dotenv()


def get_client() -> genai.Client:
    """Build a Gemini client using the API key from the environment."""
    api_key = os.environ.get("GEM_KEY")
    if not api_key:
        raise ValueError(
            "GEM_KEY is not set. Copy .env.example to .env and add your real key."
        )
    return genai.Client(api_key=api_key)


def ask_gemini(client: genai.Client, prompt: str, max_attempts: int = 5) -> str:
    """
    Send a prompt to Gemini, retrying on failure with a short backoff.
    Returns the model's text response, or raises the last error if every
    attempt fails.
    """
    for attempt in range(1, max_attempts + 1):
        try:
            print(f"Attempt {attempt} of {max_attempts}...")
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt,
            )
            return response.text
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == max_attempts:
                raise
            time.sleep(2 * attempt)  # simple linear backoff


def main():
    client = get_client()
    prompt = "Explain how AI works in a few words"
    try:
        answer = ask_gemini(client, prompt)
        print("\nGemini says:")
        print(answer)
    except Exception as e:
        print(f"\nAll attempts failed. Last error: {e}")


if __name__ == "__main__":
    main()
