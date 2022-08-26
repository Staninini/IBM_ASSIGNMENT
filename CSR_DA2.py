import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from spicy import stats
pr = print 

df = pd.read_csv('automobileEDA.csv')
    
# pr(df.head())
# pr(df['peak-rpm'].dtype)
# pr(df.corr()) ############################ df.corr() 查看int/float数据之间的相关性 #############################
# pr(df[['bore', 'stroke', 'compression-ratio','horsepower']].corr())



# sns.regplot(x='engine-size',y='price',data = df)
# plt.ylim(0,)
# plt.show()
# pr(df[["engine-size", "price"]].corr())

# sns.regplot(x='highway-mpg',y='price',data=df)
# plt.show()
# pr(df[['highway-mpg','price']].corr())

# sns.regplot(x='peak-rpm',y='price',data=df)
# plt.show()
# pr(df[['peak-rpm','price']].corr())

# pr(df[['stroke','price']].corr())
# sns.regplot(x='stroke',y='price',data=df)
# plt.show()



# sns.boxplot(x='body-style', y='price', data=df)
# plt.show()

# sns.boxplot(x='engine-location',y='price',data=df)
# plt.show()

# sns.boxplot(x='drive-wheels',y='price',data=df)
# plt.show()

# pr(df.describe())
# pr(df.describe(include=['object']))



# drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
# drive_wheels_counts.rename(columns = {'drive-wheels':'value_counts'},inplace=True)
# drive_wheels_counts.index.name = 'drive-wheels'
# pr(drive_wheels_counts)

# engine_location_counts = df['engine-location'].value_counts().to_frame()
# engine_location_counts.rename(columns={'engine-location':'counts'},inplace=True)
# engine_location_counts.index.name = 'engine-location'
# pr(engine_location_counts)



names = df['drive-wheels'].unique()
group_1 = df[['drive-wheels','price']]
group_1 = group_1.groupby(['drive-wheels'],as_index = False).mean()
# pr(group_1)

group_2 = df[['drive-wheels','body-style','price']]
group_2_mean = group_2.groupby(['drive-wheels','body-style'],as_index = False).mean()
# pr(group_2)

group_pivot = group_2_mean.pivot(index = 'drive-wheels',columns='body-style')
group_pivot = group_pivot.fillna(0)

# plt.pcolor(group_pivot,cmap='RdBu')
# plt.colorbar()
# plt.show()

# fig, ax = plt.subplots()
# im = ax.pcolor(group_pivot,cmap='RdBu')
# row_labels = group_pivot.columns.levels[1]
# col_labels = group_pivot.index
# ax.set_xticks(np.arange(group_pivot.shape[1])+0.5,minor=False)
# ax.set_yticks(np.arange(group_pivot.shape[0])+0.5,minor=False)
# ax.set_xticklabels(row_labels, minor=False)
# ax.set_yticklabels(col_labels, minor=False)
# plt.xticks(rotation=90)
# fig.colorbar(im)
# plt.show()

# group_3 = df[['body-style','price']]
# group_3_mean = group_3.groupby(['body-style'],as_index = False).mean()
# pr(group_3_mean)



p_coef,p_value = stats.pearsonr(df['wheel-base'],df['price'])
# pr(p_coef,p_value)

p_coef,p_value = stats.pearsonr(df['horsepower'],df['price'])
# pr(p_coef,p_value)

p_coef,p_value = stats.pearsonr(df['length'],df['price'])
# pr(p_coef,p_value)

p_coef,p_value = stats.pearsonr(df['width'],df['price'])
# pr(p_coef,p_value)

p_coef,p_value = stats.pearsonr(df['highway-mpg'],df['price'])
# pr(p_coef,p_value)


group_test = df[['drive-wheels','price']].groupby(['drive-wheels'])
# pr(group_test)
# pr(group_test.get_group('4wd')['price'])
# f_val,p_val = stats.f_oneway(group_test.get_group('fwd')['price'],group_test.get_group('rwd')['price'],group_test.get_group('4wd')['price'])
# pr('f=' , f_val, 'p=', p_val)

f_val,p_val = stats.f_oneway(group_test.get_group('fwd')['price'],group_test.get_group('rwd')['price'])
pr('fwd and rwd: f=' , f_val, 'p=', p_val)

f_val,p_val = stats.f_oneway(group_test.get_group('fwd')['price'],group_test.get_group('4wd')['price'])
pr('fwd and 4wd: f=' , f_val, 'p=', p_val)

f_val,p_val = stats.f_oneway(group_test.get_group('rwd')['price'],group_test.get_group('4wd')['price'])
pr('rwd and 4wd: f=' , f_val, 'p=', p_val)