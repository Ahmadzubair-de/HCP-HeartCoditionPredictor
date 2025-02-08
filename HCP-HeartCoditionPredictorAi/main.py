from src.predict import predict_probability

def get_user_input():
    """Sammelt Benutzereingaben und validiert sie"""
    inputs = [
        ("Alter (Gib dein Alter in Jahren an, z. B. 45)", int),
        ("Geschlecht (1 = männlich, 0 = weiblich)", int),
        ("Brustschmerztyp (1 = typ. Angina, 2 = atyp. Angina, 3 = nicht-anginöser Schmerz, 4 = kein Schmerz)", int),
        ("Blutdruck in Ruhe (mm Hg, z. B. 120 – dein Blutdruck im Ruhezustand)", int),
        ("Cholesterin (mg/dl – dein gesamtes Cholesterin im Blut, z. B. 200)", int),
        ("Blutzucker > 120 mg/dl? (1 = Ja, 0 = Nein – falls du es nicht weißt, wähle 0)", int),
        ("EKG-Ergebnisse (0 = normal, 1 = ST-T-Wellen-Abweichung, 2 = Hypertrophie im EKG)", int),
        ("Maximale Herzfrequenz erreicht (Wie hoch war deine höchste Herzfrequenz, z. B. 160?)", int),
        ("Angina durch Bewegung? (1 = Ja, 0 = Nein – bekommst du Brustschmerzen bei Anstrengung?)", int),
        ("ST Depression aufgrund der Belastung (Wert zwischen 0.0 und 6.0 – zeigt Sauerstoffmangel im Herzen)", float),
        ("Neigung des ST-Segments (1 = Aufwärts, 2 = Gerade, 3 = Abwärts – gemessen im EKG)", int),
        ("Anzahl der großen Blutgefäße (0–3 – Anzahl der sichtbaren Arterien im Angiogramm, NICHT alle Adern!)", int),
        ("Thalassemie (1 = Normal, 2 = Fehlerhafte Blutzellen, 3 = Schwere Blutkrankheit – falls unbekannt, wähle 1)", int)
    ]
    
    return [t(input(f"{prompt}: ")) for prompt, t in inputs]

def main():
    print("🏥 Herzinfarkt-Risiko-Analyse HCPv2 🏥\n")
    user_data = get_user_input()
    probability = predict_probability(user_data) 
    print(f"\n🩺 Ihre Herzinfarkt-Wahrscheinlichkeit beträgt: {probability}%")

if __name__ == "__main__":
    main()
