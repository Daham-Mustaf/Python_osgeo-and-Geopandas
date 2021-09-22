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


