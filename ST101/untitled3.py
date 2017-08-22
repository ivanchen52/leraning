#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:11:11 2017

@author: ivanchen
"""
from __future__ import division
class FlipPredictor(object):
    def __init__(self,coins):
        self.coins=coins
        n=len(coins)
        self.probs=[1/n]*n
    def pheads(self):
        return sum(pcoin*p for pcoin,p in zip(self.coins,self.probs))    

    def update(self,result):
        pheads=self.pheads()
        if result=='H':
            self.probs=[pcoin*p/pheads for pcoin,p in zip(self.coins,self.probs)]
        else:
            self.probs=[(1-pcoin)*p/(1-pheads) for pcoin,p in zip(self.coins,self.probs)]
            
def test(coins,flips):
    f=FlipPredictor(coins)
    quesses=[]
    for flip in flips:
        f.update(flip)
        quesses.append(f.pheads())
    return quesses
print(test([0.5,0.4,0.3],'HHTH'))