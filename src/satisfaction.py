import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def calculate_distance(point, centroid):
    """Calculate Euclidean distance between a point and a centroid."""
    return np.sqrt(np.sum((point - centroid) ** 2))

