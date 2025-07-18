## first agent without using any Framework(langchain)

from groq import Groq
from dotenv import load_dotenv
import os
import requests

load_dotenv()

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    res = requests.get(url)  
    data = res.json()        

    if res.status_code == 200:  
        temp = data['main']['temp']  
        condition = data['weather'][0]['description']  
        humidity = data['main']['humidity']  
        return f"The current temperature in {city} is {temp}°C with {condition} and humidity at {humidity}%."
    else:
        return "Sorry, I couldn't fetch the weather right now."
    
start = Groq(api_key= os.getenv("GROQ_API_KEY"))

weather_info = get_weather("Lahore")

response = start.chat.completions.create(
    model ="llama3-70b-8192",
    messages=[
        {"role" : "user", "content":f"The user asked about the current weather in lahore,here is the real weather dat:{weather_info}write a one liner natural response"}
    ]

)

print(response.choices[0].message.content)