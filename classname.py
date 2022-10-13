#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:40:40 2022

@author: mrsjneal
"""

import sys
name = str(sys.argv[1])

class person():
    def __init__(self, name):
        self.name = name
    
    def hello(self):
        print("My name is", name, "and I am a", x.__class__.__name__)

x = person(name)
x.hello()
print(x.__class__)

'''
import sys
class person():
    def __init__(self, hello):
        self.name = hello
        self.display_name = self.__class__.__name__
        
        print("My name is", self.name, "and I am a", self.display_name)
persons_name = person(sys.argv[1])
persons_name.name
print (persons_name.__class__)

'''