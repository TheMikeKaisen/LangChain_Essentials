from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

model = ChatAnthropic(
    model="claude-sonnet-4",
    temperature=0.5
)

response = model.invoke("Explain transformers.")

print(response.content)