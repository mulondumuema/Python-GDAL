from geopy.geocoders import Nominatim
import pandas as pd
locator = Nominatim(user_agent="myGeocoder")

df = pd.read_csv("/home/muema/work2/WIR/excel_files/today.csv")
df.head()



df["ADDRESS"] = df["Sub county"] + "," + df["County where the was Diagonised"] + "," + "Kenya"

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

df.to_csv("/home/muema/work2/WIR/excel_files/today2.csv")


