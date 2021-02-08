# Import the os module
import rasterio
import pyproj
print("pyproj version is: " + pyproj.__version__)

import shapely
import shapely.speedups
print("Shapely Version is: " + shapely.__version__)
print(shapely.speedups.available)

import mapnik2
print(mapnik.mapnik_version())

# Print the current working directory
#print("Current working directory: {0}".format(os.getcwd()))