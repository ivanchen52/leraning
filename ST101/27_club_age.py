#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:05:17 2017

@author: ivanchen
"""
from math import sqrt

ClubAgeData = [21,21,21,21,24,24,24,24,24,24,26,26,26,26,26,26,26,29,29,29,29,29,29,29,29,29,29,29,40,40]

def mean(data):
    return sum(data)/len(data)

def variance(data):
    mu = mean(data)
    return mean([(x-mu)**2 for x in data])

def factor(data):
    return 1.96

def ci(data):
    return factor(data) * sqrt(variance(data)/len(data))

print(mean(ClubAgeData))
print(variance(ClubAgeData))
print(ci(ClubAgeData))