#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 12:02:03 2022

@author: mrsjneal
"""

import sys

str_input = str(sys.argv[1]).strip()

def countVowels():
    uniq_vals = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(len(str_input)):
        if str_input[i].lower() in vowels:
            if str_input[i].lower() in uniq_vals:
                continue
            else:
                uniq_vals.append(str_input[i].lower())
            
    print(len(uniq_vals))
            
countVowels()
