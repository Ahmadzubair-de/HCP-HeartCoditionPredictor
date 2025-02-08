import pandas as pd
from sklearn.preprocessing import StandardScaler
from joblib import dump, load

def load_data():
    """Lädt die Rohdaten aus der CSV-Datei"""
    return pd.read_csv('data/heart_disease.csv')

def preprocess_data(df):
    """Vorverarbeitung der Daten"""
    X = df.drop('target', axis=1)
    y = df['target']
    return X, y

def save_scaler(scaler):
    """Speichert den Scaler"""
    dump(scaler, 'models/scaler.joblib')

def load_scaler():
    """Lädt den gespeicherten Scaler"""
    return load('models/scaler.joblib')