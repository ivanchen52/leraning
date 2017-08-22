#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:05:17 2017

@author: ivanchen
"""
from math import sqrt
#data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
data = [0,0,0,0,1,1,1,1,1,1]
def mean(data):
    return sum(data)/len(data)
def variance(data):
    mu = mean(data)
    ndata=[]
    for i in range(len(data)):
        ndata.append((data[i]-mu)**2)
    sigma2 = mean(ndata)
    return sigma2
#print(variance(data3))

def variance2(data):
    mu = mean(data)
    return mean([(x-mu)**2 for x in data])


def ci(data):
    return 1.96 * sqrt(variance(data)/len(data))

print(mean(data))
print(variance(data))
print(ci(data*100))