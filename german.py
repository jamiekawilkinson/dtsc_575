#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 11:45:29 2022

@author: mrsjneal
"""

#import numpy as np
import pandas as pd
#import statsmodels.formula.api as smf
import statsmodels.api as sm

df = pd.read_csv('german_credit_data.csv')
df.rename(columns={'Credit amount':'Credit_amount'}, inplace=True)
#print(df)
#df.head()


#show all col names
#col_list = list(df.columns)
#print(col_list)

#describe the model
x = df.loc[:, ['Age', 'Duration']]
x = sm.add_constant(x, prepend=True)
y = df['Credit_amount']

#fit model
mod1 = sm.OLS(y, x).fit()

print(mod1.params.round(2))
print(mod1.rsquared.round(2))
