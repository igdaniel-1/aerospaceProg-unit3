# Unit 3 Section 3 part 1

# Exercise 1: Obtaining JPL Horizons Data
# Objectives:
# Import the Horizons function within astroquery
# Obtain ephemerides for a comet named Eros (id = 433) relative to the sun (id = 500@10)
# Start at 2020-02-10 and end at 2022-12-31 with 1 year step
# Print out the ephemerides data

from astroquery.jplhorizons import Horizons #this is the only import needed for question 1
from skyfield.api import Star, load, wgs84 #world geodetic system (WGS84)
from skyfield.data import hipparcos
from skyfield.projections import build_stereographic_projection
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Circle
import pandas as pd

# 3552 Don Quixote (1983 SA)
# obj = Horizons(id='3552', location='568', epochs={'start':'2020-02-10', 'stop':'2022-12-31','step':'1y'})
# eph = obj.ephemerides()
# print(eph)

# comet named Eros (id = 433) relative to the sun (id = 500@10)
# obj = Horizons(id='433', location='500@10', epochs={'start':'2020-02-10', 'stop':'2022-12-31','step':'1y'})
# eph = obj.ephemerides()
# print(eph)

# ----- end of exercise one

ts = load.timescale()

# INPUT YOUR TIME SCALE BELOW
t = ts.utc(2021, 2, 26, 15, 19)
# INPUT YOUR GEOCOORDINATES BELOW
lat, long = 34.118, -118.3

# Obtaining Planet Data 
planets = load('de421.bsp')
jupiter = planets['Jupiter Barycenter']
earth = planets['Earth Barycenter']
barycentric = jupiter.at(t)

# Obtaining Star Data
with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)

observer = wgs84.latlon(latitude_degrees=lat, longitude_degrees=long).at(t)

# Position in the sky the observer will look at
position = observer.from_altaz(alt_degrees=90, az_degrees=0)

# Center the Observation
ra, dec, distance = observer.radec()
center_object = Star(ra=ra, dec=dec)

# print("ra, dec, distance:",ra, "--",dec, '--',distance)

# Find position of Jupiter relative to Earth and build a 180 deg projection
center = earth.at(t).observe(center_object)
projection = build_stereographic_projection(center)
field_of_view_degrees = 180.0

# find star positions
star_positions = earth.at(t).observe(Star.from_dataframe(stars))
stars['x'], stars['y'] = projection(star_positions)

# set graphing requirements for the visualizer
chart_size = 10
max_star_size = 100
limiting_magnitude = 10
# Create a filter that only shows stars of a specific magnitude or greater
bright_stars = (stars.magnitude <= limiting_magnitude)
magnitude = stars['magnitude'][bright_stars]
# Size of the star depends on the star size and magnitude of brightness
marker_size = max_star_size * 10 ** (magnitude / -2.5)

# plot the visualizer
fig, ax = plt.subplots(figsize=(chart_size, chart_size))
border = plt.Circle((0, 0), 1, color='black', fill=True)
ax.add_patch(border)

ax.scatter(stars['x'][bright_stars], stars['y'][bright_stars],
           s=marker_size, color='white', marker='.', linewidths=0, 
           zorder=2)


horizon = Circle((0, 0), radius=1, transform=ax.transData)
for col in ax.collections:
    col.set_clip_path(horizon)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
plt.title(f"Sky Map of Jupyter Barycenter relative to ({lat}, {long})")
plt.show()