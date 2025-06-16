import streamlit as st
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_llm = ChatGroq(model="llama3-70b-8192")

from typing import TypedDict,Annotated,Literal,Optional

class Review(TypedDict):
    Summary:str
    Sentiment:str


# TypeDict is used for the representation perpose not for data validation

class Review(TypedDict):
    key_themes:Annotated[list[str],"Write down all the key themes discussed in the reviews"]
    Summary:Annotated[str,"Brief Summary of Reviews"]
    Sentiment:Annotated[Literal['pos','neg'],"Return the sentiment of Reviews"]
    pros:Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons:Annotated[Optional[list[str]],"Write down all the cons inside a list"]
    name:Annotated[Optional[str],"Write down the name of reviewer"]



# from langchain_core.output_parsers import StrOutputParser

structure_llm = groq_llm.with_structured_output(Review)

query = "Nothing, it was my terrible experience ever. I like nothing about EY. Work culture, office politics is there. No one is helpful at all They have backward thinking about female employees. Same old school mentality is seen."


result = structure_llm.invoke(query)

print(result)

# {'Sentiment': 'Negative', 'Summary': 'Terrible experience at EY'}
# {'Sentiment': 'neg', 'Summary': 'Terrible experience', 'cons': ['office politics', 'unhelpful colleagues', 'backward thinking about female employees'], 'key_themes': ['bad work culture'], 'name': '', 'pros': []}