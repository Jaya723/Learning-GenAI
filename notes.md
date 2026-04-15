## HERE all the keywords and explanation is written about the langchain and the projects that i have made for the future referneces

1. Stream=True (streaming basically hepls in retuning the answers or the response generated immmediately without them been stored inthe buffer that leads to the later responses)
2. StrOutputParser() is basically used to show only the content and not the other information like the lists and all
3. Chains-> Chains are really important in the langchain as that allows to follow a pipeline like doing the work step by step. Instead of giving the full prompt to do the work chains allows work to be divided to generate an even better response
4. Dynamic prompt template-> This is used instead of normal human message and the systemmessage as the templates can be reused unlike normal messages.
5. @st.cache_resource decorator is used to prevent llm model to reload everythime as it can stored in the cache forever otherwise it would take time the other time when opening the application again
6. State_session is used to keep the history of the chats in the llm otherwise after every message the chat would disappear
7. Tools in langchain are basically used for giving the result from the web pages or basically used for web search
8. @tool converts a regular Python function into a LangChain Tool that an AI Agent can use. Without it → just a normal function, LLM can't use it. With @tool → LLM can now decide when to call it automatically
9. Async keyword before def can be used for multitasking and parallel processing
10. Annotated is basically used for adding the description with respect to the arguments or the parameters\
11. For async function use await and ainvoke and for annotated use invoke and for normal function call normally using invoke
12.  StructureTool over @tool (gives more power)
    ->want a different name than function name
    ->want detailed custom description
    ->return result directly without LLM processing
    ->want both sync + async versions
13. In arxiv tool you input the number of the research paper, author name or other parameters from the doc taken from the arxiv site
14. For combining tools to the llm first convert the query into humanmessage and give to the llm and llm with calls the tools and will generate the tool message and combined tool message and the humanmessage is given to llm for the context to get the final result. This is required because LLM has no memory-every call is fresh. So you need to give it the full conversation context for proper answer formation that is why you need to feed again the query

### PROPER EXAMPLE
HumanMessage = Customer asks waiter "What's today's special and total bill?"

AIMessage = Waiter goes to kitchen + cashier (tool calls)

ToolMessage = Kitchen says "Pasta" + Cashier says "₹500"

Final LLM call = Waiter comes back and tells customer
                 "Today's special is Pasta and your bill is ₹500"

15. 