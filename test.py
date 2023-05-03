import numpy
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import solarpy as sp
from datetime import datetime, timedelta, timezone
from pysolar import radiation, solar
from dateutil import tz

tzlocal=tz.tzoffset('IST',19800)

date_start= datetime(2023,3,8,tzinfo=tzlocal)
dates=[date_start+timedelta(minutes=i*15) for i in range(24*4)]
lat= 12.92668
lon=77.59700
altitude= [solar.get_altitude(lat,lon,d) for d in dates]
azimuth=[solar.get_azimuth(lat,lon,d ) for d in dates]
fig,axes=plt.subplots(nrows=2,figsize=(15,5))
axes[0].plot(dates,altitude)
axes[1].plot(dates,azimuth)
# axes[0].set_ylable('Altitude deg')
# axes[1].set_ylable('Azimuth (deg)')
plt.show()

rad=[radiation.get_radiation_direct(d,alt) for d,alt in zip(dates,altitude)]
print(rad)

plt.figure(figsize=(15,2.5))
plt.plot(dates,rad)
plt.ylabel('Raditaion [W/m2]')
plt.show()

# fig,ax = plt.subplots(figsize=(18,6))
#
# for h in (0,2e3,5e3,10e3):
#     t=[date+timedelta(minutes=i) for i in range(0,15*24*4,15)]
#     G=[sp.beam_irradiance(h,i,lon) for i in t]
#     ax.plot(t,G,label='h='+str(int(h))+'m')
#     myFmt = mdates.DateFormatter('%H:%M')
#     ax.xaxis.set_major_formatter(myFmt)
#
# plt.autoscale(enable=True,axis='x',tight=True)
# plt.ylim(0,1420)
# plt.xlabel('hour')
# plt.ylabel('W/m2')
# plt.title('Beam irradiance on normal plane')
# plt.legend()
# plt.grid(True)
# plt.show()