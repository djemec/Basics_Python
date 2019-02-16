#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 11:54:04 2018

@author: domenjemec
@title: homework 3a
"""
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt

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
#
#print("Account table dimensions: ", acctdf.shape)
#print("Client table dimensions: ", clientdf.shape)
#print('Client-account bridge table dimensions: ', bridgedf.shape)

# number of clients
print('Total Unique Clients: %d' % len(set(clientdf['ClientID'])))

# number of clients in each reagion
region_client_df = clientdf.groupby(by='Region')['ClientID'].count()
display(region_client_df.head())

# plot gender
gender_client_df = clientdf.groupby(by='Gender'
                                    )['ClientID'].count().reset_index(
                                            name='Frequency')
display(gender_client_df.head())
gender_client_df.plot(x='Gender', y='Frequency', kind='bar')

# count opened/closed)
account_status = acctdf.groupby(by='AccountStatus'
                                )['AccountID'].count().reset_index(
                                        name='Frequency')
account_status['Percent'] = account_status['Frequency']/account_status[
        'Frequency'].sum()*100.
display(account_status.head())

perc_open_closed = account_status[
        account_status.AccountStatus.isin(('closed', 'open'))]['Percent'].sum()

print('Accounts open or closed is ' + str(round(perc_open_closed, 3)) + '%')
# ['Percent'].sum()

# percent D accounts closed
total_d = acctdf[acctdf['AccountType'] == 'D']
total_d_closed = total_d[total_d['AccountStatus'
                                 ] == 'closed']['AccountID'].count()

print('D Accounts Closed: %f' % round(total_d_closed/total_d['AccountID'
                                                             ].count()*100, 3))
