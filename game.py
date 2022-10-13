#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 11:20:41 2022

@author: mrsjneal
"""

import numpy as np

def get_num():
    num = np.random.randint(0,11)
    return num

def compare(a,b):
    if a > b:
        return True
    else:
        return False

def check_winner(a,b):
    if (a > b) and (a >= 15):
        return("P1")
    elif (b > a) and (b >= 15):
        return("P2")
    else:
        return("No winner")
        
class Player():
    def __init__(self, name, card, score):
        self.name = name
        self.card = card
        self.score = score

p1 = Player("David", 0, 0)
p2 = Player("Olivia", 0, 0)

while p1.score <= 15 and p2.score <= 15:
    p1.card = get_num()
    p2.card = get_num()
    
    if compare(p1.card, p2.card):
        p1.score += p1.card - p2.card
    else:
        p2.score += p2.card - p1.card

print("P1 Score: ", p1.score)
print("P2 Score: ", p2.score)
    