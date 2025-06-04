import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

def login():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    name = authenticator.login("Login", location="main")
    authentication_status = authenticator.authentication_status

    if authentication_status:
        authenticator.logout("Logout", "sidebar")
        return True, name
    elif authentication_status is False:
        st.error("Benutzername oder Passwort falsch")
    elif authentication_status is None:
        st.warning("Bitte einloggen")
    return False, None

