import pyproj
UTM_X = 565718.523517
UTM_Y = 3980998.9244
srcProj = pyproj.Proj(proj="utm", zone="11",
                      ellps="clrk66", units="m")
dstProj = pyproj.Proj(proj='longlat', ellps='WGS84',
                      datum='WGS84')
long,lat = pyproj.transform(srcProj, dstProj, UTM_X, UTM_Y)
print("UTM zone 17 coordinate " + "X and Y " +
      "({:.4f}, {:.4f}) ".format(UTM_X, UTM_Y) + "long and lat "
      "= {:.4f}, {:.4f}".format(long, lat))

angle = 315 # 315 degrees = northeast.
distance = 10000

geod = pyproj.Geod(ellps='clrk66')
long2,lat2,invAngle = geod.fwd(long, lat, angle, distance)
print("{:.4f}, {:.4f}".format(lat2, long2) +
      " is 10km northeast of " +
      "{:.4f}, {:.4f}".format(lat, long))