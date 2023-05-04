import requests
from pprint import pprint
from datetime import datetime

API_Key="7eb48147dc3982995adfcff0518e670d"

Weather_desription=[]
date_and_time=[]
temperature=[]
weather_id=[]

lat = 8.0883
lon=77.5385

weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid="

final_url= weather_url+API_Key

weather_data= requests.get(final_url).json()


time=weather_data['dt']
time1=datetime.fromtimestamp(time)
print(time1)
#
# Weather_desription.append(weather_data ['weather'][0]['id'])
Weather_desription.append(803)
humidity = weather_data['main']['humidity']
temp= weather_data['main']['temp']
print('Weather is:',Weather_desription[0])

if  Weather_desription[0] == 804:
    print('true')


elif 650 >= Weather_desription[0] >= 200:
    print ('Thunderstorm with light rain')
elif 771 >= Weather_desription[0]>= 701:
    print('No lightning')
elif Weather_desription[0] == 781:
    print('tornado')
elif Weather_desription[0] == 800:
    print('false')

##if the predicion is 803 ie bbroken clouds: 51-84% check next hour prediction to see if the condition changes
##if condition changes from broken to overcast or rain then hoot else not

elif Weather_desription[0] == 803:
    data = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={API_Key}'

    data = requests.get(data).json()
    pprint(data['hourly'][1]['weather'][0]['id'])
    weather_id.append(data ['hourly'][1]['weather'][0]['id'])

    if weather_id[0] == 804:
        print('true')
    elif 650 >= weather_id[0] >= 200:
        print('Thunderstorm with light rain')
    elif 771 >= weather_id[0] >= 701:
        print('No lightning')
    elif weather_id[0] == 781:
        print('tornado')
    elif weather_id[0] == 800:
        print('false')
    else:
        print('false')

else:
    print('false')

