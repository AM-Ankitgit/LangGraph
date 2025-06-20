import os
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-70b-8192")


from langchain_core.prompts import PromptTemplate

prompt1 = PromptTemplate(
    template="write a joke about {topic} in hindi",
    input_variables=['topic']
)


from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
     
prompt2 = prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

from langchain_core.runnables import RunnableSequence

final_chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

result = final_chain.invoke({"topic":"What is AI stablity in ai"})
print(result)