# Unit 3 Question 4 part 3

# new dependency: specutils

# Continuum Fitting with Specutils
# Objectives:
# Create a generic Continuum Fitting using fit_generic_continuum from specutils
# Visualize the fitting using matplotlib

import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models
from specutils.spectra import Spectrum1D, SpectralRegion
from specutils.fitting import fit_generic_continuum

print('hey hey girl')