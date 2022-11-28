# -*- coding: utf-8 -*-
"""
 * Copyright 2022 Centre for Computational Geography.
 *
 * Licensed under the Apache License, Version 2.0 (the"License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an"AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * Created on Fri Nov 25 23:40:03 2022
 @version: 1.0
 @author: Andy Turner

This program is to be executed in the QGIS Python environment.
It is an example showing how to use Python Console in QGIS written for a tutorial/practical.
It processes some OS Open Greenspace data and prints out some statistics about features.

It has been tested on QGIS Version 3.22. To run it:
1. Download OS Open Greenspace data in GeoPackage format from https://osdatahub.os.uk/downloads/open/OpenGreenspace
2. Unzip the file into a directory
3. Open QGIS
4. Open the Python Console: From the menu choose Plugins > Python Console
5. Use the OpenScript... button to open this script.
6. Use the Run Script button to run the script.
7. Select the geopackage data.
8. Watch what happens:
    The data should get loaded into QGIS.
    The features in the GreenspaceSite MultiPolygon layer are gone through in 3 ways.
    The Console Output should be something like the following:
There are 149900 features
There are 3016 features with the function Golf Course
The area of all the features with the function Golf Course is 1244186735.2820458 
    For details look at the code.

"""
from PyQt5.QtWidgets import QFileDialog
from osgeo import ogr

# Load data
# Get path to opgrsp_gpkg_gb/OS Greenspace (GPKG) GB/data/opgrsp_gb.gpkg file
fd = QFileDialog()
title = 'Open File'
path = ""
gpkg = QFileDialog.getOpenFileName(fd, title, path)[0]
#gpkg = 'C:/Users/geoagdt/Downloads/opgrsp_gpkg_gb/OS Open Greenspace (GPKG) GB/data/opgrsp_gb.gpkg'
#print(gpkg)
# Load in the layers
for layer in ogr.Open(gpkg):
    layer_name = layer.GetName()
    #print(layer_name)
    iface.addVectorLayer(gpkg + "|layername=" + layer_name, layer_name, 'ogr')
# AccessPoint
# GreenspaceSite

# Set layer to be GreenspaceSite MultiPolygon layer
layer = QgsProject().instance().mapLayersByName('GreenspaceSite')[0]
# Print the attributes in the active layer
#print(layer.attributeAliases())
# {'distinctiveName1': '', 'distinctiveName2': '', 'distinctiveName3': '', 'distinctiveName4': '', 'fid': '', 'function': '', 'id': ''}

# Loop through the features and calculate the number of all features
n = 0
for f in layer.getFeatures():
    n = n + 1
print("There are", n, "features")

# Look at features with the function "Golf Course"
function = "Golf Course"
# Calculate the number of features
n = 0
for f in layer.getFeatures():
    if f['function'] == function:
        n = n + 1
print("There are", n, "features with the function", function)
# Calculate the total area of Golf Course features
area = 0
for f in layer.getFeatures():
     if f['function'] == function:
        n = n + 1
        area = area + f.geometry().area()
print("The area of all the features with the function", function, "is", area)
