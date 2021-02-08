angle = 315 # 315 degrees = northeast.
distance = 10000

geod = pyproj.Geod(ellps='clrk66')
long2,lat2,invAngle = geod.fwd(long, lat, angle, distance)
print("{:.4f}, {:.4f}".format(lat2, long2) +
      " is 10km northeast of " +
      "{:.4f}, {:.4f}".format(lat, long))