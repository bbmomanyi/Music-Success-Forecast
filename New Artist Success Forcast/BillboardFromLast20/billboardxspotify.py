#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 04:20:43 2023

@author: britney
"""

import pandas as pd
import seaborn as sns

# Load the combined dataset
combined = pd.read_csv('combined_dataset.csv')

# Calculate the correlation matrix
corr_matrix = combined.corr()

# Visualize the correlation matrix using a heatmap
#sns.heatmap(corr_matrix, cmap='coolwarm', annot=True)

# Create a scatter plot of Streams vs. Weekly.rank
sns.scatterplot(x='Streams', y='Weekly.rank', data=combined)

# Create a box plot of Peak.position by Genre
sns.boxplot(x='Peak.position', y='Genre', data=combined)

# Create a line plot of Weeks.on.chart over time
sns.lineplot(x='Date', y='Weeks.on.chart', data=combined)