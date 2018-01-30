#!/bin/env python
"""
the Hello World of Google Earth Engine API
Load the EE API and print metadata abnout one of their image datasets
"""

import ee


# initialize the Earth Engine object, using the authentication credentials.
ee.Initialize()

# print the information for an image asset
image = ee.Image('srtm90_v4')
print(image.getInfo())

