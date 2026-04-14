import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(
    page_title="Simple LangChain Chatbot using groq", page_icon=":robot_face:")

st.title("Simple LangChain Chatbot using groq")
st.markdown("This is a simple chatbot built using LangChain and the groq language model. It can respond to user queries in a conversational manner.")

with st.sidebar:
    st.header("Chatbot Settings")
    # api key
    api_key = st.text_input("Enter your groq API Key", type="password",
                            help="GET your free API key from https://console.groq.com/keys to use the chatbot.")

    # model selection
    model_name = st.selectbox("Select groq Model", options=[
                              "llama-3.1-8b-instant", "llama-3.3-70b-versatile"])

    if st.button("Clear Chat"):
        st.session_state["messages"] = []
        st.rerun()

# inititalizing the chat hstory
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# initialize the chosen llm
@st.cache_resource
def get_chain(api_key, model_name):
    if not api_key:
        st.warning("Please enter the api key")
        return None
    # initialize groq model
    llm = ChatGroq(groq_api_key=api_key, model=model_name,
                   temperature=0.7, streaming=True)
    template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that answers question about anything that the user asks."),
        ("human", "{question}")
    ])

    chain = template | llm | StrOutputParser()
    return chain


chain = get_chain(api_key, model_name)

if not chain:
    st.warning("Please enter the API key to initialize the chatbot.")
else:
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    # chat input
    if question := st.chat_input("Ask me anything!"):
        st.session_state["messages"].append(
            {"role": "human", "content": question})
        with st.chat_message("human"):
            st.write(question)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            response = ""
            try:
                for chunk in chain.stream({"question": question}):
                    response += chunk
                    message_placeholder.markdown(response+"▌")
                message_placeholder.markdown(response)
                st.session_state["messages"].append(
                    {"role": "assistant", "content": response})
            except Exception as e:
                message_placeholder.markdown(
                    "Sorry, something went wrong while generating the response.")
                st.error(f"Error: {e}")
