import streamlit as st

def account():

    user_credentials = {}

    st.title("Account")

    if st.button("Sign Up"):
        create_credentials(user_credentials)

    if st.button("Login"):

        login()
        user_info = login()
        check_credentials(user_info[0], user_info[1], user_credentials)

        #while flag:

        if check_credentials(user_info[0], user_info[1], user_credentials):
            st.success("Access granted")
            #flag = False
        else:
            st.error("Access denied, Try Again")
            login()


def create_credentials(credentials):

     #Asks user for their info
    with st.form('Account Creation'):
        username = (st.text_input("Enter a username for your account: "))
        password = (st.text_input("Enter a password for your account (8 characters or numbers): ", type="password"))
        st.form_submit_button("Sign Up!")

     #stores user info in dictionary and returns dictionary
    credentials[username] = password
    return credentials


def login():

    cred_list = []
    st.header('Log-In')
    the_username = (st.text_input("Username: "))
    the_password = (st.text_input("Password: ", type="password"))
    st.button("Log In!")

    cred_list.append(the_username)
    cred_list.append(the_password)

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

