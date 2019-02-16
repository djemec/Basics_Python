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
import unittest

d = '~/Documents/Python/Homework/data/'
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
# merge account and client via bridge
df = pd.merge(pd.merge(clientdf, bridgedf, how='outer', on='ClientID'
                       ), acctdf, how='outer', on='AccountID')
df_test_merge = df
#display(df.head())

def get_client_count(df, filter_col, filter_val, df_test=df_test_merge):
    """
    Evaluates dataframe to return the number of unique clients by the filter
    column and value.  Also performs test to validate accuracy

    Arguments:
    df ~~ Pandas dataframe containing ClientID and the column to filter
    filter_col ~~ column used to filter
    filter_val ~~ value filtered for

    Returns:
    unique_client ~~ integer representing occurance count
    """
    test_passed = True
    df = df[df[filter_col] == filter_val]
    df_filter = list(set(df['ClientID']))
    print('ClientID matching filter:' + str(df_filter))

    # Perform Positive Test & return pass / fail
    for c in df_filter:
        for f in list(filter_val):
            test_passed = not df_test[(df_test.AccountStatus == 'open') &
                          (df_test.AccountType == f) &
                          (df_test.ClientID == c)].empty
            if test_passed == False:
                break
    
    print('Positive Test Success: ' + str(test_passed))
    
    # Get Negative Set
    client_neg_test = clientdf[~clientdf.ClientID.isin(df_filter)]['ClientID']
    
    # Perform Negative Test & return pass / fail
    for c_n in client_neg_test:
        for f in list(filter_val):
            test_passed = df_test[(df_test.AccountStatus == 'open') &
                          (df_test.AccountType == f) &
                          (df_test.ClientID == c_n)].empty
            if test_passed == True:
                break
    print('Negative Test Success: ' + str(test_passed))
    
    
    
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

    display(df[['AccountID', 'AccountBalance', filter_col]].head())
    
    # Return Mean
    return df['AccountBalance'].mean()

df = process_data(df)
#display(df.head())

print('There are %d acct types(includes none)' % len(set(df['UniqueAcctKey'])))

# group by client and openUniqueAcctKey
df = process_data(df, 'open')
display(df.head())

# get clients with all 3 account types open: assuming df still only has open
print('There are %d clients with all 3 account types open currently' %
      get_client_count(df, 'openUniqueAcctKey', 'DLW'))

#print('The Mean acct balance for clients with 2 LL and a W account open is $%f'
#      % round(mean_balance_by_acct_type_filter(df, 'openUniqueAcctKeyRaw',
#                                               'LL', 'W'),3))
# display(df.head())
help(mean_balance_by_acct_type_filter)