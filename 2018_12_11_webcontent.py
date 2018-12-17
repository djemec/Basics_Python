#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 23:03:13 2018

@author: domenjemec
"""

# 
# Example file for retrieving data from the internet
#
import urllib.request # instead of urllib2 like in Python 2.7


def main():
    # open a connection to a URL using urllib2
    webUrl = urllib.request.urlopen("http://www.google.com")

    # get the result code and print it
    print("result code: " + str(webUrl.getcode()))

    # read the data from the URL and print it
    data = webUrl.read()
    print(data)


if __name__ == "__main__":
    main()
