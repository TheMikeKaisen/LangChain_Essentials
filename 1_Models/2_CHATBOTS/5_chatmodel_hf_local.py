from transformers import pipeline

from langchain_huggingface import (
    HuggingFacePipeline,
    ChatHuggingFace,
)

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=200,
)

llm = HuggingFacePipeline(pipeline=pipe)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("What is artificial intelligence?")

print(response.content)