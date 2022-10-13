#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 09:47:14 2022

@author: mrsjneal
"""
import sys

fname = str((sys.argv[1]))
lname = str((sys.argv[2]))
grade_lvl = int((sys.argv[3]))
gpa = float((sys.argv[4]))
creds = float((sys.argv[5]))

class Record():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        
class Student(Record):
    def __init__(self,fname, lname, grade_lvl,gpa, creds):
        super().__init__(fname, lname)
        self.grade_lvl = grade_lvl
        self.gpa = gpa
        self.creds = creds
        
x = Record(fname, lname)
y = Student(fname, lname, grade_lvl,gpa, creds)

print("******* STUDENT RECORD *******")
print(x.fname, x.lname, y.grade_lvl, y.gpa, y.creds)