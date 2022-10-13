#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 09:50:03 2022

@author: mrsjneal
"""

import sys

str_input = str(sys.argv[1]).strip()

def capCount():
    count_Cap = 0
    sum_Cap = 0
    
    for i in range(len(str_input)):
        if str_input[i].isupper():
            count_Cap += 1
            sum_Cap += i 
            #print(i)
            
    print(count_Cap)
    print(sum_Cap)
    
capCount()
            