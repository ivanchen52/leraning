#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:19:56 2017

@author: ivanchen
"""

#Complete the median function to make it return the median of a list of numbers
data1=[1,2,5,10,-20]
def median(data):
    #Insert your code here
    idx = len(data)/2
    sortdata = sorted(data)
    return sortdata[idx]
print(median(data1))