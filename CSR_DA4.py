import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split, GridSearchCV
from tqdm import tqdm
from ipywidgets import interact, interactive, fixed, interact_manual 
pr = print



path = 'module_5_auto.csv'
df = pd.read_csv(path)

df = df.select_dtypes(include = np.number) #选择数字
# pr(df.head())

def DistributionPlot(RedFunction, BlueFunction, RedName, BlueName, Title):
    width = 12
    height = 10
    plt.figure(figsize=(width,height))

    ax1 = sns.distplot(RedFunction, hist = False, color = 'r', label = RedName)
    ax2 = sns.distplot(BlueFunction, hist = False, color = 'b', label = BlueName, ax=ax1)

    plt.title(Title)
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of cars')

    plt.show()
    plt.close()

def PollyPlot(xtrain, xtest, y_train, y_test, lr, poly_transform):
    width = 12
    height = 10
    plt.figure(figsize=(width,height))

    xmax = max([xtrain.values.max(), xtest.values.max()])
    xmin = min([xtrain.values.min(), xtest.values.min()])
    x = np.arange(xmin,xmax,0.1)

    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, y_test,'go',label='Test Data')
    plt.plot(x,lr.predict(poly_transform.fit_transform(x.reshape(-1,1))), label='Predicted Function')
    plt.ylim([-10000,60000])
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    plt.close()



y_data = df['price']
x_data = df.drop('price',axis=1)
x_train, x_test, y_train, y_test = train_test_split(x_data,y_data,test_size=0.10, random_state=1)

# pr('number of test samples :',x_test.shape[0])
# pr('number of training samples:',x_train.shape[0])

x_train1, x_test1, y_train1, y_test1 = train_test_split(x_data, y_data, test_size=0.40, random_state=0)
# pr('number of test samples :',x_test1.shape[0])
# pr('number of training samples:',x_train1.shape[0])

lre = LinearRegression()
lre.fit(x_train[['horsepower']], y_train)
# pr(lre.score(x_test[['horsepower']], y_test))
# pr(lre.score(x_train[['horsepower']], y_train))

lre2 = LinearRegression()
lre2.fit(x_train1[['horsepower']],y_train1)
# pr(lre2.score(x_test1[['horsepower']],y_test1))
# pr(lre2.score(x_train1[['horsepower']],y_train1))

Rcross = cross_val_score(lre, x_data[['horsepower']], y_data, cv=4)
# pr(Rcross)
# pr("The mean of the folds are", Rcross.mean(), "and the standard deviation is" , Rcross.std())
# pr(-1*cross_val_score(lre, x_data[['horsepower']], y_data, cv=4, scoring='neg_mean_squared_error').mean()) #'neg_mean_squared_error':-1*MSE

Rcross1 = cross_val_score(lre, x_data[['horsepower']], y_data, cv=2)
# pr(Rcross1.mean())
# pr(-1*cross_val_score(lre, x_data[['horsepower']], y_data, cv=2, scoring='neg_mean_squared_error').mean())

yhat = cross_val_predict(lre,x_data[['horsepower']],y_data,cv=4)
# pr(yhat[0:5],y_data[0:5].tolist())

