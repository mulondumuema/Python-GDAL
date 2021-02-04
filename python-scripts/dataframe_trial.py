# import Pandas as pd
import pandas as pd
# create a new data frame
df = pd.DataFrame({'Last': ['Smith', 'Nadal', 'Federer'],
                   'First': ['Steve', 'Joe', 'Roger'],
                 'Age':[32,34,36]})

df['Name'] = df['First'].str.cat(df['Last'],sep=" ")
df
df["Name2"] = df["First"] + " " + df["Last"]
print(df)