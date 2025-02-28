import requests

API_KEY = "14eabd44702e55da1fd9e0c73c0402da"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    parameters={'q':city, 'appid':API_KEY, 'units':"metric"}
    response= requests.get(BASE_URL, params=parameters)
    if response.status_code==200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("Error- You hurt Hitler")


city_name=input("Enter City name")
get_weather(city_name)
