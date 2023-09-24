import streamlit as st

def account_manager():
    # Define a dictionary to store usernames and passwords
    user_credentials = {
        "user1": "password1",
        "user2": "password2",
        "user3": "password3"
    }

    # Streamlit app title
    st.title("Simple Username/Password Authentication")

    # Streamlit sidebar for login and user creation
    with st.sidebar:
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        st.header("Create User")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        create_user = st.button("Create User")

    # Streamlit main content
    if st.sidebar.button("Login"):
        if username in user_credentials and user_credentials[username] == password:
            st.success("Access granted!")
        else:
            st.error("Access denied. Please check your username and password.")

    if create_user:
        create_new_user(new_username, new_password, user_credentials)

# Function to create a new user
def create_new_user(username, password, user_credentials):
    if username and password:
        user_credentials[username] = password
        st.success(f"User '{username}' has been created.")
    else:
        st.warning("Please provide both a username and a password for user creation.")




