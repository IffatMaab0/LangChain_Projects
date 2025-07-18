## Modifying Agent Using Langchain

import os
from dotenv import load_dotenv
from groq import Groq
import requests
from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq


load_dotenv()

@tool
def get_weather(city: str) -> str:
    "Get the current weather in a given city using OpenWeather API."
    api_key=os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res= requests.get(url)
    data = res.json()

    if res.status_code == 200:
        temp = data["main"]["temp"]
        desc= data["weather"][0]["description"]
        return f"{city}'s temperature is {temp}°C with {desc}."
    else:
        return "Failed to fetch weather"
llm = ChatGroq(
    model = "llama3-70b-8192",
    api_key= os.getenv("GROQ_API_KEY"),
) 

agent = initialize_agent(
    tools = [get_weather],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)
ques = input("Which city weather information do you need? ")
agent.invoke(ques)