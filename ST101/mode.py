#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:36:09 2017

@author: ivanchen
"""

#Complete the mode function to make it return the mode of a list of numbers
data1=[1,2,5,10,-20,5,5]
def mode(data):
    modecnt = 0
    for i in range(len(data)):
        icount = data.count(data[i])
        if icount > modecnt:
            mode = data[i]
            modecnt = icount
    return mode


print(mode(data1))