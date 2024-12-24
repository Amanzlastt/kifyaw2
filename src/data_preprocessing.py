import pandas as pd 
import numpy as np

def load_data(path):
    return pd.read_csv(path)

# Function to replace missing values and outliers
def preprocess_column(column):
    """Takes coulumn of a dataframe and returns filters data using interquartile ranges"""
    # Replace missing values with mean (for numeric) or mode (for categorical)
    if column.dtype == 'float64' or column.dtype == 'int64':
        column.fillna(column.mean(), inplace=True)
        # Identify outliers using the IQR method
        Q1 = column.quantile(0.25)
        Q3 = column.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        column.clip(lower_bound, upper_bound, inplace=True)  # Replace outliers
    else:
        column.fillna(column.mode()[0], inplace=True)  # Replace missing with mode


