# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:47:16 2020

@author: shri
"""

# Photo

def profilePhotoAcceptance(L,N):

    for i in range(0,N):
        print()
        W=int(input("Enter width --- "))
        H=int(input("Enter height --- "))
        print()
        print("Width = ",W," Height = ",H)
        
        if W<L or H<L:
            print("Upload Another")
        
        elif W==H:
            print("Accepted !")
            break
        
        else:
            print("Crop it")
        

L=int(input("Enter the minimum dimension --- "))
N=int(input("Enter no of photos --- "))

profilePhotoAcceptance(L,N)