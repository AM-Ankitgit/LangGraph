from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()
import os

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-70b-8192")

parser = JsonOutputParser()  # using jsonoutputparse cannot get  desired json structure output

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)


# output for first execution with same input 
# {'fact1': {'description': 'Definition', 'value': 'A black hole is a region in space where the gravitational pull is so strong that nothing, including light, can escape.'}, 
# 'fact2': {'description': 'Formation', 'value': 'Black holes are formed when a massive star collapses in on itself and its gravity becomes so strong that it warps the fabric of spacetime.'}, 
# 'fact3': {'description': 'Singularity', 'value': 'At the center of a black hole lies a point called a singularity, where the density and gravity are infinite and the laws of physics as we know them break down.'}, 
# 'fact4': {'description': 'Event Horizon', 'value': 'The point of no return around a black hole is called the event horizon, which marks the boundary beyond which anything that enters cannot escape.'}, 


# output for second execution with same input  which is different format so that json schema not be fixed

# {'fact1': 'A black hole is a region in space where the gravitational pull is so strong that nothing, including light, can escape.', 
#  'fact2': 'Black holes are formed when a massive star collapses in on itself and its gravity becomes so strong that it warps the fabric of spacetime.',
#  'fact3': 'The center of a black hole is called a singularity, where the density and gravity are infinite and the laws of physics as we know them break down.', 
#  'fact4': 'Black holes can come in various sizes, ranging from small, stellar-mass black holes formed from the collapse of individual stars, to supermassive black holes found at the centers of galaxies, with masses millions or even billions of times that of our sun.',
#  'fact5': "According to Einstein's theory of general relativity, black holes distort spacetime, causing strange effects such as gravitational lensing, where the light from distant objects is bent around the black hole, and time dilation, where time appears to slow down near the event horizon."}