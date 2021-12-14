import streamlit as st
import webbrowser

url = "https://www.streamlit.io/"

if st.button("🎈 Open streamlit.io in a new tab"):
    webbrowser.open_new_tab(url)
