import requests
import json
from os import environ 

def get_wind_direction():
    weather_bearing = json["wind"]["deg"]
    wind_speed_mph = get_wind_speed()
    if wind_speed_mph != 0:
        if weather_bearing in range(315, 360) or weather_bearing in range(0, 45):
            wind_direction = "north"
        elif weather_bearing in range(45, 135):
            wind_direction = "east"
        elif weather_bearing in range(225, 315):
            wind_direction = "west"
        else:
            wind_direction = "south"
        print(f"There is a {wind_speed_mph}mph {wind_direction}erly wind")
        print(f"The raw wind degs is: {weather_bearing}")
    else:
        print(f"There is no wind to have a direction!")
       

def get_wind_speed():
    wind_speed = json["wind"]["speed"]
    wind_speed_mph = round(wind_speed * 2.237,2)
    return wind_speed_mph

def get_daylight_percentage():
    sunset = json["sys"]["sunset"]
    sunrise = json["sys"]["sunrise"]
    percentage_day = round(100*(int(sunset) - int(sunrise))/(24*3600),2)
    return f"{percentage_day}% of the day is actually day!!!! :O"


base_url = "https://api.openweathermap.org/data/2.5/weather?"

location = input("where bouts m8? ")
api_key = environ.get("WEATHER_API")

complete_url = f"{base_url}q={location}&appid={api_key}"



response = requests.get(complete_url)
json = response.json()
if json['cod'] == '404':
    print("nonononononononononononono")
else:
    weather_broad = json["weather"][0]["main"]
    weather_precise = json["weather"][0]["description"]
    temp = round(json["main"]["temp"] - 273.15,2)
    
    print(f"Weather: {weather_broad} ({weather_precise})")
    print(f"Temp (C) = {temp}")
    get_wind_direction()
    print(get_daylight_percentage())

