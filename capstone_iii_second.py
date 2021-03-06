# -*- coding: utf-8 -*-
"""Capstone_III - second.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xVPginXDpcXMJHHXeZOkxcb1rW0nBpET

### **Data**
"""

#Link Gdrive
from google.colab import drive
drive.mount('/content/gdrive')

# Imports

import math    
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

"""Original Dataset - [World Happiness Report](https://www.kaggle.com/datasets/unsdsn/world-happiness)

"The happiness scores and rankings use data from the Gallup World Poll. The scores are based on answers to the main life evaluation question asked in the poll. This question, known as the Cantril ladder, asks respondents to think of a ladder with the best possible life for them being a 10 and the worst possible life being a 0 and to rate their own current lives on that scale. The scores are from nationally representative samples for the years 2013-2019 and use the Gallup weights to make the estimates representative. The columns following the happiness score estimate the extent to which each of six factors – economic production, social support, life expectancy, freedom, absence of corruption, and generosity – contribute to making life evaluations higher in each country than they are in Dystopia, a hypothetical country that has values equal to the world’s lowest national averages for each of the six factors. They have no impact on the total score reported for each country, but they do explain why some countries rank higher than others."
"""

#Bring in dataset file
happiness_df = pd.read_excel('/content/gdrive/My Drive/Colab Datasets/World Happiness Report 2019.xlsx')
happiness_df.head()

#descriptive statistics
happiness_df.describe()

"""### **Data** **Exploration**"""

#Any null values?
null_rows = happiness_df[happiness_df.isnull().any(axis=1)]
null_rows.head()
#No null values

#view of correlations between all columns
happiness_df.corr()

"""I'll focus on Happiness Score, GDP per capita, and social support

**Hypothesis 1:**

H₀: µ = µ₀ - There is no statistically significant difference between happiness scores of countries with a GDP per capita lower than average and countries with a GDP per capita higher than average.

Hₐ: µ ≠ µ₀ - There is a statistically significant difference between happiness scores of countries with a GDP per capita lower than average and countries with a GDP per capita higher than average.

**Hypothesis 2:**

H₀: µ = µ₀ - There is no statistically significant difference between happiness scores of countries with a social support score lower than average and countries with a social support score higher than average.

Hₐ: µ ≠ µ₀ - There is no statistically significant difference between happiness scores of countries with a social support score lower than average and countries with a social support score higher than average.
"""

#how is 'Score' distriuted? Histogram
sns.histplot(happiness_df['Score']);

#How is 'GDP per capita' distributed? Histogram
sns.histplot(happiness_df['GDP per capita']);

#How is 'Social support' distributed? Histogram
sns.histplot(happiness_df['Social support']);

#view of correlations between chosen variables
sns.pairplot(happiness_df, vars = ['Score', 'GDP per capita', 'Social support']);

"""### **Analysis**

### **Analysis - GDP**
"""

# Split the data for a t-test. lower GDP vs higher GDP. the mean being the cutoff point
low_gdp = happiness_df.loc[happiness_df['GDP per capita'] < 0.793883]
high_gdp = happiness_df.loc[happiness_df['GDP per capita'] > 0.793883]

#box plot of happiness score for lower gdp countries
sns.boxplot(y='Score', data=low_gdp);

#box plot of happiness score for higher gdp countries
sns.boxplot(y='Score', data=high_gdp);

# run a two sample t-test
stats.ttest_ind(low_gdp['Score'], high_gdp['Score'])

"""# The p-value is less than 0.05, so there **is** a statistically significant difference between the two samples. Therefore, we reject the null hypothesis.

### **Analysis - Social Support**
"""

# split the data for a t-test. lower social support vs higher social support. the mean being the cutoff point
high_social = happiness_df.loc[happiness_df['Social support'] > 1.208814]
low_social = happiness_df.loc[happiness_df['Social support'] < 1.208814]

#box plot of happiness score for lower social support countries
sns.boxplot(y='Score', data=low_social);

#box plot of happiness score for higher social support countries
sns.boxplot(y='Score', data=high_social);

# run a two sample t-test
stats.ttest_ind(low_social['Score'], high_social['Score'])

"""# The p-value is less than 0.05, so there **is** a statistically significant difference between the two samples. Therefore, we reject the null hypothesis.

## **The evidence shows that these two factors (GDP per capita and social support) play a significant role in a country's overall happiness score.**

## Recommendations: Conduct further research into the role these two factors play in overall happiness scores and how that impacts global development.
"""