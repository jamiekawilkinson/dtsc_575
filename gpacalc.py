#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 12:48:41 2022

@author: mrsjneal
"""

import sys

grd1 = str(sys.argv[1]).upper()
grd2 = str(sys.argv[2]).upper()
grd3 = str(sys.argv[3]).upper()
grd4 = str(sys.argv[4]).upper()

grades = [grd1, grd2, grd3, grd4]

gradgpa = {'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, \
           'C':2.0, 'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}
    
gpa = (gradgpa[grd1] + gradgpa[grd2] + gradgpa[grd3] + gradgpa[grd4]) / 4

print("My gpa is", "{:.2f}".format(gpa)) 