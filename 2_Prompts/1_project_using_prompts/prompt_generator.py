from langchain_core.prompts import PromptTemplate
from langchain_core.load import dumpd
import json


# Purpose of this file: 
# This script creates a complex prompt and saves it as an external JSON file (template.json).
# The main advantage of doing this is "Separation of Concerns". 
# By saving the prompt externally, you keep your main application code (like prompt_ui.py) clean 
# and avoid cluttering it with massive blocks of text. It also allows you to reuse, update, 
# or share this exact prompt across different projects without changing your actual Python code.

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
    # input_variables tells LangChain which placeholders must be filled when this template is used
    input_variables=['paper_input', 'style_input','length_input'],
    # validate_template ensures all listed input_variables actually exist inside the template string above
    validate_template=True
)

# Export the prompt object to a JSON file using the modern, non-deprecated way.
# 1. We convert the template object into a serializable dictionary using dumpd
template_dict = dumpd(template)

# 2. We write that dictionary to a JSON file
with open('template.json', 'w') as f:
    json.dump(template_dict, f, indent=4)