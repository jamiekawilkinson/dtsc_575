#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:05:16 2022

@author: mrsjneal
"""

import sys
import numpy as np

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])


np.random.seed(42)

def reallyrandom():
    try:
        rand_int = np.random.randint(0,10, size = num1)
        mult_rand = rand_int * num2
        idx_result = mult_rand[num3]
        print("Your random value is", idx_result)
    except:
        num3 > num1
        
reallyrandom()
        