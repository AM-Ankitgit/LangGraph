import os
from langchain_groq import ChatGroq
from langchain.schema import Document

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-70b-8192")

from langchain.tools import StructuredTool
from pydantic import BaseModel,Field

class MultiplyInput(BaseModel):
    a:int=Field(...,description="Enter interger value of a")
    b:int=Field(...,description="Enter interger value of b")  # The ... is a shorthand for saying “no default value, this field is required”.



def multiply(a:int,b:int)->int:
    return a*b

from langchain.tools import StructuredTool

multiply_tool = StructuredTool.from_function(func=multiply,
                                             name="mulitplyfunction",
                                             description="it use to multiple two function",
                                             args_schema=MultiplyInput)

RESULT = multiply_tool.invoke({"a":1,"b":10})

print(RESULT)