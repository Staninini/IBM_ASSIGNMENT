# import os
# # print(os.getcwd())
# path = r"C:\Users\roone\Desktop\Python\new project\IBM_Assignment"
# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That is a file")
#     if os.path.isdir(path):
#         print("That is a directory!")
# else:
#     print("That location doesn't exist!")

# with open('employees1.txt') as emp:
#     # a = emp.readlines()
#     b = emp.readline()
#     c = emp.readline()
#     # print(a)
#     print(b)
#     print(c)

# with open('schedule.txt') as schedule:
#     line = schedule.readline()
#     while line:
#         if line != '\n':
#             try:
#                 data = line.split(';')
#                 print(data[0])
#             except IndexError:
#                 pass
#         line = schedule.readline()

# with open('employees1.txt') as emp:
#     lines = emp.readlines()
#     n = [0,2,4]
#     for i in n:
#         spl = lines[i].split(' - ')
#         print(spl[0])


# Q1: You have a file with some numbers inside, read the numbers from
# numbers.txt and multiply by 5 , then write the result into a new file named
# result.txt

        
# with open('Yuc Z. - numbers.txt','r') as numbers:
#     with open('result.txt','w') as results:
#         a = numbers.readline()
#         while a:
#             b = str(int(a)*5)
#             results.write(f'{b}\n')
#             a = numbers.readline()


# Q2: Read a file named agenda.txt that contains the entry records for
# each person , and take input to select which person you want to search for and show their data
# if the person does not exist then add their data into the file
# <date>;<name>;<time>

with open('Yuc Z. - agenda.txt','r') as agenda:
    n = agenda.read()
    a = input('input the name:')
    m = n.split('\n')
    for i in m:
        if a in i:
            print(i)
        else:
            agenda.close()
            with open('Yuc Z. - agenda.txt','a') as agenda:
                b = input('input the date:')
                c = input('input the name:')
                d = input('input the time:')
                agenda.write(f'{b};{c};{d}\n')
            break