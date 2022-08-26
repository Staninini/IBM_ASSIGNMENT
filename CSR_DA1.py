import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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

# pr(df.info())
# missingdata = df.isnull()
# # print(missingdata.head())
# # l = missingdata.columns.values.tolist()


# for i in missingdata.columns:
#     print(i)
#     print(missingdata[i].value_counts())
#     print(' ')

avg_norm_loss = int(df['normalized-losses'].astype('float').mean(axis=0))
df['normalized-losses'].replace(np.nan,avg_norm_loss,inplace=True)

avg_bore = round(df['bore'].astype('float').mean(axis=0),2)
# pr(avg_bore)
df['bore'].replace(np.nan,avg_bore,inplace=True)
# pr(df['bore'])

avg_stroke = round(df['stroke'].astype('float').mean(axis=0),2)
df['stroke'].replace(np.nan,avg_stroke,inplace=True)

# pr(df['num-of-doors'].value_counts())
# pr(df['num-of-doors'].value_counts().idxmax())
df['num-of-doors'].replace(np.nan,'four',inplace=True)

df.dropna(subset=['price'],axis=0,inplace=True)
df.reset_index(drop=True,inplace=True)

# pr(df.dtypes)
df[['bore','stroke']] = df[['bore','stroke']].astype('float')
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
# pr(df.dtypes)


df["city-mpg"] = round(235/df["city-mpg"],2)
df.rename(columns={'city-mpg':'city-L/100km'},inplace=True)

df['highway-mpg'] = round(235/df['highway-mpg'],2)
df.rename(columns={'highway-mpg':'highway-L/100km'},inplace=True)

df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()

df['height'] = df['height']/df['height'].max()
# pr(df[['length','width','height']].head())

df['horsepower'] = df['horsepower'].astype('float')
bins = np.linspace(min(df['horsepower']),max(df['horsepower']),4)
names = ['low','midium','high']
df['horsepower_binned'] = pd.cut(df['horsepower'],bins,labels=names,include_lowest=True)
# pr(df[['horsepower','horsepower_binned']])
# pr(df['horsepower_binned'].value_counts())

# plt.bar(names, df['horsepower_binned'].value_counts())
# plt.xlabel('horsepower')
# plt.ylabel('count')
# plt.title('horsepower bins')
# plt.show()

# plt.hist(df['horsepower'],bins=3)
# plt.xlabel('horsepower')
# plt.ylabel('count')
# plt.title('horsepower bins')
# plt.show()


# plt.hist(df['highway-L/100km'],bins=3)
# plt.xlabel('highway-L/100km')
# plt.ylabel('count')
# plt.title('highway-L/100km bins')
# plt.show()

highway_bins = np.linspace(min(df['highway-L/100km']),max(df['highway-L/100km']),4)
df['highway_bins'] = pd.cut(df['highway-L/100km'],highway_bins,labels = names,include_lowest=True)

# plt.bar(names,df['highway_bins'].value_counts())
# plt.xlabel('highway-L/100km')
# plt.ylabel('counts')
# plt.title('highway-L/100km')
# plt.show()

dummy_variable_1 = pd.get_dummies(df['fuel-type'])
# pr(dummy_variable_1.head())
dummy_variable_1.rename(columns={'diesel':'fuel type:diesel','gas':'fuel type: gas'},inplace=True)
df = pd.concat([df,dummy_variable_1],axis=1)
df.drop(['fuel-type','horsepower_binned','highway_bins'],axis=1,inplace=True)
# pr(df.head())

dummy_variable_2 = pd.get_dummies(df['aspiration'])
dummy_variable_2.rename(columns={'std':'aspiration:std','turbo':'aspiration:turbo'},inplace=True)
df = pd.concat([df,dummy_variable_2],axis=1)
df.drop(['aspiration'],axis=1,inplace=True)
# pr(df.head())

df.to_csv('clean_df.csv')