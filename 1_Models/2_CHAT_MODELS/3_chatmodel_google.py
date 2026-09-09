# Import the function to load environment variables (like API keys) from a .env file
from dotenv import load_dotenv
# Import the Google chat model class from the langchain_google_genai package
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the environment variables from the .env file so the Google API key is available
load_dotenv()

# Initialize the Google chat model
# We specify the model version, max tokens, and set the 'temperature' 
# (higher temperature = more creative/random output)
model = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",
    max_tokens=500,
    temperature=1.9
)

# Send a prompt to the chat model and store its generated response
response = model.invoke("When is Independance day of India?")

# For this specific model, we access the text inside the first item of the response content
print(response.content[0]['text'])