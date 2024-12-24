import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

def top_bottom_frequent(df, column):
    """Takes data frame and  column name and returns a list of top_10, bottom_10, most_frequent values of the column"""
    top_10 = df[column].nlargest(10).to_list()
    bottom_10 = df[column].nsmallest(10).to_list()
    most_frequent = df[column].value_counts().head(10).index.to_list() 
    lists = [top_10, bottom_10, most_frequent]
    return lists

def avg_through_plot(handset_metrics):
    """Plot Average throughput per Handset"""
    plt.figure(figsize=(14, 6))
    sns.barplot(data=handset_metrics, x='Handset Type', y='Avg Throughput', color='skyblue')
    plt.xticks(rotation=90)
    plt.title('Average Throughput per Handset Type', fontsize=16)
    plt.ylabel('Average Throughput (kbps)')
    plt.xlabel('Handset Type')
    plt.tight_layout()
    return plt


def avg_retransmission_plot(handset_metrics):
    plt.figure(figsize=(14, 6))
    sns.barplot(data=handset_metrics, x='Handset Type', y='Avg TCP Retransmission', color='orange')
    plt.xticks(rotation=90)
    plt.title('Average TCP Retransmission per Handset Type', fontsize=16)
    plt.ylabel('Average TCP Retransmission (Bytes)')
    plt.xlabel('Handset Type')
    plt.tight_layout()
    return plt