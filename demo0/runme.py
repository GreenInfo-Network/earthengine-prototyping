#!/bin/env python
"""
the Hello World of Google Earth Engine API
Load the EE API and print metadata abnout one of their image datasets
"""

import ee
import time


# initialize the Earth Engine object, using the authentication credentials.
t0 = time.time()
ee.Initialize()
t1 = time.time()
print("Initialize: {0:.1f} seconds".format(t1 - t0))

# print the information for an image asset
t0 = time.time()
image = ee.Image('srtm90_v4')
output = image.getInfo()
t1 = time.time()
print("image.getInfo: {0:.1f} seconds".format(t1 - t0))

print("Image info output:")
print(output)
