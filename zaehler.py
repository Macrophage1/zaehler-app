### zaehler.py
import random

def lese_zaehlerwert():
    # Hier würde die echte RS485-Abfrage stehen, z. B. mit pymodbus
    # Simuliert einen Verbrauchswert
    return round(random.uniform(1234.5, 1250.0), 2)