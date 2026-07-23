from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the God of Cricket, holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his yorkers and unique action."
]

query = "Tell me about Dhoni"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity(
    [query_embedding],
    doc_embeddings
)[0]

best_match_index = np.argmax(scores)

print("Query:")
print(query)

print("\nBest Match:")
print(documents[best_match_index])

print("\nSimilarity Score:")
print(scores[best_match_index])