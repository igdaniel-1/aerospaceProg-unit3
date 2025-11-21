# Unit 3 Question 4 part 3

# new dependency: specutils

# Continuum Fitting with Specutils
# Objectives:
# Create a generic Continuum Fitting using fit_generic_continuum from specutils
# Visualize the fitting using matplotlib

import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models
from astropy import units as u
# from specutils.spectra import Spectrum1D, SpectralRegion
from specutils.spectra import Spectrum, SpectralRegion
from specutils.fitting import fit_generic_continuum

# Generate Random Spectra
np.random.seed(0)
x = np.linspace(0., 10., 200)
y = 3 * np.exp(-0.5 * (x- 6.3)**2 / 0.8**2)
y += np.random.normal(0., 0.2, x.shape)
spectra = Spectrum(flux=y*u.Jy, spectral_axis=x*u.um)

# Create a Continuum Fitting
y_continuum = 3 * np.exp(-0.5 * (x - 6.3)**2 / 0.8**2)
y += y_continuum

# Create a Model Spectra using Spectrum1D
# AstropyDeprecationWarning: The Spectrum1D class is deprecated and may be removed in a future version. Use Spectrum instead.
spectra = Spectrum(flux=y*u.Jy, spectral_axis=x*u.um)
continuum_fit = fit_generic_continuum(spectra)
g1_fit = fit_generic_continuum(spectra)
y_continuum_fitted = g1_fit(x*u.um)

# visualize the spectra
# Create a subplot using matplotlib
# Plot the random spectra x, y
# Plot the continuum fitting x, y_continuum_fit
# Set the title of the plot to be "Continuum Fitting"
# Display the plot with grid settings!

fig, ax = plt.subplots()
ax.plot(x, y, color='blue')
ax.plot(x, y_continuum_fitted, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Continuum Fitting')
plt.grid(True)
plt.show()