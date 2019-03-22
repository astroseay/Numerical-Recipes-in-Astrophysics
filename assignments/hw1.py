"""
@author: christopher seay
         s2286181

3 tasks:
"""
import numpy as np
import matplotlib.pyplot as plt
###### Task 1: building a poisson distribution function and a
###### random number generator
### 1a poisson distribution
def poissonDist(w,k):
    # poisson distribution given by: P_w(k) = [w^k * e^(-w)] / k!
    n = factorial(k)
    P = (w**k)*(np.e**(-w))/n
    P_w = (w**k)*(np.e**(-w))/factorial(k)
    return P_w

def factorial(n):
    if n < 0 or type(n) is float:
        raise ValueError('non-integers and negative numbers are invalid')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return float(result)
# output below works
# print(poissonDist(1,0),poissonDist(5,10),\
#         poissonDist(3,20),poissonDist(2.6,40))

### 1b random number generator
I_j = 0 # set seed
def mlcg(seed=I_j,a=9824192,m=2**64-1):
    # want to remember the last value of the local I_j so that it changes
    # the next step o set seed to global
    global I_j
    c = 12235356
    I_j = (a*I_j + c) % m
    return I_j

def shift_xor(a1=21,a2=35,a3=4):
    global X, Y, Z, W
    X = mwc()
    Y = mwc()
    Z = mwc()
    W = mwc()
    t = X ^ (X << a1)
    X = Y
    Y = Z
    Z = W
    W = W ^ (W >> a2) ^ t ^ (t >> a3)
    return W

def mwc(a = 182937572,m = 2**64-1):
    x = a*(mlcg() & m) + (mlcg() >> 32)
    #let's mwc!
    print(x)
    return x

# arr_random1 = []
# arr_random2 = []
# for i in range(0,1000):
#     arr_random1.append(mlcg(I_j))
#     arr_random2.append(mlcg(I_j))
# print(arr_random1)
#
# plt.scatter(arr_random1,arr_random2,c='c')


###### Task 2: satellite galaxies study
