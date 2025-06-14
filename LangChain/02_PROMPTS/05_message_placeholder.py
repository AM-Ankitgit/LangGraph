from langchain.prompts import MessagesPlaceholder,ChatPromptTemplate

# MessagesPlaceholder :  this is use to handle chathistory we can bring the proper chat history in the conversion

template = ChatPromptTemplate([
    ("system", "you are expert ai moodle"),
    (MessagesPlaceholder(variable_name="chat_history")),
    ("human","Please Specify your query here {query}")
])

from pathlib import Path
chat_history = [] 
# we load chat_history from the database 
with open(Path("LangChain\\02_PROMPTS\\chat_history.txt")) as f:
    chat_history.extend(f.readlines())

# print(chat_history)
prompt =({"chat_history":chat_history,"query":"how should i plan my trip to us"})

from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_llm = ChatGroq(model="llama3-70b-8192")



chain =  template | groq_llm

res = chain.invoke(prompt)
print(res.content)

chat_history.extend(res)

print(chat_history)