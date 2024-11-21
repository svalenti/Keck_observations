
import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, get_sun, get_moon, SkyCoord
from astropy.coordinates import Angle
import astropy.units as u


# Example target coordinates (RA and Dec)
# SN2024pxl = SkyCoord(ra="17:32:27.35", dec="07:03:44.8", unit=(u.hourangle, u.deg))
# SN2024seh = SkyCoord(ra="21:55:50.90", dec="-03:05:23.2", unit=(u.hourangle, u.deg))
# SN2024kgi = SkyCoord(ra="22:44:43.99", dec="16:05:07.0", unit=(u.hourangle, u.deg))
SN2024ryv = SkyCoord(ra="00:25:29.99", dec="20:14:34.9", unit=(u.hourangle, u.deg))
# SN2024any = SkyCoord(ra="03:08:57.83", dec="-02:56:45.9", unit=(u.hourangle, u.deg))
# SN2024mpq = SkyCoord(ra="22:30:41.08", dec="+39:17:30.20", unit=(u.hourangle, u.deg))
# SN2024kgi = SkyCoord(ra="22:44:43.99", dec="16:05:07.0", unit=(u.hourangle, u.deg))
SN2024rmj = SkyCoord(ra="01:07:52.74", dec="+03:30:40.27", unit=(u.hourangle, u.deg))
# SN2024ugc = SkyCoord(ra="02:45:17.36", dec="+35:18:20.0", unit=(u.hourangle, u.deg))
# SN2024ueo = SkyCoord(ra="03:44:01.35", dec="-05:36:22.35", unit=(u.hourangle, u.deg))
SN2024xal = SkyCoord(ra="03:08:57.83", dec="-14:21:44.40", unit=(u.hourangle, u.deg))
SN2024wal = SkyCoord(ra="02:42:59.46", dec="+11:57:28.28", unit=(u.hourangle, u.deg))
SN2024gvz = SkyCoord(ra="06:07:51.73", dec="-24:53:52.7", unit=(u.hourangle, u.deg))
SN2024inv = SkyCoord(ra="11:06:32.16", dec="+11:22:42.6", unit=(u.hourangle, u.deg))


# Set the observing location 
location = EarthLocation(lat=37.3414*u.deg, lon=-121.6429*u.deg, height=1283*u.m)

# Define the time range 
start_time_24ryv = Time('2024-11-23 02:22:42.548', scale='utc')
exposure_24ryv   = (6*1200)/3600
start_time_24rmj = Time('2024-11-23 04:43:57.548', scale='utc')
exposure_24rmj   = (5*1200)/3600
start_time_24xal = Time('2024-11-23 06:41:57.548', scale='utc')
exposure_24xal   = (3*900)/3600
start_time_24gvz = Time('2024-11-23 08:49:57.548', scale='utc')
exposure_24gvz   = (6*1200)/3600
start_time_24inv = Time('2024-11-23 11:11:12.548', scale='utc')
exposure_24inv   = (5*1200)/3600


# Calculate for 1.5 hours after the start time (with one-minute intervals)
times_24ryv = start_time_24ryv + np.linspace(0, exposure_24ryv, 300)*u.hour  # 300 points, every minute over exposure time
times_24rmj = start_time_24rmj + np.linspace(0, exposure_24rmj, 300)*u.hour 
times_24xal = start_time_24xal + np.linspace(0, exposure_24xal, 300)*u.hour
times_24gvz = start_time_24gvz + np.linspace(0, exposure_24gvz, 300)*u.hour
times_24inv = start_time_24inv + np.linspace(0, exposure_24inv, 300)*u.hour

# Calculate Local Sidereal Time (LST)
lst_24ryv = times_24ryv.sidereal_time('apparent', longitude=location.lon)
lst_24rmj = times_24rmj.sidereal_time('apparent', longitude=location.lon)
lst_24xal = times_24xal.sidereal_time('apparent', longitude=location.lon)
lst_24gvz = times_24gvz.sidereal_time('apparent', longitude=location.lon)
lst_24inv = times_24inv.sidereal_time('apparent', longitude=location.lon)


# print("24pxl")
# print(lst_24pxl)
# print(" ")
# print(" ")
# print("24seh")
# print(lst_24pxl)
#=


# # Calculate Hour Angle (HA = LST - RA)
ha_24ryv = (lst_24ryv - SN2024ryv.ra)#.wrap_at(360*u.deg)
ha_24rmj = (lst_24rmj - SN2024rmj.ra)
ha_24xal = (lst_24xal - SN2024xal.ra)
ha_24gvz = (lst_24gvz - SN2024gvz.ra)
ha_24inv = (lst_24inv - SN2024inv.ra)


#print(ha_24ryv)

# print("24pxl")
# print(SN2024pxl.ra)
# print(ha_24pxl)
# print(" ")
# print(" ")
# print("24seh")
# #print(SN2024seh.ra)
#print(ha_24ryv)

ha_24rmj_mod = []
for i in ha_24rmj.hour:
	if i > 20:
		ha_24rmj_mod.append(i-24)
	else:
		ha_24rmj_mod.append(i)


ha_24ryv_mod = []
for i in ha_24ryv.hour:
	if i > 20:
		ha_24ryv_mod.append(i-24)
	else:
		ha_24ryv_mod.append(i)
        
# print(ha_24ryv_mod)


# # Plotting the Hour Angle for 5 hours
plt.figure(figsize=(9,6))
plt.plot(times_24ryv.datetime, ha_24ryv_mod, label='SN 2024ryv HA')
plt.plot(times_24rmj.datetime, ha_24rmj_mod,  label='SN 2024rmj HA')
plt.plot(times_24xal.datetime, ha_24xal.hour, label='SN 2024xal HA')
plt.plot(times_24gvz.datetime, ha_24gvz.hour, label='SN 2024gvz HA')
plt.plot(times_24inv.datetime, ha_24inv.hour, label='SN 2024inv HA')

plt.axhline(3.75, color='k', linestyle='--', label='New West HA Limit')
plt.axhline(-5.67, color='k', linestyle='--', label='East HA Limit')

plt.xlabel('Time (UTC)')
plt.ylabel('Hour Angle [hours]')
plt.title('Hour Angle Evolution 11-23-24 (UTC) at Lick Observatory')
#plt.hlines(3.75, )
plt.ylim(-6,6)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
