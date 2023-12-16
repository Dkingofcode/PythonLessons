import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

def get_current_weather():
    print('\n*** Get Current Weather COnditions ***\n')
    
    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    
    print(request_url)
    
    weather_data = requests.get(request_url).json()
    
    #print(weather_data)
    pprint(weather_data)
    print(f'Weather for {weather_data["name"]} is: {weather_data["weather"][0]["description"]}')
    print(f'temperature for {weather_data["name"]} is {weather_data["main"]["temp"]}')
    
    
if __name__ == "__main__":
          
    get_current_weather()    
    
    
    
    
    