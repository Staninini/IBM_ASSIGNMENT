# # Web scraping exercise: local file home.html

# from bs4 import BeautifulSoup 
# pr = print

# with open('home.html','r') as html_file:
#     content = html_file.read()
#     soup = BeautifulSoup(content, 'lxml')
#     # courses_html_tags = soup.find_all('h5')        #.find命令只会查找第一个数据，.find_all命令可以查找所有数据
#     # for course in courses_html_tags:
#     #     pr(course.text)        #.text命令 只打印会显示出来的文字部分
#     course_cards = soup.find_all('div',class_ = 'card')      #class已经是python自带的一个功能，因此这边不能用class，要加下划线class_
#     for course in course_cards:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1]   #.split的用法，从split出的list里取某个数值的方法
#         pr(f'{course_name} costs {course_price}.')

# # Web scraping exercise: real website
# from bs4 import BeautifulSoup
# import requests
pr = print

# html_text = requests.get('https://sou.zhaopin.com/?jl=489&kw=python').text
# soup = BeautifulSoup(html_text, 'lxml')
# jobs = soup.find_all('div', class_='joblist-box__item clearfix')

# for job in jobs:
#     date = job.find('span', class_ = 'iteminfo__line3__status__recruit').text.replace('\n','')
#     if date == '最近' or date == '最新':
#         job_title = job.find('span', class_='iteminfo__line1__jobname__name').text.replace(' ','')
#         company_name = job.find('div', class_='iteminfo__line1__compname').text.replace(' ','')
#         salary = job.find('p', class_='iteminfo__line2__jobdesc__salary').text.replace(' ','')
#         info = job.a['href']
#         pr(f'''
# 招聘职位：{job_title}
# 公司名称：{company_name}
# 薪资范围：{salary.strip()} 
# 更多信息：{info}
# ''')          #.strip()命令可以整理文字格式，去掉不必要的换行和空格

# import pandas as pd
# import matplotlib.pyplot as plt
# from datetime import datetime
# plt.style.use('seaborn')
# import yfinance as yf

# msft = yf.Ticker('msft')
# info = msft.info
# for k,v in info.items():    #字典后面加上.items()来提取它的key和value！！！！！！！！！！
#     print(k, ':', v)

# sector = info['sector']
# pr(sector)
# employee = info['fullTimeEmployees']
# pr(employee)

# pr(msft.institutional_holders)
# pr(type(msft.dividends))
# df = msft.dividends
# data = df.resample('Y').sum()
# data = data.reset_index()
# data['Year'] = data['Date'].dt.year

# plt.figure()
# plt.bar(data['Year'],data['Dividends'])
# plt.ylabel('Dividend Yield($)')
# plt.xlabel('Year')
# plt.show()