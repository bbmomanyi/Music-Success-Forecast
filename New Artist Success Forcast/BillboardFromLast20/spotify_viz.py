#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 04:42:27 2023

@author: britney
"""
# spotify stats viz
import pandas as pd
import matplotlib.pyplot as plt

# Load the Spotify Top 200 Charts dataset
spotify = pd.read_csv('spotifyWeeklyTop200Streams.csv')

print(list(spotify.columns))

# Scatter plot of Streams vs Week for the top 20 artists
#top_artists = spotify.groupby('Artist').sum().sort_values('Streams', ascending=False).head(20)
#plt.scatter(top_artists['Week'], top_artists['Streams'])
#plt.xlabel('Week')
#plt.ylabel('Streams')
#plt.title('Top 20 Artists - Streams vs Week')

# Bar plot of average Streams per Artist
mean_streams = spotify.groupby('Artist')['Streams'].mean().sort_values(ascending=False).head(20)
plt.bar(mean_streams.index, mean_streams.values)
plt.xticks(rotation=90)
plt.xlabel('Artist')
plt.ylabel('Mean Streams')
plt.title('Top 20 Artists - Mean Streams')

# Box plot of Streams by Features
#spotify['Has_Features'] = spotify['Features'].notnull()
#plt.boxplot([spotify[spotify['Has_Features']==True]['Streams'], 
#             spotify[spotify['Has_Features']==False]['Streams']])
#plt.xticks([1, 2], ['With Features', 'Without Features'])
#plt.ylabel('Streams')
#plt.title('Streams by Features')

plt.show()
