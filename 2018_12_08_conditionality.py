#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:58:42 2018

@author: domenjemec
@title: 2018-12-08 Conditionality
"""

def main():
    x, y = 100, 100
    
    #conditional flow for if, elif, else
    if(x< y):
        st = "x is less than y"
    elif(x==y):
        st="x and y are equal"
    else:
        st = "y is less than y"
        
        

    
    #conditional statements to use "a if c else b"
    st = "x is definitely less than y" if (x<y) else "x is greater than or the same as y"
    
    print(st)
    
    
if __name__ == "__main__":
    main()