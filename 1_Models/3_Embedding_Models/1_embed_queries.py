from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

query = "Tell me about Virat Kohli"

query_embedding = embedding.embed_query(query)

print(f"Dimensions: {len(query_embedding)}")
print(query_embedding)