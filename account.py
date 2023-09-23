import streamlit as st

def app():
    st.title('User login/signup')

    choice = st.selection("Login/Signup', {Login")

def create_credentials(credentials):
    # Asks user for their info
    username = (input("Enter a username for your account: "))
    password = (input("Enter a password for your account (8 characters or numbers): "))

    # stores user info in dictionary and returns dictionary
    credentials[username] = password
    return credentials


def login():

    cred_list = []
    username = "Enter your username: "
    password = "Enter your password: "

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
        print("Incorrect password, try again.")
        return False
    elif username not in credentials:
        print("Username incorrect, try again or Create Account.")
        return False


user_credentials = {}
flag = True
app()
create_credentials(user_credentials)
login()

while flag:

    if check_credentials(login[0], login[1], user_credentials):
        print("Access granted")
        flag = False
    else:
        login()


