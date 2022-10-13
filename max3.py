#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:02:54 2022

@author: mrsjneal
"""

import sys

num1 = sys.argv[1]
num2 = sys.argv[2]
num3 = sys.argv[3]

numlist = [num1, num2, num3]

def max3():
    print(max(numlist))
    
max3()