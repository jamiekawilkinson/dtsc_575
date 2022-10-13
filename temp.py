#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:22:15 2022

@author: mrsjneal
"""

import sys

c_temp = float(sys.argv[1])

def temp():
    f_temp = ((9/5)* c_temp) + 32
    
    print("The temperature is %.2f degrees Fahrenheit." % f_temp)

temp()
