from langchain_core.prompts import ChatPromptTemplate
# in chatpromptemplate we cannot use the direct in build systemmessage class
# SystemMessage(content="Your are expert ai model"),
# instead we need to add like ("systema","Your are expert ai model") 
# same for other messages





from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_llm = ChatGroq(model="llama3-70b-8192")

template = ChatPromptTemplate(
    [
        ("system","your ai expert {domain}")
        ,("human","Explain in term what is {topic}")
        ]
        )


prompt = ({"domain":"LifeScince","topic":"Life"})

chain  = template | groq_llm
res = chain.invoke(prompt)

print(res.content)




