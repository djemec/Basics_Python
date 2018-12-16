#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:44:02 2018

@author: domenjemec
@title: homework2
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


d = "/Users/domenjemec/Documents/Python/Homework/data/"
scores = "scores.csv"
sleep = "sleep.csv"

# extract data
scoresdf = pd.read_csv(d + scores)
sleepdf = pd.read_csv(d + sleep)


def process_data(leftdf, rightdf, join_field, join, x, y):
    """
    Merges 2 dataframes and strips out outliers (> 3 stdev)

    Arguments:
    leftdf ~~ dataframe to the left of the join
    rightdf ~~ dataframe to the right of the join
    join_field ~~ field the two dataframes are joined on
    join ~~ the way the dataframes are joined
    x ~~ future x axis of data frame
    y ~~ future y axis of the data frame

    Returns:
    dataframe ~~ returns merged and processed dataframe
    """
    # srtips spaces from the joining field
    leftdf[join_field] = leftdf[join_field].str.strip()
    rightdf[join_field] = rightdf[join_field].str.strip()
    # returns merged dataset
    df = pd.merge(leftdf, rightdf, how=join, on=join_field)
    # remove outliers > 3 stdev
    std_to_strip = 3
    df = df[np.abs(df[x]-df[x].mean()) <= (df[x].std()*std_to_strip)]
    df = df[np.abs(df[y]-df[y].mean()) <= (df[y].std()*std_to_strip)]
    return df


x_index = 'Sleep'
y_index = 'Scores'
df = process_data(scoresdf, sleepdf, 'ID', 'left', x_index, y_index)


def model_data(df, x_field, y_field):
    """
    Runs scilearn linear regression modeling to stdout the R-Squared and
    regression function

    Arguments:
    df ~~ datafield to analyze
    x_field ~~ field to index for x axis
    y_field ~~ field to index for y axist

    Returns:
    model ~~ returns linear regression model
    """
    # creates a 2d array
    x = df[[x_field]]
    y = df[[y_field]]
    # initialize and learn the regression
    model = LinearRegression()
    model.fit(x, y)
    # pull the confidence interval and best fit coeficients
    score = model.score(x, y)
    m = model.coef_[0][0]
    b = model.intercept_[0]
    print('R-squared: %f' % round(score, 3))
    print('y=%fx+%f' % (round(m, 3), round(b, 3)))
    return model


model = model_data(df, x_index, y_index)


def plot_data_and_model(model, x, y):
    """
    Plots scatterplot from lists and plots the bestfit

    Arguments:
    model ~~ sklearn linear regression model for the bestfit line
    x ~~ pandas series for the x axis of the scatter plot
    y ~~ pandas series for the y axis of the scatter plot

    """
    # add scatter plot of sleep hrs and scores
    plt.scatter(x, y, s=1)
    # create array of x,y cordinates for the best fit line
    xmap = np.linspace(np.min(x), np.max(x), num=len(x))
    ymap = model.predict(xmap.reshape(-1, 1))
    # create plot
    plt.plot(xmap, ymap, color='r')
    plt.xlabel('Sleep [HR]')
    plt.ylabel('Score [%]')
    plt.show()


plot_data_and_model(model, df[x_index], df[y_index])
