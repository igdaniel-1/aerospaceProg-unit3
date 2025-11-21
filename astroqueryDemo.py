# Unit 3 question 5 part 1

from astroquery.esasky import ESASky
import astropy.units as u
from astroquery.esa.jwst import Jwst
from astropy.coordinates import SkyCoord

# --------- Demo:
# catalog_list = ESASky.list_catalogs()
# map_list = ESASky.list_maps()
# print(map_list)

# region_maps = ESASky.query_region_maps(position="M51", radius=10 * u.arcmin, missions="all")
# print(region_maps)

# spectra = ESASky.get_spectra(position="Gaia DR3 4512810408088819712", radius="6.52 arcmin",
#                              missions=['Herschel', 'XMM-NEWTON'])
# print(spectra)

# ----------- Exercise:
# Gather data from the ESA JWST Archive
# Print out the status of JWST TAP
# Jwst.get_status_messages()

# Query the following region using SkyCoord with Astropy with the details:
# ra = 44, dec = -10, unit = (u.degree, u.degree), frame = 'icrs'

# obtain maps for a specified region using query_region_maps
# icrs_region_map = SkyCoord(ra=44, dec=-10, unit=(u.degree, u.degree), frame='icrs')
# print(icrs_region_map)


coord = SkyCoord(ra=53, dec=-27, unit=(u.degree, u.degree), frame='icrs')
width = u.Quantity(5, u.deg)
height = u.Quantity(5, u.deg)
result = Jwst.query_region(coordinate=coord, width=width, height=height)
print(result)

# print data products for the Observation ID jw01043010001_02101_00013_mirimage
product_list = Jwst.get_product_list(observation_id='jw01063107001_02101_00013_nrca3')
print(product_list)