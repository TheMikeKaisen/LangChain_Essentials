from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0.7
)

response = llm.invoke("Explain LangChain in one paragraph.")

print(response)