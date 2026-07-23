from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar is known as the God of Cricket.",
    "Rohit Sharma has multiple ODI double centuries.",
    "Jasprit Bumrah is India's premier fast bowler."
]

document_embeddings = embedding.embed_documents(documents)

print(f"Number of embeddings: {len(document_embeddings)}")
print(f"Embedding dimension: {len(document_embeddings[0])}")
print(document_embeddings[0][:10])