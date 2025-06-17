from dotenv import load_dotenv
from langchain_groq import ChatGroq

import os

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-70b-8192")


from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


parser=  StrOutputParser()

prompt = PromptTemplate(template="Generate 5 interesting facts about {topic}",
                        input_variables=['topic']
                        )

chain = prompt | model |parser

result = chain.invoke({"topic":"soccker"})

# print(result)

chain.get_graph().print_ascii()
# chain.get_graph().draw_ascii()


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