#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:43:03 2022

@author: mrsjneal
"""

import sys

f_name = sys.argv[1]
l_name = sys.argv[2]

def username():
    u_fname = f_name[0].lower()
    u_lname = l_name[-7:].lower()
    
    u_name = u_fname + u_lname + str(len(f_name + l_name))
    
    print ("Your username is " + u_name)

username()