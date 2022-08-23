import numpy as np
import pandas as pd
def compute_cost(x,y,w,b):
    x = np.array([1,2])
    y = np.array([300,500])
    n = np.size(x)
    cost_sum = 0
    for i in range(n):
        f_wb = w*x(i)+b
        cost = (f_wb - y(i))**2
        cost_sum = cost_sum + cost
    j = cost_sum/(2*n)
    return j
