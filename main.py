import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)



print("Libraries imported successfully!")


df = pd.read_csv("data/Sleep_Efficiency.csv")


print("Dataset shape:", df.shape)
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])



print(df.head())

print("Dataset information:")
df.info()

print("Statistical summary:")
print(df.describe())

print("Missing values:")
print(df.isnull().sum())