#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 20:12:53 2022

@author: mrsjneal
"""

import sys
import pandas as pd

start_slice = int(sys.argv[1])
stop_slice = int(sys.argv[2])

stop_slice -= 1

#start_slice = 4
#stop_slice = 9


df = pd.read_csv(r'president_heights.csv')

#height_col = df.loc[start_slice:stop_slice, "height(cm)"]

height_col = df.loc[start_slice:stop_slice,"height(cm)"]
sel_height = pd.DataFrame(height_col)

#print(sel_height)

total = sel_height['height(cm)'].sum()
#print(total)

div_height = (stop_slice - start_slice) + 1

stop_slice += 1

avg_height = total / div_height
print("The average height of presidents number", start_slice, "to", \
      stop_slice, "is", "{:.2f}".format(avg_height))
