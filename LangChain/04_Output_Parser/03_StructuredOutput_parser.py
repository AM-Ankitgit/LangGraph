from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_core.prompts import PromptTemplate


load_dotenv()
import os

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama3-70b-8192")



# To solve the problem of jsonoutput parse we can use the structure output parser



responseschema = [
    ResponseSchema(name='fact1',description="Fact 1 about the topic"),
    ResponseSchema(name='fact2',description="Fact 2 about the topic"),
    ResponseSchema(name='fact3',description="Fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(response_schemas=responseschema)

# for this we need the schema

template = PromptTemplate(
    template="Give 3 Fact about {topic}\n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({"topic":"black hole"})
print(result)

# using the StructureOutput Parser we cannot peform the data validation

{'fact1': 'A black hole is a region in space where the gravitational pull is so strong that nothing, including light, can escape. It is formed when a massive star collapses in on itself.', 
 'fact2': "The point of no return, called the event horizon, marks the boundary of a black hole. Once something crosses the event horizon, it is trapped by the black hole's gravity.", 
 'fact3': 'Black holes come in various sizes, ranging from small, stellar-mass black holes formed from the collapse of individual stars, to supermassive black holes found at the centers of galaxies, with masses millions or even billions of times that of the sun.'}

