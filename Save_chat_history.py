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
