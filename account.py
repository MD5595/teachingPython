import streamlit as st

def account():

    user_credentials = {}
    flag = True

    st.title("Account")

    if st.button("Sign Up"):
        create_credentials(user_credentials)

    if st.button("Login"):

        login()
        user_info = login()
        check_credentials(user_info[0], user_info[1], user_credentials)

        while flag:

            if check_credentials(user_info[0], user_info[1], user_credentials):
                st.success("Access granted")
                flag = False
            else:
                st.error("Access denied, Try Again")
                login()


def create_credentials(credentials):

    # Asks user for their info
    with st.form(key='Account Creation'):
        username = (st.text_input("Enter a username for your account: ", "Type here..."))
        password = (st.text_input("Enter a password for your account (8 characters or numbers): ", "Type here..."))
        st.form_submit_button("Sign Up!")
    # stores user info in dictionary and returns dictionary
    credentials[username] = password
    return credentials


def login():

    cred_list = []
    with st.form(key='Log-In'):
        username = (st.text_input("Enter the username for your account: ", "Type here..."))
        password = (st.text_input("Enter the password for your account: ", "Type here..."))
        st.form_submit_button("Log In!")

    cred_list.append(username)
    cred_list.append(password)

    return cred_list

def check_credentials(username, password, credentials):
    """
    Using dictionary of account information, checks to see if user exists
    when logging in
    """

    if username in credentials and (credentials[username] == password):
        return True
    elif (username in credentials) and (credentials[username] != password):
        st.warning("Incorrect password, try again.")
        return False
    elif username not in credentials:
        st.warning("Username incorrect, try again or Create Account.")
        return False

