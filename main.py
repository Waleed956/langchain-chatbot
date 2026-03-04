from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="minimax-m2.5:cloud",
    temperature=0.7,

)

prompt  = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()


for chunk in chain.stream({"question": "What is RAG"}):
    print(chunk, end="", flush=True)