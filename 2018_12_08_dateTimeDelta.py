#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:43:56 2018

@author: domenjemec
@title: 2018-12-11 Time Deltas
"""
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    # Construct basic timedelta
    print(timedelta(days=365, hours=5, minutes=1))

    # print today's date
    now = datetime.now()

    # print date one year from now
    print("one year is " + str(now + timedelta(days=365)))

    # create a timedelta that uses more than 1 argument
    print("in 3 weeks, and 1 day it's " +
          str(now + timedelta(weeks=3, days=1)))

    # calculate the date 1 week ago & string format
    t = datetime.now() + timedelta(weeks=-1)
    s = t.strftime("%A %B %d, %Y")
    print("1 week ago was " + s)

    # how many days until April 14 1941
    today = date.today()
    new_date = date(2019, 4, 14)
    if new_date < today:
        print("It's in the past by %d days" % ((today-new_date).days))
        new_date = new_date.replace(year=today.year+1)
    print("the next April 4th is %d days away" % ((new_date-today).days))


if __name__ == "__main__":
    main()
