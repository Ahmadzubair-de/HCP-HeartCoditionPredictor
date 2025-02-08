# 🫀 Heart Condition Predictor (HCP) – V2  

**HCP (Heart Condition Predictor)** ist ein **KI-Modell**, das anhand von Nutzereingaben das **Herzinfarktrisiko in Prozent** berechnet.  
Es wurde mit **TensorFlow** und **scikit-learn** trainiert und kann einfach in andere Systeme integriert werden.  

---

## 📂 Projektstruktur  
📦 HCP
┣ 📂 Data # Enthält die Trainingsdaten (CSV-Datei)
┣ 📂 Models # Speichert das trainierte Modell
┣ 📂 Source # Enthält den Quellcode
┃ ┣ 📜 model.py
┃ ┣ 📜 predict.py
┃ ┣ 📜 train.py
┃ ┗ 📜 utils.py
┣ 📜 main.py # Startet die KI und nimmt Nutzereingaben an
┣ 📜 requirements.txt # Liste aller benötigten Bibliotheken

yaml
Kopieren
Bearbeiten
---

## ⚙️ Installation & Nutzung  

### 🔹 1. Umgebung einrichten & Abhängigkeiten installieren  
```bash
python -m venv venv  
source venv/bin/activate  # (Linux/macOS)  
venv\Scripts\activate  # (Windows)  
pip install -r requirements.txt  
🔹 2. Modell trainieren
bash
Kopieren
Bearbeiten
python -m source.train  
🔹 3. KI starten & testen
bash
Kopieren
Bearbeiten
python main.py  
✅ Das war’s – einfach, effizient & ready to use! 🚀