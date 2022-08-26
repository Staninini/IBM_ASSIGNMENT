# # *********************************
# # Python multiprocessing

# # *********************************
# # multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
# #                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
# #                   multithreading = better for io bound tasks (waiting around)

# from multiprocessing import Process, cpu_count
# import time

# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
# # 3.636472700003651 seconds seconds on single process
# # 2.074777100002393 seconds on 2 process
# # 1.9359494999953313 seconds on 3 process
# # 1.6961437999852933 seconds on 4 process
# # 1.353144099994097 seconds on 5 process
# # 1.2608994000038365 seconds on 6 process
# # 1.5303754000051413 seconds on 7 process

# def main():
#     print("cpu count:", cpu_count()) # you can only run as many processes as the no of cores in your cpu
#     # any more will actually increase exec time as it becomes redundant 
# # if we were to use only one thread with 100m it would take a long time
#     #a = Process(target=counter, args=(100000000,)) #takes 5.16 sec
#     # #takes 3.03 sec
#     a = Process(target=counter, args=(16666666.6667,))
#     b = Process(target=counter, args=(16666666.6667,)) # 5.19
#     c = Process(target=counter, args=(16666666.6667,))
#     d = Process(target=counter, args=(16666666.6667,))
#     e = Process(target=counter, args=(16666666.6667,))
#     f = Process(target=counter, args=(16666666.6667,))


#     x=time.perf_counter() # to note starting time
#     a.start()
#     b.start()
#     c.start()
#     d.start()
#     e.start()
#     f.start()


#     print("processing...")
#     #counter(100000000)
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     e.join()
#     f.join()




#     y=time.perf_counter()
#     print("Done!")
#     print("finished in:",y-x, "seconds")

  
# if __name__ == '__main__':
#     main()

import os
path = "C:\Users\roone\Desktop\Python\new project\IBM_Assignment"
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    if os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")