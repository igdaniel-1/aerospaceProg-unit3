# Unit 3 Section 3 part 1

# Exercise 1: Obtaining JPL Horizons Data
# Objectives:
# Import the Horizons function within astroquery
# Obtain ephemerides for a comet named Eros (id = 433) relative to the sun (id = 500@10)
# Start at 2020-02-10 and end at 2022-12-31 with 1 year step
# Print out the ephemerides data

from astroquery.jplhorizons import Horizons
from skyfield.api import Star, load, wgs84
from skyfield.data import hipparcos
from skyfield.projections import build_stereographic_projection
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Circle

# 3552 Don Quixote (1983 SA)
# obj = Horizons(id='3552', location='568', epochs={'start':'2020-02-10', 'stop':'2022-12-31','step':'1y'})
# eph = obj.ephemerides()
# print(eph)

# comet named Eros (id = 433) relative to the sun (id = 500@10)
obj = Horizons(id='433', location='500@10', epochs={'start':'2020-02-10', 'stop':'2022-12-31','step':'1y'})
eph = obj.ephemerides()
print(eph)