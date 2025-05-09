import requests

# Option 1: Set API key directly (for testing only)
GROQ_API_KEY = "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"

# Option 2: Use environment variable (recommended for production)
# import os
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_CHAT_URL = "https://api.groq.com/openai/v1/chat/completions"

def get_resume_feedback(resume_text):
    prompt = f"""
You're a resume critique expert. Analyze the following resume and give structured feedback in:
1. Grammar and clarity
2. Structure and formatting
3. Skill gaps and relevance
4. ATS compatibility
5. Suggested improvements

Resume:
\"\"\"{resume_text}\"\"\"
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(GROQ_CHAT_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"⚠️ LLM Error: {response.status_code} - {response.text}"
