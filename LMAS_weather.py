import requests
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd
import json

API_Key="7eb48147dc3982995adfcff0518e670d"

Weather_desription=[]
date_and_time=[]
temperature=[]


location= "Sibsagar"

lat = 12.92668
lon=77.59700
date = '2023-04-07'

weather_url = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={API_Key}%20&q={lat}%2C{lon}'

weather_data= requests.get(weather_url).json()
pprint(weather_data)


#
#
# pprint(weather_data ['weather'][0]['description'])
# pprint(weather_data ['weather'][0]['id'])
#
# Weather_desription.append(weather_data ['weather'][0]['id'])
# humidity = weather_data['main']['humidity']
# temp= weather_data['main']['temp']
# print('Weather is:',Weather_desription[0])
# print('Humidity is :',weather_data['main']['humidity'])
# print('Temperature is :',weather_data['main']['temp'])
# if 802 >=Weather_desription[0] >= 805:
#     if humidity >= 99:
#         print ('conditional True')
#     elif temp >=2:
#         print('temperature conditional true')
#
# if 650 >= Weather_desription[0] >= 200:
#     print ('Thunderstorm with light rain')
# if 771 >= Weather_desription[0]>= 701:
#     print('No lightning')
# if Weather_desription[0] == 781:
#     print('tornado')
# else:
#     print('false')






