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

df.drop(['AREA','REG','DEV','Type','Coverage'],axis=1,inplace=True)
df.rename(columns = {'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace = True)
df['Total']=df.sum(axis=1)
df.set_index('Country',inplace=True)
df.index.name = None 
df.columns = list(map(str,df.columns))
years = list(map(str,range(1980,2014)))

mpl.style.use(['ggplot'])




# country = df['Total'].sort_values()[-5:].index.tolist()
# data = df.loc[['Pakistan','Philippines','United Kingdom of Great Britain and Northern Ireland','China','India'],years]
df.sort_values(by = 'Total', ascending=False,axis=0,inplace=True)
data = df.head(5)[years]
data = data.transpose()
data.index = data.index.map(int)
mpl.style.use('ggplot')
# data.plot(kind='area',stacked=False,
#              figsize=(20, 10))
# plt.title('Immigration from top 5 countries')
# plt.ylabel('Number of immigrants')
# plt.xlabel('Years')
# plt.legend()
# plt.show()

# count, bin_edges = np.histogram(df['2013'])
# df['2013'].plot.hist(figsize=(8,5),xticks=bin_edges)
# plt.title('Histogram of Immigration from 195 Countries in 2013')
# plt.ylabel('Number of Countries')
# plt.xlabel('Number of Immigrants')
# plt.show()


d = df.loc[['Denmark','Norway','Sweden'],years]
d = d.transpose()
count,bin_edges = np.histogram(d,15)
# d.plot(kind = 'hist', figsize=(10,6), bins =15, alpha = 0.6, xticks = bin_edges, color = ['coral', 'darkslateblue', 'mediumseagreen'])
# plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
# plt.ylabel('Number of Years')
# plt.xlabel('Number of Immigrants')
# plt.legend()
# plt.show()
# xmin = bin_edges[0]
# xmax = bin_edges[-1]
# d.plot(kind = 'hist',figsize = (10,6), bins = 15, xticks = bin_edges, color = ['coral', 'darkslateblue', 'mediumseagreen'],stacked=True,xlim=(xmin,xmax))
# plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
# plt.ylabel('Number of Years')
# plt.xlabel('Number of Immigrants') 
# plt.legend()
# plt.show()

d2 = df.loc[['Greece','Albania','Bulgaria'],years].transpose()
x,y = np.histogram(d2,15)
# d2.plot(kind='hist',figsize=(10,6),bins=15,xticks=y,alpha=0.35)
# plt.title('Histogram of Immigration from Greece, Albania and Bulgaria from 1980 - 2013')
# plt.ylabel('Number of Years')
# plt.xlabel('Number of Immigrants') 
# plt.legend()
# plt.show()

d3 = df.loc['Iceland',years]
# d3.plot(kind='bar',figsize=(10,6),rot=45)
# plt.xlabel('Year') # add to x-label to the plot
# plt.ylabel('Number of immigrants') # add y-label to the plot
# plt.title('Icelandic immigrants to Canada from 1980 to 2013') # add title to the plot
# plt.annotate('', xy=(32,70),xytext=(28,20),xycoords='data',
# arrowprops=dict(arrowstyle='->',connectionstyle='arc3',color='blue',lw=2)
# )
# plt.annotate('2008 - 2011 Financial Crisis',xy=(28,30),rotation=72.5,va='bottom',ha='left')
# plt.show()

df.sort_values(by='Total',axis=0,ascending=False,inplace=True)
d4 = df.head(15)
d4 = d4['Total'][::-1]
# d4.plot(kind='barh',figsize=(10,10),color='steelblue')
# for x,y in enumerate(d4):
#     label = format(int(y),',')                                   #########在数字里自动增加千位分隔符
#     plt.annotate(label,xy=(y-60000,x-0.1),color='white')
# plt.xlabel('Year')
# plt.ylabel('Number of immigrants')
# plt.title('Immigrants to Canada from 1980 to 2013 from top 15 countries')
# plt.show()

d5 = df.groupby('Continent',axis=0).sum()
d5 = d5['Total'].sort_values(ascending=False)
color_list = ['lightskyblue', 'yellowgreen', 'lightcoral', 'gold', 'lightgreen', 'pink']
explode_list = [0,0,0,0.1,0.1,0.1]
# d5.plot(kind='pie',figsize=(15,6),autopct='%1.f%%',startangle=90,shadow=False,
# labels=None,pctdistance=1.12,colors=color_list,explode=explode_list)
# plt.title('Immigration to Canada by Continent [1980 - 2013]',y=1.12)
# plt.axis('equal')
# plt.legend(labels=df.index,loc='upper left')
# plt.show()

d6 = df.groupby('Continent',axis=0).sum()
d6 = d6['2013'].sort_values(ascending=False)
explode_list = [0,0,0,0,0.1,0.2]
color_list = ['lightskyblue', 'yellowgreen', 'lightcoral', 'gold', 'lightgreen', 'pink']
# d6.plot(kind='pie',figsize=(15,6),labels=None,autopct='%1.1f%%',pctdistance=1.13,
# colors=color_list,startangle=90,explode=explode_list)
# plt.title('Immigration to Canada by Continent in 2013',y=1.05)
# plt.legend(labels=d6.index,loc='upper left')
# plt.axis('equal')
# plt.show()

# fig = plt.figure()
# ax1 = fig.add_subplot(1,2,1)
# ax2 = fig.add_subplot(1,2,2)

d7 = df.loc[['China','India'], years].transpose()
# d7.plot(kind='box',figsize=(15,5), vert = False, color = 'blue', ax=ax2)
# ax2.set_title('Box plot of Chinese and Indian Immigrants from 1980 - 2013')
# ax2.set_xlabel('Number of Immigrants')
# ax2.set_ylabel('Countries')

# d7.plot(kind='line',figsize = (15,5),ax=ax1)
# ax1.set_title('Line plot of Chinese and Indian Immigrants from 1980 - 2013')
# ax1.set_xlabel('Years')
# ax1.set_ylabel('Number of Immigrants')
# plt.show()


d8 = df.sort_values(by='Total',ascending=False,axis=0).head(15)
years80 = list(map(str,range(1980,1990)))
years90 = list(map(str,range(1990,2000)))
years00 = list(map(str,range(2000,2010)))

df80 = d8.loc[:,years80].sum(axis=1)
df90 = d8.loc[:,years90].sum(axis=1)
df00 = d8.loc[:,years00].sum(axis=1)

d8 = pd.DataFrame({'1980s':df80,'1990s':df90,'2000s':df00})

# d8.plot(kind='box',figsize=(10,6))
# d8 = d8.reset_index()
# pr(d8[d8['2000s']>209611.5])
# plt.title('Immigration from top 15 countries for decades 80s, 90s and 2000s')
# plt.show()

d9 = pd.DataFrame(df[years].sum(axis=0))
d9.index = list(map(int,d9.index))
d9.reset_index(inplace=True)
d9.columns=['year','total']

# d9.plot(kind='scatter',x='year',y='total',figsize=(10,6),color='darkblue')
x = d9['year']
y = d9['total']
fit = np.polyfit(x,y,deg=1)

# plt.xlabel('Year')
# plt.ylabel('Number of Immigrants')
# plt.title('Total Immigration to Canada from 1980 - 2013')
# plt.plot(x, fit[0]*x+fit[1])
# plt.annotate(f'y = {int(fit[0])}x - {-int(fit[1])}', xy=(2000, 150000))
# plt.show()



d10 = pd.DataFrame(df.loc[['Denmark','Norway','Sweden'],years].sum(axis=0))
d10.index = list(map(int,d10.index))
d10.reset_index(inplace=True)
d10.columns = ['year','total']
# d10.plot(kind='scatter',x='year',y='total',color='darkblue',figsize=(10,6))

x = d10['year']
y = d10['total']
fit = np.polyfit(x,y,deg=1)

# plt.plot(x, fit[0]*x+fit[1])
# plt.annotate(f'y = {int(fit[0])}x + {int(fit[1])}',xy=(1985,450))
# plt.xlabel('Year')
# plt.ylabel('Number of Immigrants')
# plt.title('Immigration from Denmark, Norway and Sweden to Canada from 1980 - 2013')
# plt.show()

