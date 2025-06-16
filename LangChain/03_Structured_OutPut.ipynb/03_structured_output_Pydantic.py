import streamlit as st
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_llm = ChatGroq(model="llama3-70b-8192")

from typing import TypedDict,Annotated,Literal,Optional
from pydantic import BaseModel,Field
# class Review(TypedDict):
#     Summary:str
#     Sentiment:str


# TypeDict is used for the representation perpose not for data validation

class Review(BaseModel):
    key_themes:list[str]=Field(description="Write down all the key themes discussed in the reviews")
    Summary:str=Field(description="Brief Summary of Reviews")
    Sentiment:Literal['pos','neg']=Field(description="Return the sentiment of Reviews")
    pros:Optional[list[str]]=Field(description="Write down all the pros inside a list")
    cons:Optional[list[str]]=Field(description="Write down all the cons inside a list")
    name:Optional[str]=Field(description="Write down the name of reviewer")



# from langchain_core.output_parsers import StrOutputParser

structure_llm = groq_llm.with_structured_output(Review)

query = "Nothing, it was my terrible experience ever. I like nothing about EY. Work culture, office politics is there. No one is helpful at all They have backward thinking about female employees. Same old school mentality is seen."


result = structure_llm.invoke(query)

print(result)

# {'Sentiment': 'Negative', 'Summary': 'Terrible experience at EY'}
# {'Sentiment': 'neg', 'Summary': 'Terrible experience', 'cons': ['office politics', 'unhelpful colleagues', 'backward thinking about female employees'], 'key_themes': ['bad work culture'], 'name': '', 'pros': []}