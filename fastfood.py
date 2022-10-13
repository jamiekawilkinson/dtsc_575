#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 10:51:20 2022

@author: mrsjneal
"""

#import numpy as np
import pandas as pd
#import statsmodels.formula.api as smf
import statsmodels.api as sm

df = pd.read_csv('fastfood.csv')
#print(df)
#df.head()

#show all col names
#col_list = list(df.columns)
#print(col_list)

#describe the model
x = df.loc[:, ['total_fat', 'sat_fat','cholesterol','sodium']]
x = sm.add_constant(x, prepend=True)
y = df['calories']

#fit model
mod1 = sm.OLS(y, x).fit()

#summarize the model (logistics regression table)
sum1 = mod1.summary()
#print(sum1)

print(mod1.mse_total.round(2))
print(mod1.rsquared.round(2))
print(mod1.params.round(2))
print(mod1.pvalues.round(2))





