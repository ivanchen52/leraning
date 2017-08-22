#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 14:26:10 2017

@author: ivanchen
"""




try:
    guess_row = int(input("Guess Row:"))
except ValueError:
   print("That's not an int!")