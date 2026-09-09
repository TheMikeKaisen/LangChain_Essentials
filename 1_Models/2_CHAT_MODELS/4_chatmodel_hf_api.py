# Import the function to load environment variables (like API keys) from a .env file
from dotenv import load_dotenv
from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace,
)

# Load the environment variables from the .env file so the Hugging Face API token is available
load_dotenv()

# HuggingFaceEndpoint: Connects to a Hugging Face model hosted on their API
# We specify the repository ID, task type, and generation parameters
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-8B",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.7,
)

# ChatHuggingFace: A wrapper that converts the base LLM into a chat-compatible model, 
# allowing it to properly format conversational messages and roles
chat = ChatHuggingFace(llm=llm)

# Send a prompt to the chat model
response = chat.invoke("When is Independance day of India?")

# Print the model's response content to the console
print(response.content)