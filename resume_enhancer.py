import requests

GROQ_API_KEY = "Your Groq api key"
GROQ_CHAT_URL = "https://api.groq.com/openai/v1/chat/completions"

def enhance_resume(resume_text, jd_text):
    prompt = f"""
You are a resume optimization assistant.

Given the following resume and job description, rewrite the resume to maximize its alignment with the job description. Keep the original structure and tone, but improve keywords, highlight matching skills, and add relevant experiences if appropriate.

Resume:
\"\"\"
{resume_text}
\"\"\"

Job Description:
\"\"\"
{jd_text}
\"\"\"

Now provide the enhanced version of the resume:
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(GROQ_CHAT_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Enhancement error {response.status_code}: {response.text}")

