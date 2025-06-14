import streamlit as st
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_llm = ChatGroq(model="llama3-70b-8192")

from typing import TypedDict,Annotated

class Review(TypedDict):
    Summary:str
    Sentiment:str


class Review(TypedDict):
    Summary:Annotated[str,"Brief Summary of Reviews"]
    Sentiment:Annotated[str,"Return the sentiment of Reviews"]

# from langchain_core.output_parsers import StrOutputParser

structure_llm = groq_llm.with_structured_output(Review)

query = "Nothing, it was my terrible experience ever. I like nothing about EY. Work culture, office politics is there. No one is helpful at all They have backward thinking about female employees. Same old school mentality is seen."


result = structure_llm.invoke(query)

print(result)

# {'Sentiment': 'Negative', 'Summary': 'Terrible experience at EY'}