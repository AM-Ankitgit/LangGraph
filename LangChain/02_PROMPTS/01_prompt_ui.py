
import streamlit as st
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_llm = ChatGroq(model="llama3-70b-8192")


# print(res)
st.header("AI-Bot") 


# res = groq_llm.invoke("hi")
# st.write(res.content)


# static prompt 
# prompt= st.text_input("say something",)

# dynamic promt

# for taking input create dropdown

paper_name = st.selectbox("Select Research Paper Name",["Select...","Attention is all you need","BERT: Pretraining of deep bidirectional transformers","GPT-3:Language models","SORA"])

style_input = st.selectbox("Select Explaination Style",["Beginner","Technical","Mathematically"])

length_input = st.select_slider("select the length of output in Lines",["1","4","10","20","30"])


from langchain_core.prompts import PromptTemplate,load_prompt


# template  =  f"""You are expert in Summarizing the research paper \n
# name of the paper is :{paper_name}\n
# paper summurization style is : {style_input}\n
# summarized the paper in  : {length_input} line
# """



# template = ChatPromptTemplate(messages=(
#     "system","""You are expert in Summarizing the research paper \n
#     name of the paper is :{paper_name}\n
#     paper summurization style is : {style_input}\n
#     summarized the paper in  : {length_input} line
#     """),

#     input_variables= ['paper_name','style_input','length_input'],  # validate_template is used to validate this field
#     validate_template= True
#     )


# load the template from json for resuability

template = PromptTemplate(
        template="""
        You are expert in Summarizing the research paper \n name of the paper is :"{paper_name}"\n 
        paper summurization style is : "{style_input}"\n 
        summarized the paper in  : "{length_input}" line
        """,

    input_variables= ['paper_name','style_input','length_input'],  # validate_template is used to validate this field
    validate_template= True
    )

# template = load_prompt("prompt_template")
# prompt = template.invoke({"paper_name":paper_name,
#                          "style_input":style_input,
#                          "length_input":length_input})


if st.button("Sumbit"):
        # template = load_prompt("prompt_template.json")
        chain  = template| groq_llm 
        response = chain.invoke({"paper_name":paper_name,
                         "style_input":style_input,
                         "length_input":length_input}
                         )
        
        st.write(response.content)
        st.balloons()
        st.snow()

