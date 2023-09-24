import streamlit as st

st.set_page_config(
    page_title="py.EDU",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)
st.header(":blue[py]:red[EDU]:snake:")

if 'expandtitle' not in st.session_state:
    st.session_state.expandtitle = None







with st.sidebar:
    "Select:"
    if st.button("Home",use_container_width=True):
        st.session_state.expandtitle = "Home"

    with st.expander("Practice Tools"):
        if st.button("Flashcard Maker"):
            st.session_state.expandtitle = "Flashcards"
    with st.expander("Unit 1"):
        if st.button("Unit 1.1: Python Introduction"):
            st.session_state.expandtitle = "Unit 1.1"
        if st.button("Unit 1.2: Syntax and Formatting Conventions"):
            st.session_state.expandtitle = "Unit 1.2"
        if st.button("Unit 1.3: Variables"):
            st.session_state.expandtitle = "Unit 1.3"
        if st.button("Unit 1.4: Inputs and Outputs"):
            st.session_state.expandtitle = "Unit 1.4"
        if st.button("Unit 1.5: Summary"):
            st.session_state.expandtitle = "Unit 1.5"

    with st.expander("Unit 4"):
        if st.button("Unit 4.1"):
            st.session_state.expandtitle = "Unit 4.1"

if st.session_state.expandtitle == "Unit 1.1":
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
            "\tprint(\"Hello, World!\")", language='python')
    st.markdown("After writing your first program, choose which way you want to run it. If you are writing code in "
                "the terminal "
                "you would use the \"python3 hello_world.cpp\" command. Whatever way you run it, the result of the "
                "program should be:")
    st.code("Hello, World!", language='python')
    question1 = st.radio("What would hello_world.py output?", ("Hello, World!", "Hello, Python", "Hello", "Bye"),
                         index=None)
    if question1 == "Hello, World!":
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 1.2"
    elif question1 == "Hello, Python" or question1 == "Hello" or question1 == "Bye":
        st.markdown("Try Again!")


elif st.session_state.expandtitle == "Unit 1.2":
    st.header("Unit 1.2: Syntax and Formatting Conventions")
    st.divider()
    st.subheader("A Python file being formatted improperly or having inappropriately named components will cause it to "
                "not function.")
    st.divider()
    st.subheader("Syntax Errors")
    st.markdown("The most errors you will face as you program will be syntax errors. Even if your logic "
                "is sound, if you spell something incorrectly your program will not function. Computers are good at "
                "following instructions but mistakes as minor as writing rint(“Hello”) instead of print(“Hello”) will "
                "trip up the computer.")
    st.subheader("Indentation")
    st.markdown("Indentation indicates a line/block of code is related to the non-indented code directly above it. "
                "The following code will not work due to the unnecessary indent")
    st.code("print(\"“Hi.\")\n\tprint(\"Hi.\")", language='python')
    st.markdown("Ensure you include the correct spelling, spacing, indents, and within your code. Starting in unit 3 "
                "cases where indentation is required will appear.")
    question2 = st.radio("Which two print statements would output: Goodmorning!",
                         ("print(\"Goodmorning!\')", "print(Goodmorning!\")", "print(\"Goodmorning!\")", "print(\"Goodmorning!)"),
                         index=None,
                        )

    if (question2 == "print(\"Goodmorning!\")"):
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 1.3"
    elif question2 == "print(\"Goodmorning!\')" or question2 == "print(Goodmorning!\")" or question2 == "print(\"Goodmorning!)":
        st.markdown("Try Again!")





elif st.session_state.expandtitle == "Unit 1.3":
    st.header("Unit 1.3: Variables")
    # Add content for Unit 1.3

elif st.session_state.expandtitle == "Unit 1.4":
    st.header("Unit 1.4: Inputs and Outputs")
    # Add content for Unit 1.4

elif st.session_state.expandtitle == "Unit 1.5":
    st.header("Unit 1.5: Summary")
    # Add content for Unit 1.5

elif st.session_state.expandtitle == "Unit 4.1":
    st.header("Unit 4.1:")
    # Add content for Unit 4.1

elif st.session_state.expandtitle == "Cheatsheet":
    st.header("Cheatsheet")
    # Add content for Cheatsheet

elif st.session_state.expandtitle == "Flashcards":
    st.header("Flashcards")
    # Add content for Flashcards

elif st.session_state.expandtitle == "Home":
    st.header("Home")
    # Add content for Home
