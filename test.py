import requests
from pprint import pprint
from datetime import datetime

API_Key="7eb48147dc3982995adfcff0518e670d"

Weather_desription=[]
date_and_time=[]
temperature=[]


location= "Sibsagar"

lat = 12.9716
lon=77.5946


data= f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={API_Key}'

data= requests.get(data).json()
pprint(data ['daily'])
time=data['minutely'][59]['dt']
time1=datetime.fromtimestamp(time)
#
# print(time1)

