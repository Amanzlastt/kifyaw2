import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def clean_data(df):
    """Takes dataframe and returns cleaned data"""
    df=df.dropna(subset=['Start', 'Start ms', 'End', 'End ms', "Bearer Id", "Avg Bearer TP DL (kbps)","Avg Bearer TP UL (kbps)", "Activity Duration DL (ms)",
                      "Activity Duration UL (ms)","Dur. (ms).1","Total UL (Bytes)","Total DL (Bytes)","IMEI", "Last Location Name" ])
    df=df.apply(lambda col: col.fillna(col.mean()) if col.dtype in ['float64', 'int64'] else col)
    return df



def top_handsets_plot(top_handsets):
    """Takes top handsets and plots barplot"""
    top_handsets.plot(kind='bar', color='skyblue', figsize=(10, 6))
    plt.title('Top 10 Handsets Used by Customers')
    plt.xlabel('Handset')
    plt.ylabel('Number of Users')
    plt.xticks(rotation=45, ha='right')
    return plt

def top_3_handsets_from_top_5(top_5_counts):
    """Takes top_5_counts and returns plot of Top 5 Handsets per Top 3 Manufacturers"""
    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=top_5_counts,
        x='Handset',
        y='Count',
        hue='Handset Manufacturer', dodge=False
    )
    plt.title('Top 5 Handsets per Top 3 Manufacturers')
    plt.xlabel('Handset')
    plt.ylabel('Number of Users')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Manufacturer')
    return plt

def hist(df_cleaned):
    plt.hist(df_cleaned['Total Data Volume'], bins=20, color='blue', alpha=0.7)
    plt.title('Distribution of Total Data Volume')
    plt.xlabel('Total Data Volume (Bytes)')
    plt.ylabel('Frequency')
    return plt


def boxplot(df_cleaned):
    # Example: Boxplot for session duration
    sns.boxplot(x=df_cleaned['Dur. (ms)'])
    plt.title('Boxplot of Session Duration')
    return plt

def heatmap(corr_matrics):
    sns.heatmap(corr_matrics, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Application Data')
    return plt

