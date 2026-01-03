from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from lanchai_core.output_parsers import StrOutputParser, ResponseSchema

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

os.environ["LANGSERVE_API_KEY"] = os.getenv("LANGSERVE_API_KEY")
os.environ["LANCHAIN-TRACING"] = "true"

# creating chatbot

prompt=ChatPromptTemplate.from_messages
([
    ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
    ("user", "Qusestion:{text_to_translate}")
])

#Streamlit Freamwork

st.title("LangChain Demo with Open AI API")     
input_text=st.text_input("search the topic you want")    

llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7,)
output_parser=StrOutputParser()

#chain
chain=prompt | llm | output_parser

if input_text:
   st.write(chain.invoke({'Question':input_text}))
