#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 17:29:45 2022

@author: mrsjneal
"""

import sys

rship = sys.argv[1]
#rship = rship.replace(" ", "")

relations = {'Darth Vader':'father', 'Leia':'sister', 'Han':'brother in law', \
             'R2D2':'droid', 'Rey':'Padawan', 'Tatooine':'homeworld'}

def luke():
    if rship == 'Darth Vader':
        print("No, I am your father") 
    else:
        print("Luke, I am your", relations[rship])

luke()
    