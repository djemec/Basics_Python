#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 13:31:28 2018

@author: domenjemec
@title: Homework problem 1

"""

from matplotlib import pyplot as plt
import numpy
from scipy import stats

# Store random list of numbers
rand_list = numpy.random.randint(low=1, high=101, size=1000)

print(rand_list)

# Show data structure of random_int
print(type(rand_list))

# show max and min
rand_max_min = (min(rand_list), max(rand_list))
print(rand_max_min)
print(type(rand_max_min))

# reverse list
rand_list = numpy.flip(rand_list)
print(rand_list)

#sorts list
rand_list[::-1].sort()
print(rand_list)

# dataset
print("6a. set lenght: " + str(len(set(rand_list))))

# occurances of 50s

print(numpy.count_nonzero(rand_list == 50))

# plot NPF
val, cnt = numpy.unique(rand_list, return_counts=True)
pmf = cnt / len(rand_list)

numpy.set_printoptions(suppress=True)
print(numpy.column_stack((val, pmf)))

# histogram

fig, ax = plt.subplots(1, 1)
ax.plot(val, pmf, 'bo', ms=2, mec='b')
ax.vlines(val, 0, pmf, colors='g', linestyles='dashed', lw=2)
plt.title('Custom made discrete distribution(PMF)')
plt.ylabel('Probability')
plt.xlabel('int generated')
plt.show()

# cdf
cdf = numpy.cumsum(pmf)

plt.plot(cdf, val)

rand_list_mean = rand_list.mean()

fig_cdf, ax2_cdf = plt.subplots(1, 1)
ax2_cdf.plot(val, cdf)

ax2_cdf.vlines(rand_list_mean, 0, 1, colors='r', linestyles='-', lw=2)
plt.title('CDF Updated')
plt.ylabel('Probability')
plt.xlabel('int generated')
plt.show()
