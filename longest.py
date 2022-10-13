#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 18:08:45 2022

@author: mrsjneal
"""

import sys

str_input = sys.argv[1]
str_list = str_input.split(' ')  
    
def longest():
    string_length = 0
    longest_string = ""
    
    for string in str_list:
        if len(string) > string_length:
            string_length = len(string)
            longest_string = string.lower()
    
    print("The longest word is %s" % longest_string)

longest()


    