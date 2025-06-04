### main.py
import streamlit as st
from login import login
from zaehler import lese_zaehlerwert

# main.py
authenticated, username = True, "Hanni"  # Testweise immer eingeloggt


if authenticated:
    st.title("🔌 RS485 Zählerauslese")
    st.success(f"Willkommen {username}!")

    if st.button("Zähler auslesen"):
        wert = lese_zaehlerwert()
        st.metric("Zählerstand", f"{wert} kWh")
else:
    st.stop()
