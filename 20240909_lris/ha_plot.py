
import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, get_sun, get_moon, SkyCoord
from astropy.coordinates import Angle
import astropy.units as u

# Example target coordinates (RA and Dec)
SN2024pxl = SkyCoord(ra="17:32:27.35", dec="07:03:44.8", unit=(u.hourangle, u.deg))

# Set the observing location 
location = EarthLocation(lat=37.3414*u.deg, lon=-121.6429*u.deg, height=1283*u.m)

# Define the time range (e.g., over one day, with one-minute intervals)
start_time_24pxl = Time('2024-09-09 03:50:00', scale='utc')
end_time_24pxl = Time('2024-09-09 05:20:00', scale='utc')


# Calculate for 1.5 hours after the start time (with one-minute intervals)
times = start_time_24pxl + np.linspace(0, 1.5, 300)*u.hour  # 300 points, every minute over 1.5 hours

# Calculate Local Sidereal Time (LST)
lst = times.sidereal_time('apparent', longitude=location.lon)

# Calculate Hour Angle (HA = LST - RA)
ha = (lst - SN2024pxl.ra).wrap_at(360*u.deg)

# Plotting the Hour Angle for 5 hours
plt.figure(figsize=(10,6))
plt.plot(times.datetime, ha.hour, label='SN 2024pxl HA')
plt.axhline(3.75, color='k', linestyle='--', label='New HA Limit')
plt.xlabel('Time (UTC)')
plt.ylabel('Hour Angle [hours]')
plt.title('Hour Angle of SN 2024pxl 09-09-24 (Lick Observatory)')
#plt.hlines(3.75, )
plt.ylim(1,5)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
