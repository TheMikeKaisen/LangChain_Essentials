from dotenv import load_dotenv
from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace,
)

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-8B",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.7,
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("When is Independance day of India?")

print(response.content)