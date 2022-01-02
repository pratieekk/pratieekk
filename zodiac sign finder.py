# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 11:44:44 2022

@author: Shree
"""
print("\t\t \b this code tells your zodiac sign based on your birth day\n")
#print()
d=int(input("enter the birth date: "))
#print("\n")
m=input("enter the month: ")
#print("\n")
y=int(input("enter the year: "))
print("your date of birth is ",d,m,y)
print("your zodiac sign is:-")
if (m=="january"):

    if d in range(1,21):
        
        print("capricorn")
        
    else:
        print("aquarious")
     
     
if(m=="february"):
    
    if d in range(1,19):
     
        print("aquarious")
    else:
         print("pisces")
     
if(m=="march"):
    
    if d in range(1,21):
     
        print("pisces")
    else:
         print("aries")
         
if(m=="april"):
    
    if d in range(1,20):
     
        print("aries")
    else:
         print("taurus")
         
if(m=="may"):
    
    if d in range(1,21):
     
        print("taurus")
    else:
        print("gemini")

if(m=="june"):
    
    if d in range(1,21):
     
        print("gemini")
    else:
         print("cancer")
         
if(m=="july"):
    
    if d in range(1,23):
     
        print("cancer")
    else:
         print("leo")

if(m=="august"):
    
    if d in range(1,23):
     
        print("leo")
    else:
         print("virgo")

if(m=="september"):
    
    if d in range(1,23):
     
        print("virgo")
    else:
         print("libra")

if(m=="october"):
    
    if d in range(1,23):
     
        print("libra")
    else:
         print("scorpio")
         
if(m=="november"):
    
    if d in range(1,22):
     
        print("scorpio")
    else:
         print("sagitarus")
         
if(m=="december"):
    
    if d in range(1,22):
     
        print("sagitarus")
    else:
         print("capricorn")
     
     
     
     
     
     
     
         
     
     
     
