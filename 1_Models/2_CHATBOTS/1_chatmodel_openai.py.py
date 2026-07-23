from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7
)

response = model.invoke("What is LangChain?")

print(response.content)