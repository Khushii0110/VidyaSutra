# vidya.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

class VidyaSutra:
    def __init__(self):
        pass
    
    def read_csv(self, file_path):
        return pd.read_csv(file_path)
    
    def train_test_split(self, X, y, test_size=0.2, random_state=None):
        return train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    def standard_scaler(self):
        return StandardScaler()
    
    def random_forest_classifier(self, *args, **kwargs):
        return RandomForestClassifier(*args, **kwargs)

