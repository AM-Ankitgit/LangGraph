import os
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-70b-8192")


from langchain_core.prompts import PromptTemplate

promt1 = PromptTemplate(
    template="Generate the tweet on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(template="Generate the linkedin post about the {topic}",
                         input_variables=['topic'])

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

from langchain_core.runnables import RunnableParallel,RunnableSequence

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(promt1,model,parser),
    "linkedin":RunnableSequence(prompt2,model,parser)
})


result = parallel_chain.invoke({"topic":"AI Commentory"})

print(result)