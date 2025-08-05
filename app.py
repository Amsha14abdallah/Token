import streamlit as st
from auth import login_user, register_user
from utils import generate_token
from Databases import save_token, get_latest_token, get_token_history
st.sidebar.markdown("---")


if st.sidebar.button("🚪 Logout"):
    st.session_state.authenticated = False
    st.session_state.user = None
    st.rerun()
st.set_page_config(page_title="Electricity Token System", layout="centered")

menu = ["Login", "Sign Up"]
choice = st.sidebar.selectbox("Chagua", menu)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user = None

if choice == "Login":
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Ingia"):
        if login_user(username, password):
            st.success("Login imefanikiwa!")
            st.session_state.authenticated = True
            st.session_state.user = username
        else:
            st.error("Username au Password si sahihi.")

elif choice == "Sign Up":
    st.subheader("📝 Sajili akaunti")
    new_user = st.text_input("Tengeneza Username")
    new_pass = st.text_input("Weka Password", type="password")
    if st.button("Sajili"):
        if register_user(new_user, new_pass):
            st.success("Umefanikiwa kusajiliwa. Tafadhali login sasa.")
        else:
            st.error("Username tayari upo. Chagua mwingine.")

