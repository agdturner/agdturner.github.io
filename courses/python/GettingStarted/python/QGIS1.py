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
It is an example showing how to use Python Console in QGIS.
It was written for a tutorial to support student learning.
It requires some OS Open Greenspace data unzipped and in GeoPackage format.
The users is to use a file dialog to select the input data file.
The layers in the GeoPackage are loaded into QGIS for display.
The attributes and geometry for one of the layers in the GeoPackage are 
processed, and a text summary is output to the console. As the processing steps
are done some other information is also written out. This was used as the code
was incrementally developed to understand what is returned from functions 
called, and how data attributes and values are named so that selections of 
these could be specified in the processing.

The code was developed, run and tested on QGIS Version 3.22. To run it:
    1. Download OS Open Greenspace data in GeoPackage format from:
       https://osdatahub.os.uk/downloads/open/OpenGreenspace
    2. Extract the zip file into a directory
    3. Open QGIS
    4. Open the Python Console:
       From the menu choose Plugins > Python Console
    5. Use the Show Editor Button to open the editor pane of the Python 
       Console
    6. Use the OpenScript... Button to open this script.
    7. Use the Run Script button to run the script.
    8. Select the opgrsp_gb.gpkg GeoPackage format data extracted from the zip 
       file.
   
Users should expect:
    1. The GeoPackage data layers to get loaded into QGIS.
    2. The following should be printed to the console:
<QGIS1>
A QFileDialog should appear. Please select the opgrsp_gb.gpkg File
<Load layers>
layer_names ['AccessPoint', 'GreenspaceSite']
vlayers {'AccessPoint': <QgsVectorLayer: 'AccessPoint' (ogr)>, 
         'GreenspaceSite': <QgsVectorLayer: 'GreenspaceSite' (ogr)>}
</Load layers>
CRS set to <QgsCoordinateReferenceSystem: EPSG:27700>
gs_layer <QgsVectorLayer: 'GreenspaceSite' (ogr)>
<gs_layer.fields()>
fid Integer64
id String
function String
distinctiveName1 String
distinctiveName2 String
distinctiveName3 String
distinctiveName4 String
</gs_layer.fields()>
There are 149900 features in <QgsVectorLayer: 'GreenspaceSite' (ogr)>
There are 3016 features with the function Golf Course
The area of all the features with the function Golf Course is 
1244186735.2820458
The largest area of a Golf Course is 3113897.6925000283
The bounding box extent of which is: <QgsRectangle: 345852.09999999997671694 
680903.13000000000465661, 348457.76000000000931323 683178.09999999997671694>
The feature id of which is 13444
</QGIS1>
    3. In the message window of QGIS the following warning is issued when the
       QFileDialog is used:
           ResourceWarning: unclosed file 
       This is expected behaviour and the warning can be ignored.
       
