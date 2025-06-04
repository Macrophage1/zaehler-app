import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

def login():
    st.write("Login-Funktion wurde aufgerufen")  # ← hier rein

    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    name = authenticator.login(location="main")

    if "authentication_status" in st.session_state:
        if st.session_state["authentication_status"]:
            authenticator.logout("Logout", "sidebar")
            st.write("Login erfolgreich!")  # Debug
            return True, name
        elif st.session_state["authentication_status"] is False:
            st.error("Benutzername oder Passwort falsch")
        elif st.session_state["authentication_status"] is None:
            st.warning("Bitte einloggen")

    st.write("Login fehlgeschlagen oder abgebrochen.")  # Debug
    return False, None
