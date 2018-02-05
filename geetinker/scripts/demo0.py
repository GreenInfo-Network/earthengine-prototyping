#!/bin/env python

import ee
import time


def run():
    # say a little about ourselves
    print("Hello World of Google Earth Engine API")
    print("Load the EE API and print metadata about one of their image datasets")
    print("")

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

    print("")
    print("Image info output:")
    print(output)
