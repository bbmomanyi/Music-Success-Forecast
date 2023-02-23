#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 02:17:10 2023

@author: britney
"""

# used to run the success rates or all the artists in the dataset

import pandas as pd
from sklearn.linear_model import LinearRegression

# read the CSV file
df = pd.read_csv('artist_data.csv')

# create a linear regression model
model = LinearRegression()

# fit the model to the entire dataset
model.fit(df[['NumAlbums', 'NumSongs', 'SocialMediaFollowers']], df['Success'])

# make predictions for all artists in the dataset
predictions = model.predict(df[['NumAlbums', 'NumSongs', 'SocialMediaFollowers']])

# add the predictions to the dataframe
df['PredictedSuccess'] = predictions

# print the dataframe with the predicted success column
print(df)
