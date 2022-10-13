#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 19:32:12 2022

@author: mrsjneal
"""

import sys
import string

str_input = sys.argv[1]
str_lower = str_input.lower()
str_nospace = str_lower.replace(" ", "")
str_nkd = str_nospace.translate(str.maketrans('', '', string.punctuation))

str_back = str_nkd[-1::-1]

def palindrome():
    if str_nkd == str_back:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")

palindrome()
