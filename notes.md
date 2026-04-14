HERE all the keywords and explanation is written about the langchain and the projects that i have made for the future referneces

1. Stream=True (streaming basically hepls in retuning the answers or the response generated immmediately without them been stored inthe buffer that leads to the later responses)
2. StrOutputParser() is basically used to show only the content and not the other information like the lists and all
3. Chains-> Chains are really important in the langchain as that allows to follow a pipeline like doing the work step by step. Instead of giving the full prompt to do the work chains allows work to be divided to generate an even better response
4. Dynamic prompt template-> This is used instead of normal human message and the systemmessage as the templates can be reused unlike normal messages.
5. @st.cache_resource decorator is used to prevent llm model to reload everythime as it can stored in the cache forever otherwise it would take time the other time when opening the application again
6. State_session is used to keep the history of the chats in the llm otherwise after every message the chat would disappear
7. 