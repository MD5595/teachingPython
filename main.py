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
    st.title("Variable Explanation App")


    st.write("""
    Variables are values or characters that are stored within a phrase. Some of the data types that variables can store are strings (any characters placed within “ “), integers (any whole number), and floats (numbers with decimal places).

    Making a variable and giving it a value is called variable declaration. Some examples are shown below:
    """)
    st.code("A = 28\nMy_name = 'John'\nNumber1 = 1\n_car_ = 'F-150'", language='python')

    st.write("""
    Note the use of an equal sign to assign values to the variables. In Unit 3.1 we will go over Python’s equal symbol.

    By using variables we can label information using names that allow code to be clear.
    """)


    st.write("""
    Below is the code for a program.
    """)
    st.code(
        "import random\n"
        "\n"
        "num1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])\n"
        "animal = random.choice(['Cow', 'Pig', 'Sheep', 'Dog', 'Whale'])\n"
        "\n"
        "your_random_password = str(animal) + str(num1)\n"
        "print(your_random_password)",
        language='python'
    )

    st.write("""
    Even if you don’t understand some parts such as random.choice and str(), you can reasonably figure out that this is the code for a random password generator. As you progress through this course you will find out that it is not hard to get lost when overlooking code you are currently working on. By having appropriately named variables you will reduce the time you spend rereading your code to regain understanding of it.
    """)

    st.write("""
    Below is the same code but with non-descriptive names.
    """)
    st.code(
        "import random\n"
        "\n"
        "dwq = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])\n"
        "ejd = random.choice(['Cow', 'Pig', 'Sheep', 'Dog', 'Whale'])\n"
        "\n"
        "qua = str(ejd) + str(dwq)\n"
        "print(qua)",
        language='python'
    )

    st.write("""
    As you can see, this code is much harder to understand compared to its descriptive version.
    """)


    st.write("""
    There are some rules tied with variable naming.
    """)
    st.write("**Variable Naming Rules:**")
    st.write("- Variables must start with a letter or underscore.")
    st.write("- Variables can only contain the letters/symbols A-Z, 0-9, and _.")
    st.write("- Variables with different capitalization are different, even if the spelling is the same.")
    st.write("- When making a variable that holds a word, ' ' must be used.")
    st.write("- Variables cannot have the same name as keywords.")


    st.write("""
    Some examples of incorrect variable names, along with reasoning as to why the code is incorrect.
    """)
    st.code(" #A non-letter/underscore character is at the front of the variable name", language='python')
    st.code("", language='python')
    st.code("", language='python')
    st.code("", language='python')

    st.write(" Making your variables descriptive is vital to creating readable code that is easily decipherable.")

elif st.session_state.expandtitle == "Unit 1.4":
    st.header("Unit 1.4: Inputs and Outputs")
    # Add content for Unit 1.4

elif st.session_state.expandtitle == "Unit 1.5":
    st.header("Unit 1.5: Summary")
    # Add content for Unit 1.5

elif st.session_state.expandtitle == "Unit 2.1":
    st.title("Mathematical Operators Explanation")

    # Explanation of mathematical operators
    st.write("""
    Mathematical symbols, which are operators, are used in Python equations.
    Here are some basic math operators:

    - Addition (+)
    - Subtraction (-)
    - Multiplication (*)
    - Division (/)
    - Remainder (%): The left number after division
    - Exponents (**): The base is placed to the left of the symbol while the power is to the right
    - Floor Division (//): Removes any decimals produced from the division
    """)

    # Examples of using mathematical operators
    st.write("""
    When you want to display the solution to a math problem, you can either assign it to a variable and then print it, directly place the equation in a print statement, or place an equation using variables inside a print statement.
    """)
    num1 = 10 % 3
    num2 = 3 ** 2
    num3 = 5 // 2
    num4 = 2
    num5 = 14

    st.write(f"num1 = {num1}")
    st.write(f"num2 = {num2}")
    st.write(f"num3 = {num3}")
    st.write(f"3 // 10 = {3 // 10}")
    st.write(f"num4 / num5 = {num4 / num5}")


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
