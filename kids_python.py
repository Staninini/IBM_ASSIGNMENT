import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pr=print
# data1 = pd.DataFrame({
#     'subject_id':['1','2','3'],
#     'first_name':['Alex','Amy','Allen'],
#     'last_name':['Anderson','Ackerman','Ali']})

# data2 = pd.DataFrame({
#     'subject_id':['1','2','3','4','5'],
#     'test_id':[50,51,52,53,54]})

# data3 = pd.DataFrame({
#     'subject_id':['2','3','4','5'],
#     'first_name':['Billy','Brian','Bran','Bryce']})

# # new1 = pd.merge(data2,data3)
# # new2 = pd.merge(data1,data3,on = 'subject_id')          #注意写法是.merge(a,b,on='...')
# # pr(new1)
# # pr(new2)
# new3 = pd.concat([data1,data2],axis=0)                    #注意写法是.concat([a,b],axis=0)
# pr(new3)
# new4 = pd.concat([data1,data2],axis=1)                    #注意写法是.concat([a,b],axis=0)
# pr(new4)

# frame = pd.DataFrame({
#     'color':['white','red','green','red','green'],
#     'price1':[5,4,2,4.5,2.5]})

# f1 = frame.groupby('color').price1
# pr(f1.mean())


# frame1 = frame.duplicated()
# pr(frame1)

# frame2 = frame.drop_duplicates()
# pr(frame2)

# data1 = pd.read_excel('c1-Chinese.xlsx')
# data2 = pd.read_excel('c1-Math.xlsx')
# data3 = pd.read_excel('class_2.xlsx')

# data = pd.merge(data1,data2, on='Name')
# datas = pd.concat([data,data3])
# # pr(datas)

# math = datas.groupby('Class').Math
# mean_math = math.mean()
# pr(mean_math)

# chinese = datas.groupby('Class').Chinese
# mean_chinese = chinese.mean()
# pr(mean_chinese)

#修改全局字体：
# plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['font.size'] = 12

# mon = np.arange(1,13)
# temp_H = [-13,-7,2,13,21,26,28,26,21,12,0,-9]
# temp_B = [5,8,13,20,25,28,30,30,26,20,13,7]
# temp_G = [18,19,22,26,30,31,33,33,32,29,25,21]

# plt.title('各城市月平均气温',fontproperties='SimHei',fontsize=22)
# plt.xlabel('月份',fontproperties='SimHei',fontsize=15,color='grey') #仅修改标题字体
# plt.ylabel('气温',fontproperties='SimHei',fontsize=15,color='grey')
# plt.plot(mon,temp_H,'go-',mon,temp_B,'ro--',mon,temp_G,'b*')
# plt.show()

