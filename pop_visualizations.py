#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:04:49 2023

@author: britney
"""

#pop genre vizualizations

## popularity distribution Plot
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df["popularity"], bins=20)
plt.xlabel("Popularity Score")
plt.title("Distribution of Popularity Scores for Top Pop Tracks")
plt.show()

## Realease Date Trend Plot
df["release_date"] = pd.to_datetime(df["release_date"])
df["year"] = df["release_date"].dt.year

year_counts = df["year"].value_counts().sort_index()
plt.plot(year_counts.index, year_counts.values)
plt.xlabel("Year")
plt.ylabel("Number of Top Tracks")
plt.title("Trend of Pop Track Releases by Year")
plt.show()

# Scatterplot showing the relationship between popularity and danceability
plt.figure(figsize=(10, 6))
sns.scatterplot(x="popularity", y="danceability", hue="artist_name", data=df)
plt.title("Popularity vs. Danceability")
plt.xlabel("Popularity")
plt.ylabel("Danceability")
plt.show()