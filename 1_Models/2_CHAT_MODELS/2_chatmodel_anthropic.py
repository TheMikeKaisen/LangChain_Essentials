# Import the function to load environment variables (like API keys) from a .env file
from dotenv import load_dotenv
# Import the Anthropic chat model class from the langchain_anthropic package
from langchain_anthropic import ChatAnthropic

# Load the environment variables from the .env file so the Anthropic API key is available
load_dotenv()

# Initialize the Anthropic chat model
# We specify the model version and set the 'temperature' 
# (higher temperature = more creative/random output)
model = ChatAnthropic(
    model="claude-sonnet-4",
    temperature=0.5
)

# Send a prompt to the chat model and store its generated response
response = model.invoke("Explain transformers.")

# Print the model's response content to the console
print(response.content)