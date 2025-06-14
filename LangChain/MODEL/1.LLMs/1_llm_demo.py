from langchain_groq import ChatGroq
from langchain_groq import ChatGroq


import os
from dotenv import load_dotenv

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_llm = ChatGroq(model="llama3-70b-8192")

response = groq_llm.invoke("what is capital of us")