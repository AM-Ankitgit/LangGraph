from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage


from dotenv import load_dotenv
import os
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_llm = ChatGroq(model="llama3-70b-8192")

chat_history = [
    SystemMessage(content="Your are expert ai model"),
]
while True:
    query = input("You:")
    chat_history.append(HumanMessage(content=query))
    if query=='Exit':
        break
    
    # print(chat_history)
    res= groq_llm.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))
    res = f"AI:{res.content}"
    print(res)