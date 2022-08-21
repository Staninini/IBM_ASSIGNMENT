import pandas as pd
import numpy as np
pr = print

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(path, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers

df1 = df.replace('?',np.NaN)
df = df1.dropna(subset=['price'],axis=0)

df.to_csv('carprice.csv', index = False)
# pr(df.dtypes)
# pr(df.describe())
# pr(df.describe(include='all'))

# pr(df[['length', 'compression-ratio']])
# pr(df[['length', 'compression-ratio']].describe())

pr(df.info())