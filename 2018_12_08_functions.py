#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 12:43:57 2018

@author: domenjemec
@title: 2018-12-08 Functions
"""
#Function type
f=""
#define a basic function
def basic_function():
    global f
    f="basic"
    print("I am the " + f + " function")
 
#function that takes arguments
def basic_arg_function(arg1, arg2):
    global f
    f="basicArg"
    print("I am the " + f + " function with inputs 1:" + arg1 + " 2:" + arg2)

#function that returns a value
def basic_func_w_return(arg1):
    global f
    f="basicArgWValue"
    y="Int " if isinstance(arg1,int) else "String "
    return "I am the " + f + " function with inputs 1:" + y+ str(arg1)

#function that with default value for an argument
def power(num,x=1):
    result = 1
    for i in range(x):
        result = result * num
    return "I am the defalutArgWReturn function value: " + str(result)

#function with variable number of arguments
def multi_add(*args):
    result = ""
    for s in args: 
        result = s if result =="" else result + ", " + s
    return result

#function with variable and non variable args (note var has to be last)
def multi_add_prefixed(start, *args):
    n = multi_add(args)
    return start + str(n)

    
    
#executes
#basic_function()
#basic_arg_function(arg1="value1",arg2="value2")
#print(basic_func_w_return(1))
#print(power(9,4))
#print(power(x=14, num=2))


#String parsing / array indexing fun
#x="9^4"
#print(power(int(x.split("^")[0]),int(x.split("^")[1])))


#print("Variable formula: " + multi_add("A", "B", "C"))
print(multi_add_prefixed("This is the start string for a mixed formula: ", "A", "B", "C"))