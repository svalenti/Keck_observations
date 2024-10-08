
import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, get_sun, get_moon, SkyCoord
from astropy.coordinates import Angle
import astropy.units as u

# Example target coordinates (RA and Dec)
SN2024pxl = SkyCoord(ra="17:32:27.35", dec="07:03:44.8", unit=(u.hourangle, u.deg))
SN2024seh = SkyCoord(ra="21:55:50.90", dec="-03:05:23.2", unit=(u.hourangle, u.deg))
SN2024kgi = SkyCoord(ra="22:44:43.99", dec="16:05:07.0", unit=(u.hourangle, u.deg))
SN2024ryv = SkyCoord(ra="00:25:29.99", dec="20:14:34.9", unit=(u.hourangle, u.deg))
SN2024any = SkyCoord(ra="03:08:57.83", dec="-02:56:45.9", unit=(u.hourangle, u.deg))

# Set the observing location 
location = EarthLocation(lat=37.3414*u.deg, lon=-121.6429*u.deg, height=1283*u.m)

# Define the time range 
start_time_24pxl = Time('2024-09-09 03:52:17.562', scale='utc')
exposure_24pxl   = (4*1200)/3600
start_time_24seh = Time('2024-09-09 05:27:02.562', scale='utc')
exposure_24seh   = (4*1200)/3600
start_time_24kgi = Time('2024-09-09 07:01:47.562', scale='utc')
exposure_24kgi   = (3*1200)/3600
start_time_24ryv = Time('2024-09-09 08:13:17.562', scale='utc')
exposure_24ryv   = (5*1200)/3600
start_time_24any = Time('2024-09-09 10:11:17.562', scale='utc')
exposure_24any   = (6*1200)/3600



# Calculate for 1.5 hours after the start time (with one-minute intervals)
times_24pxl = start_time_24pxl + np.linspace(0, exposure_24pxl, 300)*u.hour  # 300 points, every minute over exposure time
times_24seh = start_time_24seh + np.linspace(0, exposure_24seh, 300)*u.hour
times_24kgi = start_time_24kgi + np.linspace(0, exposure_24kgi, 300)*u.hour
times_24ryv = start_time_24ryv + np.linspace(0, exposure_24ryv, 300)*u.hour 
times_24any = start_time_24any + np.linspace(0, exposure_24any, 300)*u.hour


# Calculate Local Sidereal Time (LST)
lst_24pxl = times_24pxl.sidereal_time('apparent', longitude=location.lon)
lst_24seh = times_24seh.sidereal_time('apparent', longitude=location.lon)
lst_24kgi = times_24kgi.sidereal_time('apparent', longitude=location.lon)
lst_24ryv = times_24ryv.sidereal_time('apparent', longitude=location.lon)
lst_24any = times_24any.sidereal_time('apparent', longitude=location.lon)

# print("24pxl")
# print(lst_24pxl)
# print(" ")
# print(" ")
# print("24seh")
# print(lst_24pxl)
#=


# # Calculate Hour Angle (HA = LST - RA)
ha_24pxl = (lst_24pxl - SN2024pxl.ra)#.wrap_at(360*u.deg)
ha_24seh = (lst_24seh - SN2024seh.ra)#.wrap_at(360*u.deg)
ha_24kgi = (lst_24kgi - SN2024kgi.ra)#.wrap_at(360*u.deg)
ha_24ryv = (lst_24ryv - SN2024ryv.ra)
ha_24any = (lst_24any - SN2024any.ra)

#print(ha_24ryv)

# print("24pxl")
# print(SN2024pxl.ra)
# print(ha_24pxl)
# print(" ")
# print(" ")
# print("24seh")
# #print(SN2024seh.ra)
#print(ha_24ryv)

ha_24ryv_mod = []
for i in ha_24ryv.hour:
	if i > 20:
		ha_24ryv_mod.append(i-24)
	else:
		ha_24ryv_mod.append(i)


print(ha_24ryv_mod)

# # Plotting the Hour Angle for 5 hours
# plt.figure(figsize=(10,6))
plt.plot(times_24pxl.datetime, ha_24pxl.hour, label='SN 2024pxl HA')
plt.plot(times_24seh.datetime, ha_24seh.hour, label='SN 2024seh HA')
plt.plot(times_24kgi.datetime, ha_24kgi.hour, label='SN 2024kgi HA')
plt.plot(times_24ryv.datetime, ha_24ryv_mod, label='SN 2024ryv HA')
plt.plot(times_24any.datetime, ha_24any.hour, label='SN 2024any HA')
plt.axhline(3.75, color='k', linestyle='--', label='New HA Limit')
plt.xlabel('Time (UTC)')
plt.ylabel('Hour Angle [hours]')
plt.title('Hour Angle Evolution 09-09-24 (Lick Observatory)')
#plt.hlines(3.75, )
plt.ylim(-6,6)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
