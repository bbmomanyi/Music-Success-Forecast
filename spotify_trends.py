#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 23:31:51 2023

@author: britney
"""



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the dataset
df = pd.read_csv("/Users/britney/Downloads/New Artist Success Forcast/BillboardFromLast20/spotifyWeeklyTop200Streams.csv")

# convert Week to datetime
df["Week"] = pd.to_datetime(df["Week"])

# set the style for the plots
sns.set_style("darkgrid")

# Top 10 most streamed songs by features
top10_features = df.groupby('Features')['Streams'].sum().sort_values(ascending=False)[:10]
plt.figure(figsize=(10,5))
plt.bar(top10_features.index, top10_features.values)
plt.xticks(rotation=90)
plt.title('Top 10 Most Streamed Songs by Features')
plt.ylabel('Streams (in billions)')
plt.show()


# Top 20 Songs with the Most Streams of All Time
top_songs = df.groupby(["Name", "Artist"], as_index=False)["Streams"].sum().sort_values(by="Streams", ascending=False).head(20)
plt.figure(figsize=(12, 8))
sns.barplot(x="Streams", y="Name", data=top_songs, palette="rocket")
plt.title("Top 20 Songs with the Most Streams of All Time")
plt.xlabel("Streams (in billions)")
plt.ylabel("Song Name")
plt.show()

# Top 20 Artists with the Most Streams of All Time
top_artists = df.groupby("Artist", as_index=False)["Streams"].sum().sort_values(by="Streams", ascending=False).head(20)
plt.figure(figsize=(12, 8))
sns.barplot(x="Streams", y="Artist", data=top_artists, palette="rocket")
plt.title("Top 20 Artists with the Most Streams of All Time")
plt.xlabel("Streams (in billions)")
plt.ylabel("Artist Name")
plt.show()

# Weekly Streams Over Time
weekly_streams = df.groupby("Week", as_index=False)["Streams"].sum()
plt.figure(figsize=(12, 8))
sns.lineplot(x="Week", y="Streams", data=weekly_streams, palette="rocket")
plt.title("Weekly Streams Over Time")
plt.xlabel("Week")
plt.ylabel("Streams (in billions)")
plt.show()

