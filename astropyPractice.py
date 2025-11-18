# Unit 3 Question 1 part 1
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename


plt.style.use(astropy_mpl_style)

image_file = get_pkg_data_filename('./M13.fits')
image_data = fits.getdata(image_file, ext=0)

print(image_data.shape)



# with fits.open('./M13.fits') as hdul:
#     hdul.info()
#     print(hdul[0].header)