from geopy.geocoders import Nominatim
import pandas as pd
locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("Champ de Mars, Paris, France")
print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
df = pd.read_csv("/home/muema/Downloads/addresses.csv")
df.head()



df["ADDRESS"] = df["Address1"] + "," + df["Address3"] + "," + df["Address4"] + "," + df["Address5"] + "," + "Sweden"

from geopy.extra.rate_limiter import RateLimiter

# 1 - conveneint function to delay between geocoding calls
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
# 2- - create location column
df['location'] = df['ADDRESS'].apply(geocode)
# 3 - create longitude, laatitude and altitude from location column (returns tuple)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
# 4 - split point column into latitude, longitude and altitude columns
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)

print(df)
print(df.to_string())

df.to_csv('/home/muema/Downloads/addresses.csv')
