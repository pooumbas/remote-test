#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np 
primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
def Bens_fun(x):
    for ii in range(x//2):
        if ii in primes:
            for ee in range((x//2)):
                if ee in primes:
                    if ii*ee==x:
                        print(ii,ee)
print(Bens_fun(115))

def bens_fun(x):
    y=[]
    count=0
    for ii in primes:
        if ii>x:
            break
        while x%primes[count]==0:
            x=x/primes[count]
            y.append(primes[count])
        count+=1
    return y
print(bens_fun(115))

def prime_check(x):        
    for ii in range(2,x):
        if x%ii==0:
            return False
    return True
print(prime_check(10))
count=0
for ii in range(1000):
    if prime_check(ii)==True:
        count+=1
print(count)    
                        
        
       
            
            

