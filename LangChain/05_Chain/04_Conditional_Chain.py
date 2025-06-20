
import os
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-70b-8192")


from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel,Field
from typing import Literal,Optional
from langchain_core.output_parsers import PydanticOutputParser


parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description="Give the sentiment of the feedback")



parser2 = PydanticOutputParser(pydantic_object=Feedback)


from langchain_core.prompts import PromptTemplate
prompt1 =  PromptTemplate(template="Classify the sentiment of the following feedback text into postive or negative\n{feedback} \n {format_instruction}",
                          input_variables=['feedback'],
                          partial_variables={'format_instruction':parser2.get_format_instructions()})



# we need the condition chain because the output of the llm is never fixed to maintain the output we are mangaging through the conditinal chain
# first take the output from the first chain then connect brach chain  
# in branch we set as if elif and else condition which will give the result


first_chain = prompt1 | model | parser2

print(first_chain.invoke({"feedback":"my mobile display work inappropriate way"}))



# sentiment='negative'

# # we got output like this

positive_prompt =  PromptTemplate(template="Write appropriate response tto this positive feedback \n{feedback}",
                                  input_variables=['feedback'])
negative_prompt =  PromptTemplate(template="Write appropriate response tto this negative feedback \n{feedback}",
                                  input_variables=['feedback'])

# run this both prompt in if elif and else condition

from langchain_core.runnables import RunnableBranch,RunnableLambda

branch_chain = RunnableBranch(
    (lambda x: x.sentiment=='positive',positive_prompt | model | parser),
    (lambda x: x.sentiment=='negative',negative_prompt | model | parser),
    RunnableLambda(lambda x: "Could not find the Sentiment")
)


final_chain = first_chain | branch_chain

result = final_chain.invoke({"feedback":"my mobile display work inappropriate way"})
print(result)


final_chain.get_graph().print_ascii()
