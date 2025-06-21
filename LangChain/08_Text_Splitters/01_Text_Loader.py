from langchain_community.document_loaders import TextLoader
from pathlib import Path

from dotenv import load_dotenv
from langchain_groq import ChatGroq

import os

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-70b-8192")



path = Path("LangChain\\08_Text_Splitters\story.txt")
# print(path)


doc1 = TextLoader(path).load()
doc2 = TextLoader(path).lazy_load() # this more useful when hava large data or lot of file  it is geneator object
  # it load all data in  ram that why it take time to run 



for txt in doc2:
    print(txt)

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate


parser=StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

chain = RunnableSequence(prompt,model,parser)

result = chain.invoke({"poem":doc1[0].page_content})
print(result)



