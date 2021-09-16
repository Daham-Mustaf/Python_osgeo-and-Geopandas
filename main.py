# importing geopandas library:
import geopandas as gpd

# reading shape file 
shape_file = '/Users/m-store/Desktop/GeoPandas_PYTHON/Data/global_24h.shp'
sp = gpd.read_file(shape_file)
print(sp)
