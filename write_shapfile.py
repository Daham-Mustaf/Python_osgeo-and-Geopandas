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
