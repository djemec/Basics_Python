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


#display(acctdf.head())
#display(clientdf.head())
#display(bridgedf.head())
#
#print("Account table dimensions: ", acctdf.shape)
#print("Client table dimensions: ", clientdf.shape)
#print('Client-account bridge table dimensions: ', bridgedf.shape)

# number of clients
print('Total Unique Clients: %d' % len(set(clientdf['ClientID'])))

# number of clients in each reagion
#region_client_df = clientdf.groupby(by = 'Region')['ClientID'].count().reset_index(name='count')
region_client_df = clientdf.groupby(by = 'Region')['ClientID'].count()
display(region_client_df.head())

#plot gender
gender_client_df = clientdf.groupby(by = 'Gender')['ClientID'].count().reset_index(name='Frequency')
display(gender_client_df.head())
gender_client_df.plot(x='Gender', y='Frequency', kind='bar')

#plt.hist(clientdf['Gender'],bins = set(clientdf['Gender']))
