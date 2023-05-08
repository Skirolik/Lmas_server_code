import requests
from pprint import pprint
from datetime import datetime
import sqlite3
import pandas as pd
from sqlalchemy import create_engine



def lmas_weather(lat,lon,mac_id):
    API_Key = "7eb48147dc3982995adfcff0518e670d"
    Weather_desription = []
    date_and_time = []
    temperature = []
    weather_id = []
    true=1
    false=0

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid="

    final_url = weather_url + API_Key

    weather_data = requests.get(final_url).json()
    pprint(weather_data)

    ## saving all current data in database

    df_forecast = pd.DataFrame()

    prediction_num = 0


    current_time = []
    own_city_id = []
    city = []
    latitude = []
    longitude = []
    country = []


    sunrise = []
    sunset = []
    temperature = []
    temperature_feel = []
    temperature_min = []
    temperature_max = []
    pressure = []
    humidity = []
    main = []
    main_description = []
    clouds = []
    wind_speed = []
    wind_degree = []
    visibility = []

    # Add JSON Data to the lists

    own_city_id.append(weather_data['id'])

    city.append(weather_data['name'])
    latitude.append(weather_data['coord']['lat'])
    longitude.append(weather_data['coord']['lon'])
    country.append(weather_data['sys']['country'])
    sunrise.append(weather_data['sys']['sunrise'])
    sunset.append(weather_data['sys']['sunset'])
    temperature.append(weather_data['main']['temp'])
    temperature_feel.append(weather_data['main']['feels_like'])
    temperature_min.append(weather_data['main']['temp_min'])
    temperature_max.append(weather_data['main']['temp_max'])
    pressure.append(weather_data['main']['pressure'])
    humidity.append(weather_data['main']['humidity'])
    main.append(weather_data['weather'][0]['main'])
    main_description.append(weather_data['weather'][0]['id'])
    clouds.append(weather_data['clouds']['all'])
    wind_speed.append(weather_data['wind']['speed'])
    wind_degree.append(weather_data['wind']['deg'])
    visibility.append(weather_data['visibility'])







    Weather_desription.append(weather_data ['weather'][0]['id'])
    # Weather_desription.append(803)
    humidity = weather_data['main']['humidity']
    temp = weather_data['main']['temp']
    print('Weather is:', Weather_desription[0])

    print(current_time)

    if Weather_desription[0] == 804:
        return true


    elif 650 >= Weather_desription[0] >= 200:
        return true
    elif 771 >= Weather_desription[0] >= 701:
        return false
    elif Weather_desription[0] == 781:
        return true
    elif Weather_desription[0] == 800:
        return false

    ##if the predicion is 803 ie bbroken clouds: 51-84% check next hour prediction to see if the condition changes
    ##if condition changes from broken to overcast or rain then hoot else not

    elif Weather_desription[0] == 803:
        data = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={API_Key}'

        data = requests.get(data).json()
        pprint(data['hourly'][1]['weather'][0]['id'])
        weather_id.append(data['hourly'][1]['weather'][0]['id'])

        if weather_id[0] == 804:
            return true
        elif 650 >= weather_id[0] >= 200:
            return true
        elif 771 >= weather_id[0] >= 701:
            return false
        elif weather_id[0] == 781:
            return true
        elif weather_id[0] == 800:
            return false
        else:
            return false

    else:
        return false



