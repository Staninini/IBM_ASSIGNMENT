from cProfile import label
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pywaffle import Waffle
pr=print

text = 'Canada.xlsx'
df = pd.read_excel(
    text,
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

df.drop(['AREA','REG','DEV','Type','Coverage'],axis=1,inplace=True)
df.rename(columns = {'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace = True)
df.columns = list(map(str,df.columns))
df.set_index('Country',inplace=True)
df['Total']=df.sum(axis=1)
years = list(map(str, range(1980,2014)))
mpl.style.use('ggplot')

d1 = pd.DataFrame(df.loc[['Spain', 'Italy', 'France'],'Total'])
d1['Total'] = d1['Total']/d1['Total'].sum()*100
pr(d1)
la = d1.index.tolist()


fig = plt.figure(
    FigureClass = Waffle,
    rows = 5,
    values = d1['Total'],
    labels = la,
    legend={'loc': 'lower left'},
    colors=["#C1D82F", "#00A4E4", "#FBB034"],
    icons='star'
)
plt.show()