Sources consulted in developing this code:
1. https://qgis.org/pyqgis/3.22/
2. https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook
"""
# The following are all import statement detailing from which packages specifc
# modules are imported.
from PyQt5.QtWidgets import QFileDialog
from osgeo import ogr
from qgis.core import (
    QgsProject,
    QgsCoordinateReferenceSystem,
    QgsFeatureRequest,
    QgsVectorLayer
)
# The following import statements have been commented out rather than deleted
# as earlier versions of this code attempted to use these modules and commented
# code in this would need these imports and so they persist for educational
# reasons and completeness.
#from qgis.gui import QgsMapCanvas
#from qgis.utils import iface

# A message to the user to indicate that the program is running.
print("<QGIS1>")

# Load data
# Get path to opgrsp_gpkg_gb/OS Greenspace (GPKG) GB/data/opgrsp_gb.gpkg file
fd = QFileDialog()
title = 'Please select the opgrsp_gb.gpkg File'
print("A QFileDialog should appear.", title)
path = "" # This can be used to start the QFileDialog in a particular directory
gpkg_file = QFileDialog.getOpenFileName(fd, title, path)
#print("gpkg_file", gpkg_file)
gpkg = gpkg_file[0]
#print("gpkg", gpkg)
# Load in the layers
print("<Load layers>")
layer_names = [] # A list for storing the names of the layers in the GeoPackage
vlayers = {} # A dictionary for the virtual layers stored with keys as names
for i in ogr.Open(gpkg): # Iterate over the items in the GeoPackage
    name = i.GetName()
    # Assume all items are layers!
    layer_names.append(name)
    vl = vlayer = QgsVectorLayer(gpkg + "|layername=" + name, name, 'ogr')
    # Add the virtual layer to the dictionary using name as the key
    vlayers[name] = vl
    # The following commented out code was used to add the layers to the 
    # QGIS interface in a single step. Due to the size of the layer, drawing
    # it is slow, so a virtual layer is used now instead.
    #iface.addVectorLayer(gpkg + "|layername=" + layer_name, layer_name, 'ogr')
print("layer_names", layer_names)
print("vlayers", vlayers)
print("</Load layers>")

# Set gs_layer to be GreenspaceSite MultiPolygon layer
gs_layer = vlayers.get("GreenspaceSite")
# Print the crs of the gs_layer
crs = gs_layer.crs()
#print("crs", crs)
# Set the CRS for the project
# "EPSG:27700" is the standard Well Known Text (WKT) code for the UK British
# National Grid Projection.
QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(crs))
# NB. CoordinateReferenceSystem information about the layers can probably be 
# read from the GeoPackage.
# A message to the user to indicate that the CRS has been set
print("CRS set to", crs)
#gs_layers = QgsProject().instance().mapLayersByName('GreenspaceSite')
#print("gs_layers", gs_layers)
#gs_layer = gs_layers[0]
print("gs_layer", gs_layer)

# Print the attributes/fields of gs_layer
# When loaded as a map layer and not a virtual layer the following commented 
# print statements worked, but attributes are known as fields and are accessed
# differently with virtual layers.
#print("gs_layer.attributes()", gs_layer.attributes())
#print("gs_layer.attributeAliases()", gs_layer.attributeAliases())
print("<gs_layer.fields()>")
for field in gs_layer.fields():
    print(field.name(), field.typeName())
print("</gs_layer.fields()>")

# Iterate over the features and calculate the number of features.
n = 0
for f in gs_layer.getFeatures():
    n = n + 1
print("There are", n, "features in", gs_layer)

# Explore features with the attribute/field function = "Golf Course"
function = "Golf Course"
# Calculate the number of features, area and maximum area
n = 0
area = 0
max_f_area = 0
max_f_area_gc = None
for f in gs_layer.getFeatures():
   if f['function'] == function:
        n = n + 1
        f_area = f.geometry().area()
        area = area + f_area
        if f_area > max_f_area:
            max_f_area = f_area
            max_f_area_gc = f
print("There are", n, "features with the function", function)
print("The area of all the features with the function", function, "is", area)
print("The largest area of a", function, "is", max_f_area)
extent = max_f_area_gc.geometry().boundingBox()
print("The bounding box extent of which is:", extent)
max_f_area_gc_id = max_f_area_gc.id()
print("The feature id of which is", max_f_area_gc_id)

# Set the MapCanvas extent to extent and add gs_layer as a MapLayer 
# The following commented out code is from attempting to set the extent before 
# and after loading the entire gs_layer, but this did not always work!
#QgsMapCanvas().setExtent(extent)
#QgsMapCanvas().refresh()
#iface.mapCanvas().setExtent(extent)
#iface.mapCanvas().refresh()
#print("<addMapLayer>")
#QgsProject.instance().addMapLayer(gs_layer)
#print("</addMapLayer>")
#QgsMapCanvas().setExtent(extent)
#QgsMapCanvas().refresh()
#iface.mapCanvas().setExtent(extent)
#iface.mapCanvas().refresh()
# As a workaround a selection from the gs_layer was materialized and added.
selected_gs_layer = gs_layer.materialize(QgsFeatureRequest().setFilterFids(
    [max_f_area_gc_id]))
QgsProject.instance().addMapLayer(selected_gs_layer)
print("</QGIS1>")


