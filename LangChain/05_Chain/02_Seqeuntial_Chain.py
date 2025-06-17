from dotenv import load_dotenv
from langchain_groq import ChatGroq

import os

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-70b-8192")


from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


template1 = PromptTemplate(template="Generate detail report on following topic\n {topic}",
                           input_variables=['topic']
                           )


template2 = PromptTemplate(template="give 1 line summary of generated report\n{report}",
                           input_variables=['report'])

parser = StrOutputParser()

chain =  template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic":"inflation"})
# print(result)

chain.get_graph().print_ascii()



#      +-------------+       
#      | PromptInput |
#      +-------------+
#             *
#             *
#             *
#     +----------------+
#     | PromptTemplate |
#     +----------------+
#             *
#             *
#             *
#       +----------+
#       | ChatGroq |
#       +----------+
#             *
#             *
#             *
#    +-----------------+
#    | StrOutputParser |
#    +-----------------+
#             *
#             *
#             *
# +-----------------------+
# | StrOutputParserOutput |
# +-----------------------+
#             *
#             *
#             *
#     +----------------+
#     | PromptTemplate |
#     +----------------+
#             *
#             *
#             *
#       +----------+
#       | ChatGroq |
#       +----------+
#             *
#             *
#             *
#    +-----------------+
#    | StrOutputParser |
#    +-----------------+
#             *
#             *
#             *
# +-----------------------+
# | StrOutputParserOutput |
# +-----------------------+

