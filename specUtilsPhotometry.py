# Unit 3 question 4 part 1
# new dependencies: photutils


from astropy.io import fits
import astropy.units as u
from astropy.nddata import CCDData
from astropy.stats import sigma_clipped_stats, SigmaClip
from astropy.visualization import ImageNormalize, LogStretch
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator
import numpy as np
from photutils.background import Background2D, MeanBackground

# Retrieves the FITS file we will be using for our example
url = 'https://archive.stsci.edu/pub/hlsp/xdf/hlsp_xdf_hst_acswfc-60mas_hudf_f435w_v1_sci.fits'
with fits.open(url) as hdulist:
    hdulist.info()
    data = hdulist[0].data
    header = hdulist[0].header