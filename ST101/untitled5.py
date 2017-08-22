#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 23:09:09 2017

@author: ivanchen
"""

from math import sqrt

def mean(data):
    return sum(data)/len(data)

def variance(data):
    mu = mean(data)
    return mean([(x-mu)**2 for x in data])

def ci(data):
    return factor(data) * sqrt(variance(data)/len(data))

def factor(l):
    return 1.96

data = [1,1,1,1,0,0,0,0,0,0,0,0,0,0]
data2 = [199,200,201,202,203,204,205,206]
data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]

#print(variance(data3))
print(mean(data2))
print(variance(data2))
print(ci(data2))
