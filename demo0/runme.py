LAYERS = [
    'bagp_assembly',
    'bagp_bpadfee',
    'bagp_cities',
    'bagp_senate',
    'bagp_easement',
]


# Import the Earth Engine Python Package
import ee

# Initialize the Earth Engine object, using the authentication credentials.
ee.Initialize()

# Print the information for an image asset.
image = ee.Image('srtm90_v4')
print(image.getInfo())

