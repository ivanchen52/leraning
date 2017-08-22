#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 22:25:32 2017

@author: ivanchen
"""

#Complete the test function to perform a hypothesis test 
#on list l under the null that the mean is h

from math import sqrt

def mean(l):
    return float(sum(l))/len(l)

def var(l):
    m = mean(l)
    return sum([(x-m)**2 for x in l])/len(l)

def factor(l):
    return 1.96


def conf(l):
    return factor(l) * sqrt(var(l) / len(l))


def test(l, h):
    m = mean(l)
    c = conf(l)
    return abs(m-h) <= c
    
l=[199,200,201,202,203,204]
h=201

print(mean(l))
print(conf(l))
print(test(l,h))