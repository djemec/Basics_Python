#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 11:54:04 2018

@author: domenjemec
@title: homework 3
"""
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels as sm

d = '~/Documents/Python/Basics_Python/Homework/data/'
acct = 'AccountTable.csv'
client = 'ClientTable.csv'
bridge = 'ClientAcctFact.csv'

# extract data
acctdf = pd.read_csv(d + acct)
clientdf = pd.read_csv(d + client)
bridgedf = pd.read_csv(d + bridge)


acctdf = pd.read_csv("data/AccountTable.csv")
clientdf = pd.read_csv('data/ClientTable.csv')
bridgedf = pd.read_csv('data/ClientAcctFact.csv')


display(acctdf.head())
display(clientdf.head())
display(bridgedf.head())


def process_data(dataframe, acct_sts_filter=''):
    """
    Generates a column on each row that represents all of the client's account
    types.  Applies a filter and creates a filter column if available

    Arguments:
    dataframe ~~ Pandas dataframe containing ClientID and AccountType to
    aggregate
    acct_sts_filter ~~ (optional) What status to filter the aggregate on

    Returns:
    dataframe ~~ Pandas dataframe that has the aggregated account types in
    a UniqueAcctKey<Filter> column
    """
    new_col = acct_sts_filter + 'UniqueAcctKey'

    # Apply Status Filter
    dataframe = dataframe[dataframe['AccountStatus'] == acct_sts_filter] if (
            acct_sts_filter != '') else dataframe

    # Creates a new dataframe with the client id and a list of the acct types
    c_acct_types = dataframe.groupby('ClientID').apply(
            lambda x: list(x.AccountType)).reset_index(name=new_col)
    
    # Creates a condensed sorted column of all account types 
    c_acct_types[new_col + 'Raw'] = c_acct_types[new_col].apply(
            lambda a: ''.join([x for x in sorted(a) if str(x) != 'nan']))

    # Condenses the account type list into a unique string. None=''
    c_acct_types[new_col] = c_acct_types[new_col].apply(
            lambda a: ''.join([x for x in sorted(set(a)) if str(x) != 'nan']))

    # Merge aggregated dataframe back to mamain dataframe
    dataframe = pd.merge(dataframe, c_acct_types, how='left', on='ClientID')

    return dataframe


def get_client_count(df, filter_col, filter_val):
    """
    Evaluates dataframe to return the number of unique clients by the filter
    column and value

    Arguments:
    df ~~ Pandas dataframe containing ClientID and the column to filter
    filter_col ~~ column used to filter
    filter_val ~~ value filtered for

    Returns:
    unique_client ~~ integer representing occurance count
    """
    df = df[df[filter_col] == filter_val]
    print(set(df['ClientID']))
    return len(set(df['ClientID']))


def mean_balance_by_acct_type_filter(df, filter_col, *filter_val):
    """
    Iteratively filters a dataframe based on the column and values then
    averages the AccountBalance

    Arguments:
    df ~~ Pandas dataframe containing AccountBalance and the column to filter
    filter_col ~~ column used to filter
    filter_val ~~ value filtered for

    Returns:
    mean_acct_balance ~~ float representing the mean account balance
    """
    # Iteratively Filter
    for f in filter_val:
        df = df[df[filter_col].apply(lambda a: f in a)]

    #display(df[['AccountID', 'AccountBalance', filter_col]].head())

    # Return Mean
    return df['AccountBalance'].mean()


# merge account and client via bridge
df = pd.merge(pd.merge(clientdf, bridgedf, how='outer', on='ClientID'
                       ), acctdf, how='outer', on='AccountID')
#display(df.head())

df = process_data(df)
#display(df.head())


# group by client and openUniqueAcctKey
#df = process_data(df, 'open')
#display(df.head())

# Generate dataframe with client, count product type, total $, deposit $

def aggregate_data(df, acctType):
    df['depositBalance'] =  (df.AccountType == acctType)* df.AccountBalance
    df = df.groupby(['ClientID','UniqueAcctKey','UniqueAcctKeyRaw'])[
            'depositBalance'].sum().reset_index(name='sumDepositBalance')
    df['ctAcctType'] = df['UniqueAcctKeyRaw'].str.len()
    df['ctUniqueAcctType'] = df['UniqueAcctKey'].str.len()
    
    display(df[['ClientID','sumDepositBalance','ctAcctType','ctUniqueAcctType']].head())
    return df

client_df = aggregate_data(df, 'D')
display(client_df.head())

x_index = 'ctAcctType'
y_index = 'sumDepositBalance'
client_df.plot.scatter(x_index,y_index)
print('R: %f' % client_df[x_index].corr(client_df[y_index]))


import statsmodels.formula.api as smf

reg = smf.ols('sumDepositBalance ~ ctAcctType', data=client_df).fit()
print(reg.summary())

