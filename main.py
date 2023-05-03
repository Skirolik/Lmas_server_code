import requests
from pprint import pprint

API_Key="6a02a1fcb5602a735bddbe33439fcaf0"

Weather_desription=[]
date_and_time=[]
temperature=[]


location= "Sibsagar"

lat = 36.2137
lon=-88.6125

weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid="

final_url= weather_url+API_Key

weather_data= requests.get(final_url).json()
pprint(weather_data )
pprint(weather_data ['weather'][0]['description'])
pprint(weather_data ['weather'][0]['id'])

Weather_desription.append(weather_data ['weather'][0]['id'])
humidity = weather_data['main']['humidity']
temp= weather_data['main']['temp']
print('Weather is:',Weather_desription[0])
print('Humidity is :',weather_data['main']['humidity'])
print('Temperature is :',weather_data['main']['temp'])
if 802 >=Weather_desription[0] >= 805:
    if humidity >= 99:
        print ('conditional True')
    elif temp >=2:
        print('temperature conditional true')

if 650 >= Weather_desription[0] >= 200:
    print ('Thunderstorm with light rain')
if 771 >= Weather_desription[0]>= 701:
    print('No lightning')
if Weather_desription[0] == 781:
    print('tornado')
else:
    print('false')


# for d in weather_data['list']:
#     a=d['weather'][0]['description']
#     temperature.append(d['main']['temp'])
#     Weather_desription.append(a)
#
#     date_and_time.append(d['dt_txt'])
#     pprint((d['wind']))
#     pprint(d['weather'])
#     pprint(d['main'])
#     pprint(d['dt_txt'])
# # pprint(Weather_desription)
# # pprint(date_and_time)
# # # pprint(temperature)
