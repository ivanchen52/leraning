#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:13:15 2017

@author: ivanchen
"""

import random
from math import sqrt

def mean(data):
    return float(sum(data))/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))
    

def flip(N):
    return [random.random() > 0.5 for x in range(N)]

def mode(data):
    modecnt = 0
    for i in range(len(data)):
        icount = data.count(data[i])
        if icount > modecnt:
            mode = data[i]
            modecnt = icount
    return mode
