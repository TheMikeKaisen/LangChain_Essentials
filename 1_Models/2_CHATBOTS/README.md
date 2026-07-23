# 2. Chatbots (Chat Models)

Welcome to Chat Models! This is the most common way to interact with AI today.

## What are Chat Models?
While standard LLMs take a single string of text and continue it, **Chat Models** are specifically fine-tuned for conversation. They take a list of messages (like "Human", "AI", "System") as input and respond appropriately. This is how tools like ChatGPT work!

## What's in this folder?
Here you will find scripts demonstrating how to build a basic chatbot using different AI providers:
- **1_chatmodel_openai.py**: Connect to OpenAI's models (like GPT-4o).
- **2_chatmodel_anthropic.py**: Connect to Anthropic's models (like Claude 3.5 Sonnet).
- **3_chatmodel_google.py**: Connect to Google's models (like Gemini 1.5 Flash).
- **4_chatmodel_hf_api.py**: Connect to Hugging Face models using their Inference API over the cloud.
- **5_chatmodel_hf_local.py**: Run a smaller Hugging Face model locally on your own machine.

### How to use
To run these files, you need API keys for the respective services. Make sure your `.env` file is set up correctly in the root folder!

If you are a beginner and don't want to spend money on api keys, i suggest you go with google ai studio. Its free tier is generous as of now.