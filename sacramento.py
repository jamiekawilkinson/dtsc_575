#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 12:06:37 2022

@author: mrsjneal
"""

import numpy as np
import pandas as pd
#import statsmodels.formula.api as smf
import statsmodels.api as sm


df = pd.read_csv('sacramento.csv')

#df = pd.read_csv('/Users/mrsjneal/Desktop/dtsc_575/sacramento.csv')
#df.rename(columns={'Credit amount':'Credit_amount'}, inplace=True)
#print(df)
#df.head()

#0 => baths = 1
#1 => baths >= 1

df['baths2']= np.select([(df['baths'] == 1), (df['baths'] >= 1)], [0,1])


#show all col names
#col_list = list(df.columns)
#print(col_list)

#describe the model
x = df.loc[:, ['beds', 'sqft', 'price']]
x = sm.add_constant(x, prepend=True)
y = df.baths2

#fit model
mod1 = sm.Logit(y, x).fit()

print(mod1.params.round(2))
print(mod1.pvalues.round(2))
print('The smallest p-value is for sqft')
