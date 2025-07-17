import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv() 
groq_key = os.environ["GROQ_API_KEY"]
llm = ChatGroq(
    model = "llama3-70b-8192",
    groq_api_key=groq_key
)
prompt = PromptTemplate.from_template("what is the capital of {place}")
pipeline = prompt | llm
output = pipeline.invoke("pakistan")
print(output.content)