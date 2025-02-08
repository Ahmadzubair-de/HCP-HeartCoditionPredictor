import numpy as np
import tensorflow as tf
from .utils import load_scaler

def load_model():
    """Lädt das trainierte HCPv2-Modell"""
    return tf.keras.models.load_model('models/HCPv2.h5')

def predict_probability(user_data):
    """Gibt die Herzinfarktwahrscheinlichkeit in Prozent zurück"""
    model = load_model()
    scaler = load_scaler()
    
    # Daten skalieren und Vorhersage machen
    scaled_data = scaler.transform([user_data])
    probability = model.predict(scaled_data, verbose=0)[0][0]
    return round(probability * 100, 2)