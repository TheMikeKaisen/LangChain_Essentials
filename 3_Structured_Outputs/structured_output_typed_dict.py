"""
Structured Output using TypedDict in LangChain.

This script demonstrates how to force an LLM (Google Gemini) to return data in a specific, 
structured format (a Python dictionary) rather than arbitrary free-form text.

Key Concepts:
1. TypedDict: Defines the schema (keys and data types) for the output dictionary.
2. Annotated: Allows us to attach human-readable descriptions to fields. 
   LangChain passes these descriptions to the LLM so it knows what to extract for each field.
3. with_structured_output(): Wraps the LLM model to enforce the schema, returning a dictionary.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

# Initialize the Gemini chat model
model = ChatGoogleGenerativeAI(model='gemini-flash-lite-latest')

# Define the schema using Python's TypedDict.
# The LLM will be instructed to return a dictionary matching this structure.
class Review(TypedDict):

    # Annotated[type, "description"]: The description guides the LLM on what content belongs here.
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    
    # Literal["pos", "neg"]: Restricts the LLM output to strictly one of these choices.
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    
    # Optional[list[str]]: Field can either be a list of strings or None if not present in input.
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

# Bind the schema to the model.
# structured_model now returns a Python dict matching the 'Review' TypedDict structure.
structured_model = model.with_structured_output(Review)

# Pass raw, unstructured text to the structured model
result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

# Print the full extracted dictionary object
print(result)

# Access individual fields directly from the resulting dictionary
print(result['name'])