# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:24:15 2020

@author: shri
"""

# Cricket Score

import random

def status(y,x):
    
    if x<1 or x>250:
        return "Reduce your expectations from 20-20 cricket"
    
    elif x>=y-10 and x<=y+10:
        return "Close by, you are true Indian Cricket fan !"
    
    elif x>=y-20 and x<=y+20:
        return "You dont watch that much"
    
    else:
        return "Better luck next time !"
    



compScore=random.randint(1,251)

playerScore=int(input("Your Score guess ? "))
print("Actual Score - ",compScore)
print("Guessed Score - ",playerScore)

print(status(compScore,playerScore))