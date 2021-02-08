import pandas as pd
import re

def dms2dd(s):
    # example: s = """0°51'56.29"S"""
    degrees, minutes, seconds, direction = re.split('[°\'"]+', s)
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction in ('S','W'):
        dd*= -1
    return dd

#df = pd.DataFrame({'CPO': {0: 'Raya', 1: 'Raya'},
# 'Latitude': {0: '0°51\'56.29"S', 1: '1°23\'39.29"S'},
# 'Longitude': {0: '101°26\'46.29"E', 1: '101°35\'30.45"E'},
# 'PKO': {0: 'X', 1: 'X'},
 #'ParentCompany': {0: 'Incasi', 1: 'Incasi'}})

#df['Latitude'] = df['Latitude'].apply(dms2dd)
#df['Longitude'] = df['Longitude'].apply(dms2dd)

#print(df)


#df2 = pd.read_csv("/home/muema/Downloads/addendum2.csv")
#nms[nms.name.notnull()]
#df3 = df2[df2.Longitude1.notnull()]
#df3['Longitude2'] = df3['Longitude1'].apply(dms2dd)
#df3['Latitude2'] = df3['Latitude1'].apply(dms2dd)

#print(df3.to_string())
#df3.to_csv("/home/muema/Downloads/addendum3.csv")

#df4 = df2[df2.Longitude1.isnull()]
#print(df4.to_string())
#df4.to_csv("/home/muema/Downloads/addendum4.csv")

# df4 = pd.read_csv("/home/muema/Downloads/addendum4.csv")
#
#
# df4['Addresses'] = df4['Village of 1st case'].fillna('') + ',' + df4['Sub County of 1st case'].fillna('') +',' + df4['County ']
# print(df4.Addresses.to_string())
# print(df4.columns)
#df['location'] = df['ADDRESS'].apply(geocode)
# df5 = pd.DataFrame()
# df5 = df4['Addresses']

from opencage.geocoder import OpenCageGeocode

# key = '7c4cedcd01d7455db554757f30d3be36'
# geocoder = OpenCageGeocode(key)
# geocoding = geocoder.geocode(no_annotations='1')
# df4['location'] = df4['Addresses'].apply(geocoding)
#query = df4['Addresses']
#result = geocoder.geocode(df4['Addresses'], no_annotations=1, language='es')
# print(df4.columns)
# print(df4.location.to_string())
import pandas as pd
import numpy as np
import sys
from opencage.geocoder import OpenCageGeocode

key = '7c4cedcd01d7455db554757f30d3be36'
geocoder = OpenCageGeocode(key)
addressfile = '/home/muema/Downloads/addresses.csv'

try:
  with open(addressfile,'r') as f:
    for line in f:
      address = line.strip()
      results = geocoder.geocode(address, no_annotations='1')

      if results and len(results):
        longitude = results[0]['geometry']['lng']
        latitude  = results[0]['geometry']['lat']
        print(u'%f;%f;%s' % (latitude, longitude, address))
        # 40.416705;-3.703582;Madrid,Spain
        # 45.466797;9.190498;Milan,Italy
        # 52.517037;13.388860;Berlin,Germany
      else:
        sys.stderr.write("not found: %s\n" % address)
except IOError:
  print('Error: File %s does not appear to exist.' % addressfile)
except RateLimitExceededError as ex:
  print(ex)
  #Your rate limit has expired. It will reset to 2500 at midnight UTC timezone
  # Upgrade on https://opencagedata.com/pricing
