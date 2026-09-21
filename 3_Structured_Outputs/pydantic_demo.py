"""
Pydantic is a data validation and settings management library for Python.
It uses standard Python type hints to validate data and ensure it matches the expected types.

Key features of Pydantic:
1. Data Validation: It checks if the provided data matches the specified types. If not, it raises a helpful error.
2. Data Parsing/Casting: It tries to automatically convert data to the correct type if possible (e.g., converting a string "32" to an integer 32).
3. Structured Data: It's widely used in AI (like LangChain), FastAPI, and other libraries to ensure structured outputs and inputs.
"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# To create a Pydantic model, you inherit from BaseModel.
# A model defines the structure and types of your data.
class Student(BaseModel):
    # 'name' must be a string. If not provided, it defaults to 'Karthik'.
    name: str = 'Karthik'
    
    # 'age' is an integer, but it's optional. It defaults to None.
    age: Optional[int] = None
    
    # 'email' must be a valid email address string (enforced by EmailStr).
    email: EmailStr
    
    # 'cgpa' is a float. We use Field() to add extra validation (greater than 0, less than 10) and metadata.
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')

# Here we have raw data, usually coming from an API, user input, or an LLM.
# Notice 'age' is a string here, but the model expects an int.
new_student = {'age':'32', 'email':'  abc@gmail.com  '}

# 1. Instantiation & Validation: 
# When we pass the dictionary to Student, Pydantic automatically validates it.
# 2. Data Casting:
# Since 'age' was passed as a string ('32'), Pydantic automatically converts (casts) it to an integer (32) because of the `age: Optional[int]` type hint.
student = Student(**new_student)

print(student)

# We can easily convert the validated model back into a standard Python dictionary.
student_dict = dict(student)
print(student_dict)

# Now 'age' is a proper integer (32), not a string ('32').
print(student_dict['age'])

# Pydantic models also have built-in methods for serialization, 
# like converting the model directly to a JSON string.
student_json = student.model_dump_json()

print(student_json)