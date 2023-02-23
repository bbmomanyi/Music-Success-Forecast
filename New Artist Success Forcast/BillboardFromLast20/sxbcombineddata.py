#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 04:06:34 2023

@author: britney
"""

import pandas as pd

# Load the Billboard Hot 100 dataset
billboard = pd.read_csv('billboardHot100_1999-2019.csv')

# Convert the date column to a datetime format
#billboard['date'] = pd.to_datetime(billboard['Week'])

# Load the Spotify Top 200 Charts dataset
spotify = pd.read_csv('spotifyWeeklyTop200Streams.csv')

# Convert the date column to a datetime format
#spotify['date'] = pd.to_datetime(spotify['Week'])

# Rename the "Artists" column to "Artist"
billboard = billboard.rename(columns={'Artists': 'Artist'})

# Combine the datasets based on the title, artist, and date columns
combined2 = pd.merge(billboard, spotify, on=['Name', 'Artist', 'Week'], how='inner')

# Drop any duplicate rows
combined2.drop_duplicates(inplace=True)

# Save the combined dataset to a CSV file
combined2.to_csv('combined2_dataset.csv', index=False)



