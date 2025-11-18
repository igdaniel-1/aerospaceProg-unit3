# Unit 3 Question 1 part 1
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename

# style
plt.style.use(astropy_mpl_style)

# data
image_file = get_pkg_data_filename('./M6707HH.fits')
# print("\nimage file:", image_file)
image_data = fits.getdata(image_file, ext=0)

# read data
with fits.open('./M6707HH.fits') as hdul:
    hdul.info()
    print("\nHEADER:",hdul[0].header)

print("\nSHAPE:",image_data.shape)

# display
plt.figure()
plt.imshow(image_data)
plt.colorbar()

