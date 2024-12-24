import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def top_10(df,column):
    """takes dataframe and clumn name and returns top 10 of the given column using nlargest function""" 
    return df.nlargest(10,column) 



def cluster_summary_plot(cluster_summary):
    cluster_summary.plot(kind='bar', figsize=(12, 6))
    plt.title('Engagement Metrics by Cluster')
    plt.ylabel('Metric Value')
    plt.xticks(rotation=0)
    plt.legend(title='Metrics')
    return plt




def top_applications_plot(top_apps):
    """Takes top apps and returns plot of Top 3 Most Used Applications"""
    top_apps.plot(kind='bar', figsize=(10, 6))
    plt.title('Top 3 Most Used Applications')
    plt.ylabel('Total Traffic (Bytes)')
    return plt
    

def wcss_plot(wcss):
    plt.plot(range(1, 10), wcss)
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('WCSS')
    return plt