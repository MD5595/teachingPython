import streamlit as st
from PIL import Image

st.set_page_config(page_title="py.EDU", page_icon=":snake:", layout="wide", initial_sidebar_state="auto",
                   menu_items=None)
st.header(":blue[py]:red[EDU]:snake:")
expandtitle = None




with st.sidebar:
    "Select:"
    with st.expander("Unit 1"):
        if st.button("Unit 1.1: Python Introduction"):
            expandtitle = "Unit 1.1"
        if st.button("Unit 1.2: Syntax and Formatting Conventions"):
            expandtitle = "Unit 1.2"
        if st.button("Unit 1.3: Variables"):
            expandtitle = "Unit 1.3"
        if st.button("Unit 1.4: Inputs and Outputs"):
            expandtitle = "Unit 1.4"
        if st.button("Unit 1.5: Summary"):
            expandtitle = "Unit 1.5"

    with st.expander("Unit 4"):
        if st.button("Unit 4.1"):
            expandtitle = "Unit 4.1"

if expandtitle == "Unit 1.1":
    if st.button("Home"):
        expandtitle = "Cheatsheet"
    st.header("Unit 1.1: Introduction to Python")
    st.divider()
    st.markdown("In this introductory chapter, we'll take our first steps "
                "into the world of Python programming. Python is a versatile"
                " and beginner-friendly programming language known for its simplicity"
                " and readability. By the end of this chapter, you'll have written your"
                " first Python program and gained insight into the wide range of applications "
                "Python can be used for.")
    st.divider()
    st.subheader("Hello, Python!")
    st.markdown("In this section, we'll start with a classic \"Hello, World!\" program. This simple program" \
                "will introduce you to the basic structure of Python code and how to run it.")
    st.markdown("\t - We'll guide you through the process of writing your first Python program that displays \"Hello, "
                "World!\" on the screen.")
    st.markdown("To create a file, open any code editor (IDE or terminal) environment you have. Create a new Python "
                "file called \"hello_world.py\" In this file you will want to code the following, don't worry we will "
                "explain it later.")
    st.code("if __name__ == \"__main__\":\n"
            "\tprint(\"Hello, World\")", language='python')
    st.markdown("After writing your first program, choose which way you want to run it. If you are writing code in "
                "the terminal "
                "you would use the \"python3 hello_world.cpp\" command. Whatever way you run it, the result of the "
                "program should be:")


elif expandtitle == "Unit 1.2":
    st.header("Unit 1.2: Syntax and Formatting Conventions")
elif expandtitle == "Unit 1.3":
    st.header("Unit 1.3: Variables")
elif expandtitle == "Unit 1.4":
    st.header("Unit 1.4: Inputs and Outputs")
elif expandtitle == "Unit 1.5":
    st.header("Unit 1.5: Summary")
elif expandtitle == "Unit 4.1":
    st.header("Unit 4.1: ")
elif expandtitle == "Cheatsheet":
    st.header("Cheatsheet")
else:
    st.header("Home")
