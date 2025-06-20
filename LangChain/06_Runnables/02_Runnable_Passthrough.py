

import os
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-70b-8192")

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence



prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)


parser = StrOutputParser()
joke_gen_chain = RunnableSequence(prompt1,model,parser
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

# to run  the both prompt in parallel
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
parallel_chain = RunnableParallel({
    "joke":RunnablePassthrough(),
    "explaination":RunnableSequence(prompt2,model,parser)
})


combine_seq_parallel_chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = combine_seq_parallel_chain.invoke({"topic":"AI"})
print(result)