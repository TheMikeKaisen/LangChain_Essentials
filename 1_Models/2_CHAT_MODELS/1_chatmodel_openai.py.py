# Import the function to load environment variables (like API keys) from a .env file
from dotenv import load_dotenv
# Import the OpenAI chat model class from the langchain_openai package
from langchain_openai import ChatOpenAI

# Load the environment variables from the .env file so the OpenAI API key is available
load_dotenv()

# Initialize the OpenAI chat model
# We specify the model version and set the 'temperature' 
# (higher temperature = more creative/random output)
model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7
)

# Send a prompt to the chat model and store its generated response
response = model.invoke("What is LangChain?")

# Print the model's response content to the console
print(response.content)