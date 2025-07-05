from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq


load_dotenv()

groq_key = os.environ["GROQ_API_KEY"]

model = ChatGroq(
    model="llama3-70b-8192",
    groq_api_key=groq_key  
)
chat_history = []
system_message = SystemMessage(content="You are expert in building AI agents via coding")
chat_history.append(system_message)

while True:
    query = input("you: ")
    if query.lower() == "exit":
       break
    chat_history.append(HumanMessage(content = query))

    result =  model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content = response))
    print(f"AI: ", result.content)

print("--------MessageHistory---------")    
print(chat_history)