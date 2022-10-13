#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 09:34:52 2022

@author: mrsjneal
"""

import sys
import numpy as np

int1 = int(sys.argv[1])
int2 = int(sys.argv[2])
int3 = int(sys.argv[3])
int4 = int(sys.argv[4])

def intarray():
    numarray = np.array([int1, int2, int3, int4])
    
    print(type(numarray))
    print(int1*int2*int3*int4)

intarray()