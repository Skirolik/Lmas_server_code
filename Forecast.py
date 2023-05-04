import requests
from pprint import pprint
from datetime import datetime
import numpy as np
import pandas as pd

API_Key="7eb48147dc3982995adfcff0518e670d"

Weather_desription=[]
date_and_time=[]
temperature=[]


location= "Sibsagar"

lat = 12.9716
lon=77.5946


data= f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_Key}'


data= requests.get(data).json()
# pprint(data['list'])
date= data['list'][0]['dt_txt']



df_forecast= pd.DataFrame()

id=[]
date=[]
prediction_num = 0
list_prediction=[]

for num_forecasts in data['list']:
    df_forecast['prediction_num']=prediction_num
    list_prediction.append(prediction_num)
    date.append(data['list'][prediction_num]['dt_txt'])
    id.append(data['list'][prediction_num]['weather'][0]['id'])
    prediction_num +=1

df_forecast['prediction_num'] = list_prediction
df_forecast['date'] = date
df_forecast['id'] = id

# pprint(df_forecast)

df_forecast['time']=pd.to_datetime(df_forecast['date']).dt.time
print(df_forecast)

df_new=df_forecast.drop('date')
print(df_new)

# pprint(data['list'])
# for i in range(40):
#     Weather_desription.append(data['list'][i]['weather'][0]['id'])
#
# pprint(Weather_desription)
# newarr=np.array_split(Weather_desription,6)
# pprint(newarr)
# day1=newarr[0]
# print(day1)

#     for j in range(i):
#         pprint('hourly',data['daily'][i]['hourly'])
#
#
# time=data['minutely'][59]['dt']
# time1=datetime.fromtimestamp(time)

