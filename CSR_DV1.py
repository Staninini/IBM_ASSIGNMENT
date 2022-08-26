import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
pr=print

text = 'Canada.xlsx'
df = pd.read_excel(
    text,
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

# pr(df.head())
# pr(df.tail())
# pr(df.info(verbose=False))
# pr(df.columns)
# pr(df.index)
# pr(type(df.columns.tolist()))
# pr(type(df.index.tolist()))
# pr(df.shape)

df.drop(['AREA','REG','DEV','Type','Coverage'],axis=1,inplace=True)
df.rename(columns = {'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace = True)
df['Total']=df.sum(axis=1)
# pr(df.isnull().sum())
# pr(df.describe())
# pr(df.head())
# pr(df.Country)
# pr(df[['Country', 1980, 1981, 1982, 1983, 1984, 1985]])

df.set_index('Country',inplace=True)
df.index.name = None 

# pr(df.loc['China'])
# pr(df.iloc[87])
# pr(df[df.index=='China'])
# pr(df.loc['China',2013])
# pr(df.iloc[87,36])
# pr(df.loc['Japan',[1980, 1981, 1982, 1983, 1984, 1984]])

df.columns = list(map(str,df.columns))
years = list(map(str,range(1980,2014)))
# pr(years)

# c = df['Continent'] == 'Asia'
# pr(df[c])
# pr(df[(df['Continent'] == 'Asia') & (df['Region'] == 'Southern Asia')])
# pr(df.shape,df.columns,df.head(2))

mpl.style.use(['ggplot'])

haiti = df.loc['Haiti',years]
haiti.index = haiti.index.map(int)
# haiti.plot(kind='line')
# plt.title('Immigration from Haiti')
# plt.ylabel('Number of immigrants')
# plt.xlabel('Years')
# plt.text(2000,6000,'2010 Earthquake')
# plt.show()

# mpl.style.use(['ggplot'])
# df1 = df.loc[['India','China'], years]
# df1 = df1.transpose()
# df1.plot(kind='line')
# plt.title('Immigration from India and China')
# plt.ylabel('Number of immigrants')
# plt.xlabel('Years')
# plt.legend()
# plt.show()

# country = df['Total'].sort_values()[-5:].index.tolist()
# data = df.loc[['Pakistan','Philippines','United Kingdom of Great Britain and Northern Ireland','China','India'],years]
df.sort_values(by = 'Total', ascending=False,axis=0,inplace=True)
data = df.head(5)[years]
data = data.transpose()
data.index = data.index.map(int)
mpl.style.use('ggplot')
# data.plot(kind='line',stacked=False,
#              figsize=(20, 10))
# plt.title('Immigration from top 5 countries')
# plt.ylabel('Number of immigrants')
# plt.xlabel('Years')
# plt.legend()
# plt.show()