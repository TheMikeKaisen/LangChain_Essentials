# Import the pipeline function from the Hugging Face transformers library
from transformers import pipeline

from langchain_huggingface import (
    HuggingFacePipeline,
    ChatHuggingFace,
)

# Load a local Hugging Face model and tokenizer for text generation
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=200,
)

# HuggingFacePipeline: A LangChain wrapper that lets us use the local Hugging Face pipeline as a standard LLM
llm = HuggingFacePipeline(pipeline=pipe)

# ChatHuggingFace: A wrapper that converts the base LLM into a chat-compatible model, 
# allowing it to properly format conversational messages and roles
chat = ChatHuggingFace(llm=llm)

# Send a prompt to the chat model
response = chat.invoke("What is artificial intelligence?")

# Print the model's response content to the console
print(response.content)