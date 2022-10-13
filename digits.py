#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 12:29:25 2022

@author: mrsjneal
"""

import sys
#import string

num_input = sys.argv[1]
#num_input = num_input.strip(string.whitespace + string.punctuation)

def digits():
    dig_count = 0
    
    for i in num_input:
        if i == ".":
            continue
        else:
            dig_count += 1
    print(dig_count)
    
digits()