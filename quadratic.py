#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:20:17 2022

@author: mrsjneal
"""

import sys
import math
#import cmath

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

a = float("{:.2f}".format(a))
b = float("{:.2f}".format(b))
c = float("{:.2f}".format(c))

x = (-b + math.sqrt((b**2)-4*a*c)) / (2*a)
y = (-b - math.sqrt((b**2)-4*a*c)) / (2*a)

x = "{:.2f}".format(x)
y = "{:.2f}".format(y)

print("The solutions are", x, "and", y )