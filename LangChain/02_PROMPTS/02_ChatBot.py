from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_llm = ChatGroq(model="llama3-70b-8192")


chat_history = []

chat_history = {"system": "Your are expert ai model"
                ""}

while True:
    query = input("You:")
    chat_history.append(query)
    if query=='Exit':
        break
    
    # print(chat_history)
    res= groq_llm.invoke(chat_history)
    chat_history.append(res.content)
    res = f"AI:{res.content}"
    print(res)