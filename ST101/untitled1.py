#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 23:07:44 2017

@author: ivanchen
"""
def f(p):
    return p
print(f(0.3))

def f1(p):
    return 1-p
print(f1(0.3))

def f2(p):
    return p*p
print(f2(0.5))

def f3(p):
    return 3*p*(1-p)*(1-p)
print(f3(0.8))

def f4(p1,p2):
    return p1*p2
print(f4(0.5,0.8))

def f5(p0,p1,p2):
    return p0*p1+(1-p0)*p2
print(f5(0.3,0.5,0.9))

def f6(p0,p1,p2):
    return p0*p1+(1-p0)*(1-p2)
print(f6(0.1,0.9,0.8))


def f7(p0,p1,p2):
    return p0*p1/(p0*p1 + (1-p0)*(1-p2))
print(f7(0.01,0.7,0.9))

def f(p0,p1,p2):
    return p0*(1-p1) / ( p0*(1-p1) + (1-p0)*p2 )
print(f(0.1,0.9,0.8))