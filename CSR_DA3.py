import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
pr=print 

df = pd.read_csv('automobileEDA.csv')

lm = LinearRegression()
x = df[['highway-mpg']]
y = df['price']
lm.fit(x,y)
yhat = lm.predict(x)
# pr(yhat[0:5])
# pr(lm.intercept_)
# pr(lm.coef_)

# lm1 = LinearRegression()
# x = df[['engine-size']]
# y = df['price']
# lm1.fit(x,y)
# yhat = lm1.predict(x)
# pr(yhat[0:5])
# pr(lm1.intercept_)
# pr(lm1.coef_)
# pr(f'The predict price is {round(lm1.coef_[0],2)}*enginesize{round(lm1.intercept_,2)}')


z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
# lm2 = LinearRegression()
# lm2.fit(z,df['price'])
# pr(lm2.coef_)
# pr(lm2.intercept_)
# pr(f'The predict price is {round(lm2.intercept_,2)} + {round(lm2.coef_[0],2)} x horsepower + {round(lm2.coef_[1],2)} x curb_weight + {round(lm2.coef_[2],2)} x engine_size + {round(lm2.coef_[3],2)} x highway_mpg')

# z3 = df[['normalized-losses','highway-mpg']]
# lm3 = LinearRegression()
# lm3.fit(z3,df['price'])
# pr(lm3.coef_)
# pr(lm3.intercept_)
# pr(f'The predict price is {round(lm3.intercept_,2)} + {round(lm3.coef_[0],2)} x normalized_losses + {round(lm3.coef_[1],2)} x highway_mpg')

width = 12
height = 10
# plt.figure(figsize=(width,height))
# sns.regplot(x='highway-mpg',y='price',data=df)
# plt.ylim(0,)
# plt.show()

# plt.figure(figsize=(width,height))
# sns.regplot(x='peak-rpm',y='price',data=df)
# plt.ylim(0,)
# plt.show()

# pr(df[['peak-rpm','highway-mpg','price']].corr())

# plt.figure(figsize=(width,height))
# sns.residplot(df['highway-mpg'],df['price'])
# plt.show()

#????????????????????????????????????????????????????????????????????????????????????????
# Y_hat = lm.predict(z)
# plt.figure(figsize=(width,height))
# ax1 = sns.distplot(df['price'],hist=False,color='r',label='Actual Value')
# sns.distplot(Y_hat, hist=False,color='b',label='Fitted Values',ax=ax1)
# plt.title('Actual vs Fitted Values for Price')
# plt.xlabel('Price (in dollars)')
# plt.ylabel('Proportion of Cars')
# plt.show()
# plt.close()
#????????????????????????????????????????????????????????????????????????????????????????

#非线性回归模型！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()
#非线性回归模型！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

x = df['highway-mpg']
y = df['price']
f = np.polyfit(x,y,3)
p = np.poly1d(f)
# pr(p)
# PlotPolly(p, x, y, 'highway-mpg')

from sklearn.preprocessing import PolynomialFeatures
pi=PolynomialFeatures(degree=2)
# pr(pi)
z_pi=pi.fit_transform(z)
# pr(z.shape)
# pr(z_pi.shape)

a = np.array([[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]])
a=a.reshape(-1,1)
pr(a)