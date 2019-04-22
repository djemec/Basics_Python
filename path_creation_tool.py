#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 19:13:59 2019

@author: domenjemec
"""
import pandas as pd
import numpy as np


df = pd.DataFrame({
        'child':('A', 'B', 'C', 'D', 'E', 'F','C','X', 'B','A','C','A'),
        'parent': ('', 'F', 'B', 'F', 'B', '','E','L','F','','E','E')
        })

path_ind = pd.DataFrame(columns=['parent','child', 'path']).set_index(['child','parent'])

def path_repo_search(parent, child):
    global path_ind
    if((child,parent) in path_ind.index):
        path = path_ind.loc[(child,parent),:]['path']
    else:
        path = ''
    return path


def getPath(rdf):
    global df
    global path_repo
    parent = rdf['parent']
    child = rdf['child']
    path = path_repo_search(parent, child)
    if(path == ''):
        path = child
        ori_p = parent
        while(parent != ''):
            path = parent + '/' + path
            ind = df[df['child'] == parent].parent
            if(ind.empty):
                parent = ''
            else:
                parent = ind.iloc[0]

        path_ind.loc[(child,ori_p), :] = path

    return path


def main():
    df['path'] = df.apply(getPath, axis=1)
    sort_df = df.sort_values('path')
    print(sort_df)

if __name__ == "__main__":
    main()
