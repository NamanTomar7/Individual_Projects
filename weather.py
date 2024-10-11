import requests

API_KEY ='aecd02e36cd2518635c0aca2d537668d'
city = input("Enter city name: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}")

weather=weather_data.json()['weather'][0]['main']
temp=round(weather_data.json()['main']['temp'])
celcius=round((temp-32)*5/9)

if weather_data.json()['cod']!='404':
    print(f"The weather Condition in {city}:- ")
    print("Weather-",weather)
    print("Temp.-",celcius,"")
else:
    print("City not found")    