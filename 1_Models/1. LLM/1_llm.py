from dotenv import load_dotenv
from langchain_openai import OpenAI # Import the OpenAI LLM class from the langchain package

# Load the environment variables from the .env file so the OpenAI API key is available
load_dotenv()

# Initialize the OpenAI language model
# We specify the model version and set the 'temperature' 
# (higher temperature = more creative/random output, 0 = deterministic)
llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0.7
)

# Send a prompt to the language model and store its generated response
response = llm.invoke("Explain LangChain in one paragraph.")

print(response)