lr = LinearRegression()
lr.fit(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_train)
yhat_train = lr.predict(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
# pr(yhat_train[0:5])
yhat_test = lr.predict(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
# pr(yhat_test[0:5])

Title = 'Distribution  Plot of  Predicted Value Using Training Data vs Training Data Distribution'
# DistributionPlot(y_train, yhat_train,'Actual Values (Train)', 'Predicted Values (Train)', Title)

Title = 'Distribution  Plot of  Predicted Value Using Test Data vs Data Distribution of Test Data'
# DistributionPlot(y_test, yhat_test, 'Actual Values (Test)', 'Predicted Values (Test)', Title)



x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.45, random_state=0)
prr = PolynomialFeatures(degree=5)
x_train_prr = prr.fit_transform(x_train[['horsepower']])
x_test_prr = prr.fit_transform(x_test[['horsepower']])

poly = LinearRegression()
poly.fit(x_train_prr, y_train)
yhat = poly.predict(x_test_prr)
# pr(yhat[0:5],y_test[0:5].values)
# PollyPlot(x_train[['horsepower']], x_test[['horsepower']], y_train, y_test, poly,prr)
# pr(poly.score(x_train_prr,y_train))
# pr(poly.score(x_test_prr,y_test))

Rsqu_test = []
order = [1,2,3,4]
for n in order:
    prr = PolynomialFeatures(degree=n)
    x_train_prr = prr.fit_transform(x_train[['horsepower']])
    x_test_prr = prr.fit_transform(x_test[['horsepower']])
    lr.fit(x_train_prr,y_train)
    Rsqu_test.append(lr.score(x_test_prr,y_test))
# plt.plot(order,Rsqu_test)
# plt.xlabel('order')
# plt.ylabel('R^2')
# plt.title('R^2 Using Test Data')
# plt.text(3, 0.75, 'Maximum R^2 ') 
# plt.show()

def f(order,test_data):
    x_train, x_test, y_train, y_test = train_test_split(x_data,y_data,test_size=test_data,random_state=0)
    prr = PolynomialFeatures(degree=order)
    x_train_prr = prr.fit_transform(x_train[['horsepower']])
    x_test_prr = prr.fit_transform(x_test[['horsepower']])
    poly = LinearRegression()
    poly.fit(x_train_prr,y_train)
    PollyPlot(x_train[['horsepower']],x_test[['horsepower']],y_train,y_test, poly,prr)

# interact(f, order=(0,6,1),test_data = (0.05,0.95,0.05))

pr1 = PolynomialFeatures(degree=2)
x_train_pr1 = pr1.fit_transform(x_train[['horsepower', 'curb-weight', 'engine-size','highway-mpg']])
x_test_pr1 = pr1.fit_transform(x_test[['horsepower', 'curb-weight', 'engine-size','highway-mpg']])
# pr(x_train_pr1.shape)
# pr(x_test_pr1.shape)
poly1 = LinearRegression().fit(x_train_pr1,y_train)
yhat_pr1 = poly1.predict(x_test_pr1)
Title = 'Distribution  Plot of  Predicted Value Using Test Data vs Data Distribution of Test Data'
# DistributionPlot(y_test, yhat_pr1,'Actual Values (Train)', 'Predicted Values (Train)', Title)

prr = PolynomialFeatures(degree = 2)
x_train_prr = pr1.fit_transform(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])
x_test_prr = pr1.fit_transform(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])

RigeModel = Ridge(alpha=1)
RigeModel.fit(x_train_prr,y_train)
yhat = RigeModel.predict(x_test_prr)
# pr(yhat[0:4])
# pr(y_test[0:4].values)

Rsqu_test = []
Rsqu_train = []
dummy1 = []
Alpha = 10*np.array(range(0,1000))
pbar = tqdm(Alpha)

for alpha in pbar:
    RigeModel = Ridge(alpha=alpha)
    RigeModel.fit(x_train_prr,y_train)
    test_score, train_score = RigeModel.score(x_test_prr,y_test), RigeModel.score(x_train_prr,y_train)
    pbar.set_postfix({'Test Score':test_score,'Train score':train_score})
    Rsqu_test.append(test_score)
    Rsqu_train.append(train_score)

width = 12
height = 10

plt.figure(figsize=(width,height))

plt.plot(Alpha,Rsqu_test,label = 'validation data')
plt.plot(Alpha,Rsqu_train, label = 'training Data')
plt.xlabel('Alpha')
plt.ylabel('R^2')
plt.legend()
# plt.show()

ri = Ridge(alpha=10)
ri.fit(x_train_prr,y_train)
# pr(ri.score(x_test_prr,y_test))

parameters1 = [{'alpha':[0.001,0.1,1, 10, 100, 1000, 10000, 100000, 100000]}]
RR = Ridge()
Grid1 = GridSearchCV(RR, parameters1, cv=4)
Grid1.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']],y_data)
BestRR = Grid1.best_estimator_
pr(BestRR)
pr(BestRR.score(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_test))
