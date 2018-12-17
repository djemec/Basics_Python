#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:21:52 2018

@author: domenjemec
@title: 2018-12-11 file
"""
import csv
import numpy

d = "/Users/domenjemec/Downloads/Uber_Info/"
delivery_Csv = "Delivery.csv"

def main():
    # Open a file for writing and create it if it doesn't exist
    # f = open("textfile.txt", "w+")

    # Open the file for appending text to the end
    # f = open("textfile.txt", "a+")

    # write some lines of data to the file
    # for i in range(10):
        # f.write("This is line %d\r\n" % (i+1))

    # close the file when done
    # f.close()

    # Open the file back up and read the contents
    f = open(d + delivery_Csv, "r")
    if f.mode == 'r':
        # check to make sure that the file was opened
        # use the read() function to read the entire file
        contents = f.read()
        print(contents)

        # fl = f.readlines()
        # readlines reads the individual lines into a list
        # for x in fl:
            # print(x)

    reader = csv.reader(open(d + delivery_Csv, "r"), delimiter=",")
    x = list(reader)
    print(x)
    
    # a = numpy.loadtxt(open(d + delivery_Csv, "rb"), delimiter=",", skiprows=1)
    # print(a)


if __name__ == "__main__":
    main()
