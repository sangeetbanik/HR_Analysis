## Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

## Import the dataset
df = pd.read_csv(HR-Employee-Attrition.csv)

## Exploring the dataset
df.head()
df.info()

## Check for null values
df.isnull().sum()

## Check for duplicates
df.duplicated().sum()

## Analysing the statistics 
df.describe()
