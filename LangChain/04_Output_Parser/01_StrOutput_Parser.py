from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
import os
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

from langchain_core.prompts import PromptTemplate



os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-70b-8192")

# llm = HuggingFaceEndpoint(repo_id = "google/gemm-2-2b-it",
                        #   task="text-generation",huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN)
# ChatHuggingFace(llm=llm)

#if we are working without StrOutParser and to do the  two taks with same model then we need managed as below
# then we need to managed the code like this


# for detailed report
template1 = PromptTemplate(template="write a detail report on {topic}",
                           input_variables=['topic'])


template2 = PromptTemplate(template=" Generate summary on this 1 line report {report}",
                           input_variables=['report'])


chain = template1 | model | template2 | model

result = chain.invoke({'topic':'black hole'})
print(result)

# but best practise to do this is
print("*"*100)
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
chain = template1 | model | parser|  template2 | model | parser

result = chain.invoke({'topic':'black hole'})
print(result)






