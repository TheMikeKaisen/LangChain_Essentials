from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

# Initialize the embedding model. This model converts our raw text into 
# high-dimensional numerical vectors (embeddings) that capture semantic meaning.
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

# Convert all our documents into a matrix of embedding vectors. 
# We do this so we can mathematically compare their meanings to our query.
doc_embeddings = embedding.embed_documents(documents)

# Convert the user's query into a single embedding vector in the exact same vector space.
query_embedding = embedding.embed_query(query)

# Compute the cosine similarity between the query vector and every document vector.
# Cosine similarity measures the angle between vectors (values closer to 1 mean they are semantically similar).
# The function expects 2D arrays and returns a 2D matrix of scores, so we slice [0] to get the 1D array of scores for our single query.
scores = cosine_similarity(
    [query_embedding],
    doc_embeddings
)[0]

# np.argmax efficiently scans the array and returns the index of the highest score.
# This index corresponds directly to the document that best matches our query's meaning.
best_match_index = np.argmax(scores)

print("Query:")
print(query)

print("\nBest Match:")
print(documents[best_match_index])

print("\nSimilarity Score:")
print(scores[best_match_index])