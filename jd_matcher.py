#import requests
#from sklearn.metrics.pairwise import cosine_similarity

#GROQ_API_KEY = "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"
#GROQ_EMBED_URL = "https://api.groq.com/openai/v1/embeddings"

#def truncate(text, max_chars=4000):
  #  return text[:max_chars]

#def get_embedding(text):
  #  headers = {
   #     "Authorization": f"Bearer {GROQ_API_KEY}",
   #     "Content-Type": "application/json"
  #  }

  #  payload = {
   #     "model": "nomic-embed-text-v1",
  #      "input": truncate(text)
   # }

  #  response = requests.post(GROQ_EMBED_URL, headers=headers, json=payload, timeout=10)
  #  if response.status_code == 200:
   #     return response.json()["data"][0]["embedding"]
 #   else:
   #     raise Exception(f"Embedding error {response.status_code}: {response.text}")

#def match_resume_to_jd(resume_text, jd_text):
 #   try:
   #     resume_emb = get_embedding(resume_text)
    #    jd_emb = get_embedding(jd_text)
    #    score = cosine_similarity([resume_emb], [jd_emb])[0][0]
    #    return round(score * 100, 2)
 #   except Exception as e:
     #   return f"⚠️ Matching Error: {e}"



from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load a light and effective local model
model = SentenceTransformer("all-MiniLM-L6-v2")

def truncate(text, max_chars=4000):
    return text[:max_chars]

def get_embedding(text):
    text = truncate(text)
    return model.encode(text)

def match_resume_to_jd(resume_text, jd_text):
    try:
        resume_emb = get_embedding(resume_text)
        jd_emb = get_embedding(jd_text)
        score = cosine_similarity([resume_emb], [jd_emb])[0][0]
        return round(score * 100, 2)
    except Exception as e:
        return f"⚠️ Matching Error: {e}"
