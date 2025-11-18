# Unit 3 Question 1 part 1
# Visualizing a FITS File using Astropy and Matplotlib
# Objectives:
# Read the M6707HH.fits file using Astropy
# Print out header information for the Primary HDU
# Print the dimensions of the FITS Image
# Visualize the FITS file


from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename

# style
plt.style.use(astropy_mpl_style)

# read data
with fits.open('./M6707HH.fits') as hdul:
    hdul.info()
    print("\nHEADER:",hdul[0].header)


# data
image_file = get_pkg_data_filename('./M6707HH.fits')
# print("\nimage file:", image_file)
image_data = fits.getdata(image_file, ext=0)
print("\nSHAPE:",image_data.shape)

# display
plt.figure()
plt.imshow(image_data)
plt.colorbar()

plt.show()
