#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:58:42 2018

@author: domenjemec
@title: 2018-12-08 Loop
"""


def main():
    x = 0

    # define a while loop
    while (x < 5):
        print(x)
        x = x + 1

    # define a for loop

    for x in range(0, 10):

        print(x)

    # use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    # use the break and continue statements
    for x in range(5, 100):
        # if (x == 7): break
        if (x % 2 == 0):
            continue
        print(x)

    # using the enumerate() function to get index
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, d in enumerate(days):
        print(i, d)


if __name__ == "__main__":
    main()
