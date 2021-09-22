# importing geopandas library:
import geopandas as gpd

# reading shape file
shape_file_path = '/Users/m-store/Desktop/GeoPandas_PYTHON/Data/global_24h.shp'
sp_data = gpd.read_file(shape_file_path)
print(sp_data)