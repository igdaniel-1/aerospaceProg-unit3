# Unit 3 Question 4 part 2

# Objectives:
# Use the CircularAperture class from photutils to conduct Aperature Photometry
# Find relevant details about the photometry including the area, center coordinates, etc
# Make a visual plot of the aperture using matplotlib

from photutils.aperture import CircularAperture, ApertureStats
# from photutils import CircularAperture, ApertureStats
import matplotlib.pyplot as plt
from photutils.datasets import make_4gaussians_image 
from matplotlib.ticker import LogLocator

# Initialize Dataset
data = make_4gaussians_image()
# Define a CircularAperture positioned at (150px, 25px) with a radius of 8px to a variable titled aperature
aperture = CircularAperture((150,25),8)
statistics = ApertureStats(data, aperture)

# visualize 
plt.figure(figsize=(8, 8))
# set color map to gray
plt.imshow(data, cmap='gray')
# set aperature marker to blue
aperture.plot(color='blue', lw=1.5) # lw is linewidth
plt.colorbar(label='Counts')
plt.title('Circular Aperture Image')
plt.show()

# Get Details about ApertureStats
print("centroid:", statistics.centroid) #coordinate of the centroid (center of mass)
print("bbox:", statistics.bbox)  #bounding box of aperature
print("sum:", statistics.sum)  #sum of the unmasked data values within the aperture
print("std:", statistics.std)  # standard deviation of the unmasked pixel values within the aperture
print("n_apertures:", statistics.n_apertures) # number of positions in the input aperture
print("median:", statistics.median)  # median of the unmasked pixel values within the aperture
print("eccentricity:", statistics.eccentricity)  # eccentricity of the 2D Gaussian function that has the same second-order moments as the source