#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:01:29 2022

@author: mrsjneal
"""

'''
Create a program called randdf.py that has a function that takes two integer  \
arguments and prints a Pandas dataframe.  The two arguments will correspond \
to the number of rows and number of columns, respectively.  The dataframe \
should be filled with random integers from 0 to 100.  Set your random seed \
to 56. 
Note: Use random from numpy. Otherwise, you might get a different result.
'''

import sys
import numpy as np
import pandas as pd

num_rows = int(sys.argv[1])
num_cols = int(sys.argv[2])

#num_rows = 4
#num_cols = 5

np.random.seed(56)


def randdf():
    rand_data = pd.DataFrame(np.random.randint(0,100, size=(num_rows, num_cols)))
    print(rand_data)
    
randdf()