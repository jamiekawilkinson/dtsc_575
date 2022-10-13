#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:39:43 2022

@author: mrsjneal
"""

import sys

int_input = int(sys.argv[1])
int_input2 = int(int_input + 4)
val_list = []

for i in range(5000, 8001):
   if((i%int_input==0) & (i%int_input2==0)):
       val_list.append(i)
       
print(val_list)
      
