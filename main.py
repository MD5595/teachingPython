import streamlit as st

st.set_page_config(page_title="py.EDU", page_icon=":snake:", layout="centered", initial_sidebar_state="auto",
                   menu_items=None)
title = None


with st.sidebar:
    "Select:"
    with st.expander("Unit 1"):
        if st.button("Unit 1.1: Python Introduction"):
            title = "Unit 1.1"
        if st.button("Unit 1.2: Installing Python"):
            title = "Unit 1.2"
        if st.button("Unit 1.3: Syntax and Formatting Conventions"):
            title = "Unit 1.3"
        if st.button("Unit 1.4: Variables"):
            title = "Unit 1.4"
        if st.button("Unit 1.5: Inputs and Outputs"):
            title = "Unit 1.5"
        if st.button("Unit 1.6: Summary"):
            title = "Unit 1.6"

    with st.expander("Unit 4"):
        if st.button("Unit 4.1"):
            title = "Unit 4.1"

if title == "Unit 1.1":
    st.header("Unit 1.1: Introduction to Python")
    st.divider()
elif title == "Unit 1.2":
    st.header("Unit 1.2: Installing Python")
elif title == "Unit 1.3":
    st.header("Unit 1.3: Syntax and Formatting Conventions")
elif title == "Unit 1.4":
    st.header("Unit 1.4: Variables")
elif title == "Unit 1.5":
    st.header("Unit 1.5: Inputs and Outputs")
elif title == "Unit 1.6":
    st.header("Unit 1.6: Summary")
elif title == "Unit 4.1":
    st.header("Unit 4.1: ")
else:
    st.header("Home")


