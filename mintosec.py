#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:08:04 2022

@author: mrsjneal
"""

import sys

num_secs = float(sys.argv[1])

def mintosec():
    num_min = num_secs * 60
    num_min = round(num_min, 2)
    print(num_min)
    
mintosec()