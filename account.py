import streamlit as st

def account_manager():
    # Streamlit app title
    st.title("Simple Username/Password Authentication")

    # Function to create a new user
    def create_new_user(username, password):
        if "user_credentials" not in st.session_state:
            st.session_state.user_credentials = {}
        if username and password:
            if username not in st.session_state.user_credentials:
                st.session_state.user_credentials[username] = password
                st.success(f"User '{username}' has been created.")
            else:
                st.warning(f"User '{username}' already exists. Please choose a different username.")
        else:
            st.warning("Please provide both a username and a password for user creation.")

    # Input fields for creating a new user
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    create_user = st.button("Create User")

    # Input fields for login
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Streamlit main content
    if st.button("Login"):
        if "user_credentials" in st.session_state and username in st.session_state.user_credentials and st.session_state.user_credentials[username] == password:
            st.success("Access granted!")
        else:
            st.error("Access denied. Please check your username and password.")

    if create_user:
        create_new_user(new_username, new_password)


