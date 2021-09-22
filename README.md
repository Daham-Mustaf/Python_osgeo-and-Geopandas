# Python_Geopandas
# Table of contents
1. [GeoPandas Introduction:](#introduction)
- [Unlocking the shapefile osgeo.ogr:](#un)
- [Read shape file:](#read)
- [pgRouting Installing in the database](#ex)
- [Upgrading the database:](#up)
3. [Step One](#one)


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
simple program that reads the features out of a shapefile.

```bash
cd /usr/ports/databases/pgRouting
```
```bash
make install clean
```
or package:
```bash
pkg install pgrouting
```
Homebrew
```bash
brew install pgrouting
```
git

To download the repository
```bash
git clone git://github.com/pgRouting/pgrouting.git
cd pgrouting
git checkout v3.1.3
```

### Installing the pgRouting extension<a name="ex"></a>
Many distributions of PostGIS are equipped with pgRouting already. Execute the following SQL to check whether you have pgRouting onboard:
```j
   select pgr_version();
   ```   
Once you have the binaries set up, enable the extension by executing the following:
createdb routing
```j
psql routing -c 'CREATE EXTENSION PostGIS'
psql routing -c 'CREATE EXTENSION pgRouting'
  ```
  or
```j
    CREATE EXTENSION pgrouting;
   ```
   At this stage, we should be ready to continue with pgRouting.
   
 ### Upgrading the database: <a name="up"></a>
   Upgrading:
  ```j 
   ALTER EXTENSION pgrouting UPDATE TO "2.2.3";
  ```
    
## Step One:<a name="one"></a>

Requirments 
1- PostgresSql
2- Postgis
3- Pgrouting
 ```j
 SELECT PostGIS_Version();
			
     ```
   ```shel   
postgres -V >postgresVersion.txt
psql -V

cd pgrouting
git checkout v3.1.3
  ```

