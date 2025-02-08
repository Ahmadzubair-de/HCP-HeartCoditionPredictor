import os
import numpy as np
from sklearn.model_selection import train_test_split
from .utils import load_data, preprocess_data, save_scaler
from .model import create_model
from sklearn.preprocessing import StandardScaler

def train_model():
    # Daten laden und vorbereiten
    df = load_data()
    X, y = preprocess_data(df)
    
    # Daten skalieren
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    save_scaler(scaler)
    
    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )
    
    # Modell erstellen und trainieren
    model = create_model(X_train.shape[1])
    model.fit(
        X_train,
        y_train,
        epochs=50,
        batch_size=32,
        validation_data=(X_test, y_test)
    )
    
    # Modell speichern
    os.makedirs('models', exist_ok=True)
    model.save('models/HCPv2.h5')
    print("🎉 Modell erfolgreich trainiert und gespeichert!")

if __name__ == "__main__":
    train_model()