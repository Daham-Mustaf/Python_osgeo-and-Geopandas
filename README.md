# Python_Geopandas
# Table of contents
1. [GeoPandas Introduction:](#introduction)
- [Unlocking the shapefile osgeo.ogr:](#un)
- [Reading shape file:](#read)
- [Writing shape file:](#write)



## GeoPandas Introduction <a name="introduction"></a>
GeoPandas is an open source project to make working with geospatial data in python easier. GeoPandas extends the datatypes used by pandas to allow spatial operations on geometric types. Geometric operations are performed by shapely. Geopandas further depends on fiona for file access and matplotlib for plotting.
for more information see [GeoPandas](https://geopandas.org/)

### Unlocking the shapefile osgeo.ogr: <a name="un"></a>
At last, we are ready to start working with some geospatial data. Open up a command line or terminal
chek the layer details of shape file as follow:
```shel
OgrInfo -al global_24h.shp
``` 
```python
# We're going to start by loading the OGR library we installed earlier:
import osgeo.ogr

# We next want to open the shapefile using OGR:
shapefile = osgeo.ogr.Open("/Users/m-store/Desktop/GeoPandas_PYTHON/Data/global_24h.shp")

# shapefile has only a single layer. we need to extract the (one and only)
# layer from the shapefile:
layer = shapefile.GetLayer(0)

# Let's iterate through the various features within the shapefile
feature = ''
for i in range(layer.GetFeatureCount()):
     # To get a Feature to the feature's geometry object
    feature = layer.GetFeature(i)
    # Let's extract latitude
    latitude = feature.GetField("latitude")
    # To get a reference to the feature's geometry object
    geometry = feature.GetGeometryRef()
    # what type of geometry
    geometry_type = geometry.GetGeometryName()
    print(i, latitude, geometry_type)


```

### Reading shape files: <a name="read"></a>
Geopandas can read almost any vector-based spatial data format including ESRI shapefile, GeoJSON files and more using the command:

```python
# importing geopandas library:
import geopandas as gpd

# reading shape file
shape_file_path = '/Users/m-store/Desktop/GeoPandas_PYTHON/Data/global_24h.shp'
sp_data = gpd.read_file(shape_file_path)
print(sp_data)
```
load data from 
```python
# importing geopandas library:
import geopandas as gpd

# Returns path of a particular mapGeoPandas also implements alternate
# constructors that can read any data  format recognized by fiona.
# To read a zip file containing an ESRI shapefile with the borough boundaries
# of New York City (GeoPandas includes this as an example dataset):

sp_data = gpd.read_file(gpd.datasets.get_path('nybb'))
sp_data.set_index('BoroCode', inplace=True)
print(sp_data.head())
# Plots
sp_data.plot()

```
### Reading shape files: <a name="write"></a>
Writing vector data: Writing geospatial data to a vector-format file is almost as simple as reading it. There are, however, a couple of extra steps you have to take.
```python
# We're going to start by loading the OGR library we installed earlier:
from osgeo import ogr
from osgeo import osr

driver = ogr.GetDriverByName("ESRI Shapefile")
# creat a directory
dstFile = driver.CreateDataSource("/Users/m-store/Desktop/GeoPandas_PYTHON/Data/test-shapefile")
# create a spatial reference object that defines how the coordinates in the dataset should be interpreted:
spatialReference = osr.SpatialReference()
spatialReference.SetWellKnownGeogCS("WGS84")
# add a layer to the destination file to hold the layer's data:
layer = dstFile.CreateLayer("layer", spatialReference)
# The next step is to define the various attributes that the destination file
# will store for each feature. Let's define a field called NAME:
field = ogr.FieldDefn("NAME", ogr.OFTString)
field.setWidth(100)
layer.CreateField(field)

wkt = "POLYGON((23.4 38.9, 23.5 38.9, 23.5 38.8, 23.4 38.9))"
# create the OGR Feature object that will represent the feature,
# and set the geometry and attributes as desired:
polygon = ogr.CreateGeometryFromWkt(wkt)
feature = ogr.Feature(layer.GetLayerDefn())
feature.SetGeometry(polygon)

feature.SetField("NAME", "My Polygon")
# add the feature to the layer:
layer.CreateFeature(feature)
feature.Destroy()
dstFile.Destroy()
# This closes the destination file and makes sure that everything has been saved to disk.
```
