#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2018-12-08 Variables

# Declare a variable & initialize
f=0
#print(f)

# re-declaring the variable
#f="abc"
#print(f)

# Error: variables of different types cannot be combined

#print ("this is a string" + str(f))

# Global vs local in functions
def someFunction():
    global f
    #global pulls f into the function instead of doing a local variable 
    f="a string"
    print(f)


someFunction() 
print(f)
del f
f=4
print(f)