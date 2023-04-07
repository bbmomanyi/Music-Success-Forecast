#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 08:57:28 2023

@author: britney
"""

## combining 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the "pop_data.csv" and "hip_hop_data.csv" files as separate dataframes
pop_data = pd.read_csv("pop_data.csv")
hip_hop_data = pd.read_csv("hip_hop_data.csv")

# Concatenate the two dataframes together into one dataframe called "combined_data"
combined_genre_data = pd.concat([pop_data, hip_hop_data], ignore_index=True)

# Print the combined dataframe to make sure it looks correct
print(combined_genre_data)

combined_genre_data.to_csv('combined_genre_data.csv', index=False)

plt.figure(figsize=(10, 6))
sns.scatterplot(x="popularity", y="danceability", hue="track_genre", data=combined_genre_data)
plt.title("Popularity vs. Danceability")
plt.xlabel("Popularity")
plt.ylabel("Danceability")
plt.show()


