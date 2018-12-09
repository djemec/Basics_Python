#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 16:23:00 2018

@author: domenjemec
@title: 2018-12-08 DateTime Worksheet
"""
from datetime import date
from datetime import time
from datetime import datetime


def main():
    # DATE OBJECTS
    # Get today's date from simple today() method from the date class
    today = date.today()
    print("Today's date is ", today)

    # print out the date's individual components
    print("Date Components: ", today.day, today.month, today.year)

    # retrieve today's weekday 0-6 Sunday
    print("Day count is ", today.weekday())

    # DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print("Datetime is ", today)

    # Get the current time
    t = datetime.time(today)
    print("time is ", t)


if __name__ == "__main__":
    main()
