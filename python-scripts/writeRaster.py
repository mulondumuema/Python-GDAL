from osgeo import gdal
driver = gdal.GetDriverByName("GTIFF")
dstFile = driver.Create("Example_raster.tif", 360,180,1, gdal.GDT_Int16)

#set the projection
from gdal import osr
spatialReference = osr.SpatialReference()
spatialReference.SetWellKnownGeogCS("WGS84")
dstFile.SetProjection(spatialReference.ExportToWkt())

#set the georeferencing transform
originX = -180
originY = 90
cellWidth = 1.0
cellHeight = 1.0

dstFile.SetGeoTransform([originX, cellWidth, 0,
                         originY, 0, -cellHeight])

band = dstFile.GetRasterBand(1)

import random
values = []
for row in range(180):
 row_data = []
 for col in range(360):
     row_data.append(random.randint(1, 100))
 values.append(row_data)


import numpy
array = numpy.array(values, dtype=numpy.int16)
band.WriteArray(array)