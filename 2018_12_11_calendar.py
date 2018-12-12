#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:07:03 2018

@author: domenjemec
@title: 2018-12-11 Calendar
"""
import calendar


def main():
    # text calendar
    c = calendar.TextCalendar(calendar.SUNDAY)
    st = c.formatmonth(2017, 1, 0, 0)
    print(st)

    # HTML calendar
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    hst = hc.formatmonth(2018, 12)
    # print(hst)

    # loop over the days of a month
    for i in c.itermonthdates(2017, 8):
        print(i)

    # o mean that the day of hte week is in an overlapping month
    for i in c.itermonthdays(2017, 8):
        print(i)

    for name in calendar.month_abbr:
        print(name)

    # calculate days based on a rule : first friday of every month's date
    print("Team Meeting")

    for m in range(1, 13):
        cal = calendar.monthcalendar(2018, m)
        weekone = cal[0]
        weektwo = cal[1]

        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]

        print("%10s %2d" % (calendar.month_name[m], meetday))


if __name__ == "__main__":
    main()
