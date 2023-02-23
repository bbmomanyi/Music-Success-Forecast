#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:39:14 2023

@author: britney
"""

#created dataset with chosen artist 
#(sample existing artists)
import pandas as pd

# create the dataset
data = {
    'Artist': ['Ariana Grande', 'Billie Eilish', 'BTS', 'Dua Lipa', 'The Weeknd'],
    'NumAlbums': [6, 1, 4, 2, 10],
    'NumSongs': [92, 32, 66, 45, 105],
    'SocialMediaFollowers': [232000000, 98500000, 32000000, 14100000, 24000000],
    'Success': [0.95, 0.9, 0.85, 0.8, 0.9]
}

# create a dataframe from the data
df = pd.DataFrame(data)

# save the dataframe as a CSV file
df.to_csv('artist_data.csv', index=False)

# read the CSV file back in
df = pd.read_csv('artist_data.csv')

# print the dataframe
print(df)

