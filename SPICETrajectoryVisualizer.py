# Unit 3 Question 2 part 1

# Cassini Positioning Visualization made with SpiceyPy
# Ephemeris Data: positions and velocities of celestial bodies


import math
import numpy as np
import matplotlib.pyplot as plt
import spiceypy as spice

# Print out the toolkit version
print(spice.tkvrsn("TOOLKIT"))
# load spice kernel into program
spice.furnsh("./kernels/cassMetaK.txt")

# convert dates into Emphemeris Time
step = 4000
utc = ['Jun 20, 2004', 'Dec 1, 2005']
etOne = spice.str2et(utc[0])
etTwo = spice.str2et(utc[1])
# print("Ephemeris Time One: {}, Ephemeris Time Two: {}".format(etOne, etTwo))

# Calculate time range
times = [x*(etTwo-etOne)/step + etOne for x in range(step)]

# Running spkpos
positions, lightTimes = spice.spkpos('Cassini', times, 'J2000', 'NONE', 'SATURN BARYCENTER')

# positions is a list, make it an ndarray for easier indexing
fig = plt.figure(figsize=(9, 9))
positions = np.asarray(positions).T 

# z axis
ax  = fig.add_subplot(111, projection='3d')

# plot the calculated values for positioning within a 3D graph
ax.plot(positions[0], positions[1], positions[2])
plt.title('Cassini Positioning Visualization made with SpiceyPy')
plt.show()






# clear the kernel 
spice.kclear()


# './kernels/020514_SE_SAT105.bsp', is having issues loading