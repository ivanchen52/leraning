#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 17:57:35 2017

@author: ivanchen
"""

from random import randint

N = 1000

def simulate(N):
    K = 0
    for i in range(N):
        truth  = randint(1,3)
        guess1 = randint(1,3)
        if truth == guess1:
            monte = randint(1,3)
            while monte == truth:
                monte = randint(1,3)
        else:
            monte = 6 - truth - guess1
        guess2 = 6 - guess1 - monte
        if guess2 == truth:
            K = K + 1
    return float(K) / float(N)

def simulate2(N):
    K = 0
    for i in range(N):
        truth = randint(1,3)
        guess1 = randint(1,3)
    #    if truth == guess1:
    #        monte = randint(1,3)
    #        while monte == truth:
    #            monte = randint(1,3)
    #    else:
    #        monte = 6 - truth - guess1
    #    guess2 = 6 - guess1 - monte
        if guess1 == truth:
            K = K + 1
        
    return float(K) / float(N)

print(simulate(N))