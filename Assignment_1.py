# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:27:17 2020

@author: shri
"""

# Grade

score=int(input("Enter your score --- "))

if score>=90:
    print("----------")
    print("|         | ")
    print("|    A    |")
    print("|         | ")
    print("-----------")
    
elif score>=80 and score<90:
    
    print("----------")
    print("|         | ")
    print("|    B    |")
    print("|         | ")
    print("-----------")
    

elif score>=70 and score<80:
    
    print("----------")
    print("|         | ")
    print("|    C    |")
    print("|         | ")
    print("-----------")


elif score>=60 and score<70:
    
    print("----------")
    print("|         | ")
    print("|    D    |")
    print("|         | ")
    print("-----------")
        
    

elif score>=50 and score<60:
    
    print("----------")
    print("|         | ")
    print("|    E    |")
    print("|         | ")
    print("-----------")
        
    
else:
    print("--- FAIL ---")    