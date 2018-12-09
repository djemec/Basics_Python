#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 14:31:06 2018

@author: domenjemec
@title: 2018-12-08 Classes
"""


class MyClass():
    def method_1(self):
        print("MyClass method1")

    def method_2(self, someString):
        print("MyClass method2 " + someString)


class SecondClass(MyClass):
    def method_1(self):
        MyClass.method_1(self)
        print("second class first method")

#    def method_2(self, someString):
#        print("second class second method: " + someString)


def main():
    c = MyClass()
    c.method_1()
    c.method_2("A String")
    P = input("please enter your name: ")

    c2 = SecondClass()
    c2.method_1()
    c2.method_2(P)


if __name__ == "__main__":
    main()
