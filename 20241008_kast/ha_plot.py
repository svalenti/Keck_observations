
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
# SN2024ryv = SkyCoord(ra="00:25:29.99", dec="20:14:34.9", unit=(u.hourangle, u.deg))
# SN2024any = SkyCoord(ra="03:08:57.83", dec="-02:56:45.9", unit=(u.hourangle, u.deg))
SN2024mpq = SkyCoord(ra="22:30:41.08", dec="+39:17:30.20", unit=(u.hourangle, u.deg))
SN2024kgi = SkyCoord(ra="22:44:43.99", dec="16:05:07.0", unit=(u.hourangle, u.deg))
SN2024rmj = SkyCoord(ra="01:07:52.74", dec="+03:30:40.27", unit=(u.hourangle, u.deg))
SN2024ugc = SkyCoord(ra="02:45:17.36", dec="+35:18:20.0", unit=(u.hourangle, u.deg))
SN2024ueo = SkyCoord(ra="03:44:01.35", dec="-05:36:22.35", unit=(u.hourangle, u.deg))
SN2024xal = SkyCoord(ra="03:08:57.83", dec="-14:21:44.40", unit=(u.hourangle, u.deg))
SN2024wal = SkyCoord(ra="02:42:59.46", dec="+11:57:28.28", unit=(u.hourangle, u.deg))




# Set the observing location 
location = EarthLocation(lat=37.3414*u.deg, lon=-121.6429*u.deg, height=1283*u.m)

# Define the time range 
start_time_24mpq = Time('2024-10-09 03:04:59.500', scale='utc')
exposure_24mpq   = (2*900)/3600
start_time_24kgi = Time('2024-10-09 03:43:14.500', scale='utc')
exposure_24kgi   = (4*1200)/3600
start_time_24rmj = Time('2024-10-09 05:17:59.500', scale='utc')
exposure_24rmj   = (4*1200)/3600
start_time_24ugc = Time('2024-10-09 06:52:44.562', scale='utc')
exposure_24ugc   = (4*1200)/3600
start_time_24ueo = Time('2024-10-09 08:27:29.500', scale='utc')
exposure_24ueo   = (4*1200)/3600
start_time_24xal = Time('2024-10-09 10:02:14.500', scale='utc')
exposure_24xal   = (3*600)/3600
start_time_24wal = Time('2024-10-09 10:43:44.500', scale='utc')
exposure_24wal   = (5*1200)/3600


# Calculate for 1.5 hours after the start time (with one-minute intervals)
times_24mpq = start_time_24mpq + np.linspace(0, exposure_24mpq, 300)*u.hour  # 300 points, every minute over exposure time
times_24kgi = start_time_24kgi + np.linspace(0, exposure_24kgi, 300)*u.hour
times_24rmj = start_time_24rmj + np.linspace(0, exposure_24rmj, 300)*u.hour 
times_24ugc = start_time_24ugc + np.linspace(0, exposure_24ugc, 300)*u.hour
times_24ueo = start_time_24ueo + np.linspace(0, exposure_24ueo, 300)*u.hour
times_24xal = start_time_24xal + np.linspace(0, exposure_24xal, 300)*u.hour
times_24wal = start_time_24wal + np.linspace(0, exposure_24wal, 300)*u.hour


# Calculate Local Sidereal Time (LST)
lst_24mpq = times_24mpq.sidereal_time('apparent', longitude=location.lon)
lst_24kgi = times_24kgi.sidereal_time('apparent', longitude=location.lon)
lst_24rmj = times_24rmj.sidereal_time('apparent', longitude=location.lon)
lst_24ugc = times_24ugc.sidereal_time('apparent', longitude=location.lon)
lst_24ueo = times_24ueo.sidereal_time('apparent', longitude=location.lon)
lst_24xal = times_24xal.sidereal_time('apparent', longitude=location.lon)
lst_24wal = times_24wal.sidereal_time('apparent', longitude=location.lon)

# print("24pxl")
# print(lst_24pxl)
# print(" ")
# print(" ")
# print("24seh")
# print(lst_24pxl)
#=


# # Calculate Hour Angle (HA = LST - RA)
ha_24mpq = (lst_24mpq - SN2024mpq.ra)#.wrap_at(360*u.deg)
ha_24kgi = (lst_24kgi - SN2024kgi.ra)#.wrap_at(360*u.deg)
ha_24rmj = (lst_24rmj - SN2024rmj.ra)
ha_24ugc = (lst_24ugc - SN2024ugc.ra)
ha_24ueo = (lst_24ueo - SN2024ueo.ra)
ha_24xal = (lst_24xal - SN2024xal.ra)
ha_24wal = (lst_24wal - SN2024wal.ra)


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


ha_24ugc_mod = []
for i in ha_24ugc.hour:
	if i > 20:
		ha_24ugc_mod.append(i-24)
	else:
		ha_24ugc_mod.append(i)

print(ha_24ugc.hour)


# # Plotting the Hour Angle for 5 hours
# plt.figure(figsize=(10,6))
plt.plot(times_24mpq.datetime, ha_24mpq.hour, label='SN 2024mpq HA')
plt.plot(times_24kgi.datetime, ha_24kgi.hour, label='SN 2024kgi HA')
plt.plot(times_24rmj.datetime, ha_24rmj_mod, label='SN 2024rmj HA')
plt.plot(times_24ugc.datetime, ha_24ugc_mod, label='SN 2024ugc HA')
plt.plot(times_24ueo.datetime, ha_24ueo.hour, label='SN 2024ueo HA')
plt.plot(times_24xal.datetime, ha_24xal.hour, label='SN 2024xal HA')
plt.plot(times_24wal.datetime, ha_24wal.hour, label='SN 2024wal HA')

plt.axhline(3.75, color='k', linestyle='--', label='New HA Limit')

plt.xlabel('Time (UTC)')
plt.ylabel('Hour Angle [hours]')
plt.title('Hour Angle Evolution 10-09-24 (UTC) at Lick Observatory')
#plt.hlines(3.75, )
plt.ylim(-6,6)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
