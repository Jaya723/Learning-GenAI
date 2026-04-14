import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_groq import Chatgroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Simple LangChain Chatbot using groq", page_icon=":robot_face:")

st.title("Simple LangChain Chatbot using groq")
st.markdown("This is a simple chatbot built using LangChain and the groq language model. It can respond to user queries in a conversational manner.")


