#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 02:50:07 2023

@author: britney
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
artist_df = pd.read_csv("/Users/britney/Downloads/New Artist Success Forcast/BillboardFromLast20/artistDf.csv")

# Scatter plot of Followers vs NumAlbums
sns.scatterplot(x="Followers", y="NumAlbums", data=artist_df)
plt.title("Followers vs NumAlbums")
# understand whether having more followers is correlated with a higher number of albums

# Bar chart of the count of artists by Gender
sns.countplot(x="Gender", data=artist_df)
plt.title("Count of artists by Gender")
# results show that more males than female artist appeared 
# on the billboard within 1999-2019

# Bar chart of the count of artists by Group.Solo
sns.countplot(x="Group.Solo", data=artist_df)
plt.title("Count of artists by Group/Solo")
# results: higher # of solo artists than groups

# Box plot of YearFirstAlbum by Gender
sns.boxplot(x="Gender", y="YearFirstAlbum", data=artist_df)
plt.title("YearFirstAlbum by Gender")
# female artists tend to relaease 1st album later than male artists
# suggests gender based differences in artists timing of their cateer

# Box plot of YearFirstAlbum by Group.Solo
sns.boxplot(x="Group.Solo", y="YearFirstAlbum", data=artist_df)
plt.title("YearFirstAlbum by Group/Solo")
# solo artists release albims later than groups
# wider range of years for solo artists than groups 

# Heatmap of correlation matrix
corr_matrix = artist_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation matrix")
# shows a possitive correlation between number of albums and followers 
# suggests larger follwing => more opportunities for an artist to release music and build their career