# # q: create functions a and b , a adds 2 numbers together , 
# # b divides the result by 3
# # use lambda function to solve this problem

# add = lambda x,y: x+y 
# div = lambda x: x/3 
# print(add(5,7))
# print(div(9))

# # Q: Sort the data based on grade and print the names of the top 10 students
# # Q: ALso Print the names of the students who failed i.e. scored below 50

# students = (("Squidward", "F", 33),
#             ("Sandy", "A", 96),
#             ("Patrick","D", 65),
#             ("Obiwan","B", 80),
#             ("Yoda","A+", 98),
#             ("Kenobi","C", 75),
#             ("R2d2","A+", 99),
#             ("Ben","A+", 96),
#             ("Ron","D", 66),
#             ("Eren","A", 97),
#             ("Jonny","C", 70),
#             ("Mr.X","A+", 100))
# grade = lambda grades: grades[2]
# s = sorted(students,key=grade,reverse=True)
# print(s[:10])

# for i in range(len(students)):
#     k = students[i][2]
#     if k<50:
#         print(students[i])

# Exercise:
# Use the same store list and now convert 
# the store_euros list prices to CAD and round to 2 dp
# 1 CAD=1.3783 Euro

# store = [("shirt",20.00), # euro
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]
# to_cad = lambda data: (data[0], f'{round(data[1]*1.3783,2)}CAD')
# cad_price = list(map(to_cad,store))
# grade = lambda grades:grades[1]
# cad_price.sort(key=grade)
# print(f'The most expensive item is {cad_price[-1]}, the chepest item is {cad_price[0]}.')

# Q use the same friends list and filter out the friends whose names start with T 
# and display their score seperately

# friends_score=[("Racheal",10)
#                 ,("Monica",12),
#                 ("Abraham",15),
#                 ("Tim",3),
#                 ("Rafael",5),
#                 ("Janice",9),
#                 ("Tony",11),]

# a = lambda x:x[0][0]!='T'
# name = list(filter(a,friends_score))
# # b = lambda x: print(f'Name:{x[0]}   Score:{x[1]}')
# # list(map(b,name))
# for i in name:
#     print("Name:{} Score:{}".format(i[0],i[1]))

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")

# a=          [("Dude","p@ssword"),("Bro","abc123"),("Mister","guest")]

# l = []
# for i in range(len(usernames)):
#     m = (usernames[i],passwords[i])
#     l.append(m)
# print(l)

# Q : Create 2 lists one with employee names and other with their 
# respective roll numbers
# and combine the 2 to create a dictionary 
# where the roll number is the key that returns the
# name of the employee

# name = ['Ana', 'Sara', 'Tom', 'Jack', 'Donald']
# num = [2,1,5,4,6]
# employee = dict(zip(num,name))
# print(employee)

# Following is a piece of code that goes through a 
# list of products and seperates the items which start 
# with an "M" into a seperate list 

# Write the following first using lambda and filter function , 
# then write it using list comprehension

# product_list=["Milk","Mars","Coffee"," ","Mango Juice","Snacks"," ",]
# a = lambda x: x[0]=='M'
# li = list(filter(a,product_list))
# print(li)

# l = [i for i in product_list if i[0]=='M']
# print(l)

# formula F -> C : (farenheit_temp_value-32)*(5/9)

# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# for key,value in cities_in_F.items():
#     cities_in_F[key] = (value-32)*(5/9)
# print(cities_in_F)

#Q: You have a dictionary containing the following information:

# Your job is to return a dictionary that encrypts the password of each of the user 
# by first reversing the password and adding an "A" after every letter 

# Ex 12304n12oi => iAoA2A1AnA4A0A3A2A1
# solve this problem by using dictionary comprehension for both encryption and decryption
# isalpha isnumeric

from turtle import st


passwords={"Tim":"123o4n12oi","John":"12345qaz","Brad":"@#$$%AWES","Jessica":"1995"}

def rev(x):
    x = list(x[::-1])
    for i in range(len(x)-1):
        x.insert(2*i+1,'A')
    return "".join(x)

psw = {key:rev(value) for (key,value) in passwords.items()}
print(psw)

def p(x):
    x = list(x[::-1])
    for i in range((len(x)-1)//2):
        x.pop(-i-2)
    return "".join(x)

original_psw = {key:p(value) for (key,value) in psw.items()}
print(original_psw)