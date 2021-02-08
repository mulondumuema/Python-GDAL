from osgeo import gdal
srcFile = gdal.Open("Example_raster.tif")
band = srcFile.GetRasterBand(1)
import struct
fmt = "<" + ("h" * band.XSize)
for row in range(band.YSize):
 scanline = band.ReadRaster(0, row, band.XSize, 1,
                            band.XSize, 1,
                            band.DataType)
 row_data = struct.unpack(fmt, scanline)
 print(row_data)

 values = band.ReadAsArray()
 for row in range(band.XSize):
     print(values[row])