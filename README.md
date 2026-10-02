# gemini-hello

A small script that calls Google's Gemini API, with retry/backoff and proper
error handling. Built as my Phase 0 milestone project for the AI Mastery
roadmap — the goal was practicing a real git/GitHub workflow, virtual
environments, and the basics of making an authenticated API call, not the
specific task the script performs.

## What it does

Sends a single prompt to Gemini (`gemini-3.8-flash`) and prints the response.
If the call fails, it retries up to 5 times with a short backoff before
giving up and reporting the error.

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/gemini-hello.git
cd gemini-hello

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your API key
cp .env.example .env
# then open .env and paste in your real Gemini API key
```

## Run it

```bash
python gemini_hello.py
```

## What I learned

- How to structure a small Python project with a virtual environment and a
  `requirements.txt` that someone else (or future me) can use to reproduce
  the environment exactly.
- Why API keys belong in a `.env` file that's gitignored, never hardcoded —
  and what `.env.example` is for.
- How to write a retry loop correctly: the `try`/`except` has to live
  *inside* the loop (so a single failure doesn't kill every remaining
  attempt), and a successful call needs to `break` out instead of retrying
  needlessly.
- The difference between `.text` (this SDK's way of getting the response
  string) and `.output_text` (a different provider's convention) — a reminder
  that provider SDKs aren't interchangeable even when they look similar.
