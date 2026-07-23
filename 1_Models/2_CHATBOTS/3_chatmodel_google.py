from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",
    max_tokens=500,
    temperature=1.9
)

response = model.invoke("When is Independance day of India?")

print(response.content[0]['text'])