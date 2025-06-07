# 🧠 GenAI Resume Critique Bot

An AI-powered Streamlit web application that critiques resumes, matches them with job descriptions, and enhances them using LLMs via the Groq API.

## 🔍 Features

- 📄 **Resume Parsing** — Supports PDF and DOCX formats.
- 🤖 **LLM-based Feedback** — Analyzes resumes and provides suggestions on grammar, structure, skills, ATS-friendliness, and more.
- 📌 **JD Matching** — Matches your resume to a pasted Job Description and gives a similarity score.
- 🛠 **Resume Enhancer** — Rewrites your resume to better align with the job description.

## 🚀 Demo

https://genai-critique-resume-app-exegll6j3zheykfji3y932.streamlit.app/

## 🧰 Tech Stack

- Frontend: [Streamlit](https://streamlit.io/)
- Backend: Python
- Embeddings: `sentence-transformers` (MiniLM model)
- LLMs: Groq API (LLaMA models)
- Resume parsing: `PyMuPDF` for PDF and `python-docx` for DOCX

## 📁 File Structure
├── app.py # Main Streamlit app
├── resume_parser.py # Extracts and parses resume content
├── critique_llm.py # Sends resume to Groq LLM for critique
├── resume_enhancer.py # Enhances resume based on JD
├── jd_matcher.py # Embedding-based similarity matcher
├── requirements.txt # Python dependencies
└── README.md # Project info
