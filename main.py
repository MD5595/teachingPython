import streamlit as st
import math
import random
from account import account_manager


st.set_page_config(
    page_title="EDUpy",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)
st.header(":blue[EDU]:red[py]:snake:")


if 'expandtitle' not in st.session_state:
    st.session_state.expandtitle = "Home"





with st.sidebar:


    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    with col1:
        if st.button(":house:"):
            st.session_state.expandtitle = "Home"
    with col2:
        if st.button("1"):
            st.session_state.expandtitle = "Unit 1.1"
    with col3:
        if st.button("2"):
            st.session_state.expandtitle = "Unit 2.1"
    with col4:
        if st.button("3"):
            st.session_state.expandtitle = "Unit 3.1"
    with col5:
        if st.button("4"):
            st.session_state.expandtitle = "Unit 4.1"
    with col6:
        if st.button("5"):
            st.session_state.expandtitle = "Unit 5.1"
    with col7:
        if st.button("6"):
            st.session_state.expandtitle = "Unit 6.1"
    with col8:
        if st.button("F"):
            st.session_state.expandtitle = "Unit 7.1"
    account_manager()

    "Select:"
    if st.button("Home",use_container_width=True):
        st.session_state.expandtitle = "Home"

    with st.expander("Practice Tools"):
        if st.button("Flashcard Maker", use_container_width=True):
            st.session_state.expandtitle = "Flashcards"
    with st.expander("Unit 1"):
        if st.button("Unit 1.1: Python Introduction", use_container_width=True):
            st.session_state.expandtitle = "Unit 1.1"
        if st.button("Unit 1.2: Syntax and Formatting Conventions", use_container_width=True):
            st.session_state.expandtitle = "Unit 1.2"
        if st.button("Unit 1.3: Variables", use_container_width=True):
            st.session_state.expandtitle = "Unit 1.3"
        if st.button("Unit 1.4: Inputs and Outputs", use_container_width=True):
            st.session_state.expandtitle = "Unit 1.4"
        if st.button("Unit 1 Summary", use_container_width=True):
            st.session_state.expandtitle = "Unit 1.5"
        if st.button("Unit 1 Quiz", use_container_width=True):
            st.session_state.expandtitle = "Unit 1.6"
    with st.expander("Unit 2"):
        if st.button("Unit 2.1: Basic Symbols", use_container_width=True):
            st.session_state.expandtitle = "Unit 2.1"
        if st.button("Unit 2.2: Order of Operations", use_container_width=True):
            st.session_state.expandtitle = "Unit 2.2"
        if st.button("Unit 2.3: Modulo", use_container_width=True):
            st.session_state.expandtitle = "Unit 2.3"
        if st.button("Unit 2 Summary", use_container_width=True):
            st.session_state.expandtitle = "Unit 2.4"
        if st.button("Unit 2 Quiz", use_container_width=True):
            st.session_state.expandtitle = "Unit 2.5"
    with st.expander("Unit 3"):
        if st.button("Unit 3.1: If Statements", use_container_width=True):
            st.session_state.expandtitle = "Unit 3.1"
        if st.button("Unit 3.2: Else Statements", use_container_width=True):
            st.session_state.expandtitle = "Unit 3.2"
        if st.button("Unit 3.3: Nested Conditionals", use_container_width=True):
            st.session_state.expandtitle = "Unit 3.3"
        if st.button("Unit 3 Summary", use_container_width=True):
            st.session_state.expandtitle = "Unit 3.4"
        if st.button("Unit 3 quiz", use_container_width=True):
            st.session_state.expandtitle = "Unit 3.5"
    with st.expander("Unit 4"):
        if st.button("Unit 4.1: For-Loops", use_container_width=True):
            st.session_state.expandtitle = "Unit 4.1"
        if st.button("Unit 4.2: While Loops", use_container_width=True):
            st.session_state.expandtitle = "Unit 4.2"
        if st.button("Unit 4.3: Nested Loops", use_container_width=True):
            st.session_state.expandtitle = "Unit 4.3"
        if st.button("Unit 4 Summary", use_container_width=True):
            st.session_state.expandtitle = "Unit 4.4"
        if st.button("Unit 4 Quiz", use_container_width=True):
            st.session_state.expandtitle = "Unit 4.5"
    with st.expander("Unit 5"):
        if st.button("Unit 5.1: Lists", use_container_width=True):
            st.session_state.expandtitle = "Unit 5.1"
        if st.button("Unit 5.2: Traversing Through Lists", use_container_width=True):
            st.session_state.expandtitle = "Unit 5.2"
        if st.button("Unit 5.3: Appending/Removing", use_container_width=True):
            st.session_state.expandtitle = "Unit 5.3"
        if st.button("Unit 5.4: 2D-Lists", use_container_width=True):
            st.session_state.expandtitle = "Unit 5.4"
        if st.button("Unit 5 Summary", use_container_width=True):
            st.session_state.expandtitle = "Unit 5.5"
        if st.button("Unit 5 quiz", use_container_width=True):
            st.session_state.expandtitle = "Unit 5.6"
    with st.expander("Unit 6"):
        if st.button("Unit 6.1: Function Declaration", use_container_width=True):
            st.session_state.expandtitle = "Unit 6.1"
        if st.button("Unit 6.2: Parameters", use_container_width=True):
            st.session_state.expandtitle = "Unit 6.2"
        if st.button("Unit 6.3: Returning Values in Functions", use_container_width=True):
            st.session_state.expandtitle = "Unit 6.3"
        if st.button("Unit 6 Summary", use_container_width=True):
            st.session_state.expandtitle = "Unit 6.4"
        if st.button("Unit 6 Quiz", use_container_width=True):
            st.session_state.expandtitle = "Unit 6.5"
    with st.expander("Finals"):
        if st.button("Recap", use_container_width=True):
            st.session_state.expandtitle = "Unit 7.1"
        if st.button("Final Exam", use_container_width=True):
            st.session_state.expandtitle = "Unit 7.2"
        if st.button("Final Project", use_container_width=True):
            st.session_state.expandtitle = "Unit 7.3"




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
    st.title("Unit 1.3: Variable Explanation App")

    # Explanations
    st.write("""
    Variables are values or characters that are stored within a phrase. Some of the data types that variables can store are strings (any characters placed within “ “), integers (any whole number), and floats (numbers with decimal places).

    Making a variable and giving it a value is called variable declaration. Some examples are shown below:
    """)
    st.code("A = 28\nMy_name = 'John'\nNumber1 = 1\n_car_ = 'F-150'", language='python')

    st.write("""
    Note the use of an equal sign to assign values to the variables. In Unit 3.1 we will go over Python’s equal symbol.

    By using variables we can label information using names that allow code to be clear.
    """)

    # Code for a program
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

    # Code with non-descriptive names
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

    # Variable naming rules
    st.write("""
    There are some rules tied with variable naming.
    """)
    st.write("**Variable Naming Rules:**")
    st.write("- Variables must start with a letter or underscore.")
    st.write("- Variables can only contain the letters/symbols A-Z, 0-9, and _.")
    st.write("- Variables with different capitalization are different, even if the spelling is the same.")
    st.write("- When making a variable that holds a word, ' ' must be used.")
    st.write("- Variables cannot have the same name as keywords.")

    # Examples of incorrect variable names
    st.write("""
    Some examples of incorrect variable names, along with reasoning as to why the code is incorrect.
    """)
    st.code("", language='python')
    st.code("", language='python')
    st.code("", language='python')
    st.code("", language='python')

    st.write("""
    Making your variables descriptive is vital to creating readable code that is easily decipherable.
    """)
 #Question for 1.3
    question3 = st.radio("What would hello_world.py output?", ("variable = 42", "42 = variable", "variable == 42", "variable: 42"),
                         index=None, key="q3")
    if question3 == "variable = 42":
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 1.4"
    elif question3 == "42 = variable" or question3 == "variable == 42" or question3 == "variable: 42":
        st.markdown("Try Again!")





elif st.session_state.expandtitle == "Unit 1.4":
    st.header("Unit 1.4: Inputs and Outputs")
    st.divider()
    st.subheader("Printing Variables")
    st.markdown("As Unit 1.1 showed, code you write can be displayed on the console by utilizing print() functions.")
    st.markdown("If you want to print a number or the contents of a variable, you simply place the number/variable "
                "inside the parentheses as shown below.")
    st.code("Name = \"Jesse\"\n"
            "print(Name)\n"
            "print(16)", language='python')
    st.markdown("Output:")
    st.code("Jesse\n"
            "16", language='python')

    st.subheader("Printing Statements")
    st.markdown("When printing a statement, you surround your text with quotation marks.")
    st.code("print(\"Hello, it’s nice to meet you.\")", language='python')
    st.markdown("Output:")
    st.code("Hello, it’s nice to meet you.", language='python')

    st.subheader("User Inputs")
    st.markdown("Oftentimes, you will be required to make your programs interactive. This will be done by utilizing "
                "the input() function. A variable will be assigned the text that the user inputs.")
    st.code("Age = input(\"Input your age: \")\n"
            "print(\"You are \" + Age)", language='python')
    st.markdown("Example:")
    st.code("Input your age: 17\n"
            "You are 17", language='python')

    st.subheader("Working with Numeric Inputs")
    st.markdown("Inputs are automatically seen as words/text. In order to have an input that’s a number be seen as "
                "one by the computer, which would allow the variable the input is assigned to partake in math "
                "equations, the int() function must be used.")
    st.code("Age = int(input(\"Input your age: \"))\n"
            "Age_plus_ten = Age + 10\n"
            "print(\"You will be \" + str(Age_plus_ten) + \" in 10 years.\")", language='python')
    st.markdown("Example:")
    st.code("Input your age: 17\n"
            "You will be 27 in 10 years.", language='python')
    question3 = st.radio("What is the purpose of the str() function in the last example?",
                         ("Converts the Age variable to an integer",
                          "Converts the Age_plus_ten variable to an integer",
                          "Converts the result of the Age_plus_ten expression to a string",
                          "Converts the Age_plus_ten variable to a string"),
                         index=None,
                         key="q3"
                         )

    if (question3 == "Converts the result of the Age_plus_ten expression to a string"):
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 1.5"
    elif(question3 == "Converts the Age variable to an integer"
    or question3 == "Converts the Age_plus_ten variable to an integer"
    or question3 == "Converts the Age_plus_ten variable to a string"):
        st.markdown("Try Again!")

elif st.session_state.expandtitle == "Unit 1.5":
    st.header("Unit 1 Summary")
    st.title("Data Types Explanation")

    # Create a 2x4 table to display data types
    st.write("""
    | Data Type | Description      |
    |-----------|------------------|
    | String    | Text type        |
    | Integer   | Number type      |
    | Float     | Number type      |
    | List      | Sequence type    |
    | Boolean   | Boolean type     |
    """)

    # Explanation of data types
    st.write("""
    In some programming languages, you must specify the data type of a variable when you declare it. However, in Python, the data type is automatically determined based on the value you assign to the variable.

    Here are all the data types that this course will go over:
    - **String**: Text type
    - **Integer**, **Float**: Number type
    - **List**: Sequence type
    - **Boolean**: Boolean type
    """)

    # Examples of data types
    st.write("Below are some examples:")
    st.code("Tree = 'Oak'", language='python')
    st.code("Number1 = 13", language='python')
    st.code("Float1 = 3.14", language='python')
    st.code("List1 = ['Iphone', 'Android', 'Google Pixel']", language='python')
    st.code("Boolean1 = 3 > 8", language='python')

    st.write("""
    Different data types can be used in different statements. For example, integers, floats, and strings can be added to variables of the same data type, but booleans can't. Also, you can only use the modulus operator with the int and float data types.
    """)
elif st.session_state.expandtitle == "Unit 1.6":

    st.title("Unit 1 Quiz")

    # Question 1
    q1 = st.radio("If x = 3 and y = 5. A variable result is made that aims to find the product of the two, how would it be done?",
                  ("3 * 5",
                   "result = x * y",
                   "print(\"3 * 5\"",
                   "result = 3 * 5"),
                  index=None
                  )

    if q1 == "result = x * y":
        st.markdown("Correct!")

        # Question 2
        q2 = st.radio("What is the primary purpose of a python variable?",
                      ("To store and manipulate data",
                       "To display text on the screen",
                       "To convert numbers to strings",
                       "To create comments"),
                      index=None
                      )
        if q2 == "To store and manipulate data":
            st.markdown("Correct!")
            # Question 3
            q3 = st.radio("In Python, what does the if statement do?",
                          ("It defines a function",
                           "It performs mathematical calculations",
                           "It controls the flow of a program based on a condition",
                           "It converts text to lowercase"),
                          index=None
                          )
            if q3 == "It controls the flow of a program based on a condition":
                st.markdown("Correct!")

                # Question 4
                q4 = st.radio("What does 'print()' do in Python?",
                              ("It converts text to uppercase",
                               "It converts text to lowercase",
                               "It displays output on the screen",
                               "It converts numbers to strings"),
                              index=None
                              )
                if q4 == "It displays output on the screen":
                    st.markdown("Correct!")

                    # Question 5
                    q5 = st.radio("What is the purpose of the 'input()' function in Python?",
                                  ("To convert text to uppercase",
                                   "To accept user input",
                                   "To display text on the screen",
                                   "To convert numbers to strings"),
                                  index=None
                                  )
                    if q5 == "To accept user input":
                        st.markdown("Correct!")

                        # Question 6
                        q6 = st.radio("What is the result of '3 + 5' in Python?",
                                      ("2", "7", "8", "15"),
                                      index=None
                                      )
                        if q6 == "8":
                            st.markdown("Correct!")

                            # Question 7
                            q7 = st.radio("Which of the following is not a valid Python comment?",
                                          ("# This is a comment", "// This is a comment",
                                           "''' This is a comment '''", '"This is a comment"'),
                                          index=None
                                          )
                            if q7 == "// This is a comment":
                                st.markdown("Correct!")

                                # Question 8
                                q8 = st.radio("Which symbol is used for exponentiation in Python?",
                                              ("^", "//", "**", "pwr()"),
                                              index=None
                                              )
                                if q8 == "**":
                                    st.markdown("Correct!")

                                    # Question 9
                                    q9 = st.radio("What is the output of 'print(10 // 3)' in Python?",
                                                  ("3", "3.33", "3.0", "33"),
                                                  index=None
                                                  )
                                    if q9 == "3":
                                        st.markdown("Correct!")

                                        # Question 10
                                        q10 = st.radio("What is the purpose of the 'int()' function in Python?",
                                                       ("To convert text to uppercase",
                                                        "To accept user input",
                                                        "To convert numbers to strings",
                                                        "To convert a value to an integer"),
                                                       index=None
                                                       )
                                        if q10 == "To convert a value to an integer":
                                            st.markdown("Correct!")
                                            if st.button("Next Section!"):
                                                st.session_state.expandtitle = "Unit 2.1"

                                        elif(q10 == "To convert text to uppercase"
                                        or q10 == "To accept user input"
                                        or q10 == "To convert a value to an integer"):
                                            st.markdown("Try Again!")
                                    elif(q9 == "3.33"
                                    or q9 == "3.0"
                                    or q9 == "33"):
                                        st.markdown("Try Again!")
                                elif(q8 == "^"
                                or q8 == "//"
                                or q8 == "pwr()"):
                                    st.markdown("Try Again!")
                            elif(q7 == "# This is a comment"
                            or q7 == "''' This is a comment '''"
                            or q7 == "\"This is a comment\""):
                                st.markdown("Try Again!")
                        elif(q6 == "2"
                        or q6 == "7"
                        or q6 == "15"):
                            st.markdown("Try Again!")
                    elif(q5 == "To convert text to uppercase"
                    or q5 == "To display text on the screen"
                    or q5 == "To convert numbers to strings"):
                        st.markdown("Try Again!")
                elif(q4 == "It converts text to uppercase"
                or q4 == "It converts text to lowercase"
                or q4 == "It converts numbers to strings"):
                    st.markdown("Try Again!")
            elif(q3 == "It defines a function"
            or q3 == "It performs mathematical calculations"
            or q3 == "It converts text to lowercase"):
                st.markdown("Try Again!")
        elif(q2 == "To display text on the screen"
        or q2 == "To convert numbers to strings"
        or q2 == "To create comments"):
            st.markdown("Try Again!")
    elif(q1 == "3 * 5"
    or q1 == "print(\"3 * 5\""
    or q1 == "result = 3 * 5"):
        st.markdown("Try Again!")




elif st.session_state.expandtitle == "Unit 2.1":
    st.title("Unit 2.1: Basic Symbols")

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
elif st.session_state.expandtitle == "Unit 2.2":
    # Title of the web app
    st.title("Unit 2.2: Order of Operations in Python")

    # Explanation of the order of operations
    st.write("""
    Whenever a Python program has multiple operators in one line, different parts of the equation will be solved in a specific order.

    Below is the order in which Python operations are processed:
    1. ()
    2. **
    3. *, /, //, %
    4. +, -

    Once all operators left have the same precedence, the equation will be solved from left to right.

    Let's look at the order of operations in action:
    """)
    equation = "X = 3*6+3*(6/2)+2**2"
    st.code(equation, language='python')
    st.write("print(X)")

    # Example calculation
    X = 3 * 6 + 3 * (6 / 2) + 2 ** 2
    st.write(f"X = {X}")

    # Explanation of the calculation
    st.write("""
    The equation is solved as follows:
    1. (6/2) = 3
    2. 2**2 = 4
    3. 3*6 = 18
    4. 3*3 = 9
    5. 18+9 = 27
    6. 27+4 = 31

    Python does basic math in the same order you would do on paper.
    """)

elif st.session_state.expandtitle == "Unit 2.3":
    st.title("Modules Explanation")

    # Explanation of modules
    st.write("""
    Modules are used to shorten programs by giving the user access to a group of functions. Generally, functions are given a number/text and return a value.

    The two modules this course will have you use are the `math` and `random` modules. To use them, they first have to be imported, then the specific function you want to use has to be called using dot notation. You call a function from a module by saying `module.function`.

    Here are the math functions you will use:
    """)
    st.code("import math\n"
            "X = 2.1\n"
            "Y = 3\n"
            "\n"
            "Num1 = math.ceil(X)  # Rounds X up\n"
            "Num2 = math.fabs(X)  # Returns the absolute value of X\n"
            "Num3 = math.floor(X)  # Returns X rounded down\n"
            "Num4 = math.trunc(X)  # Returns X with the decimal part removed\n"
            "Num5 = math.pow(X, Y)  # Returns X to the Y power\n"
            "Num6 = math.sqrt(X)  # Returns the square root of X\n"
            "Num7 = math.pi  # Returns pi",
            language='python')

    st.write("""
    Below are the random functions you will use:
    """)
    st.code("import random\n"
            "\n"
            "Num1 = random.random()  # Generates a random number from 0-1\n"
            "Num2 = random.randint(X, Y)  # Returns a random number from X to Y\n"
            "Num3 = random.choice(['Red', 'Orange', 'Yellow'])  # Picks a random value within a list",
            language='python')

    st.write("""
    It will be convenient for you to memorize these functions, but it is no problem if you forget the correct syntax. Consult the cheat sheet or Google to properly type out the functions/modules.
    """)


elif st.session_state.expandtitle == "Unit 2.4":
    st.header("Unit 2 Summary")
    st.write("""
        | Operator  |   Function                                          |
        |-----------|-----------------------------------------------------|
        |    ()     |    Call operator - calls function or method         |
        |    **     | Exponent operator - raises a value to an exponent   |
        | *,/,//,%  |    Multiplication - multiplies, Division - divides, |
        |           |   Floor Division - removes decimal after division,  |  
        |           |  Modulo - Provides remainder after division         |
        |           |                                                     |
        |   +, -    | Addition - Adds, Subtraction - subtracts            |
        """)
    st.write(" Examples of each: ")
    st.code(" print('The parentheses help tell what to print')", language='python')
    st.code(" val = 3 ** 2 #stores 9 in val", language='python')
    st.code(" val = 3 * 2 #stores 6 in val", language='python')
    st.code(" val = 3 / 1 #stores 3 in val", language='python')
    st.code(" val = 3 // 2 #stores 1 in val (cuts off the .5 in 1.5)", language='python')
    st.code(" val = 3 % 2 #stores 1 in val because 3/2 is 1 remainder 1", language='python')
    st.code(" val = 3 + 2 #stores 5 in val", language='python')
    st.code(" val = 3 - 2 #stores in 1", language='python')
    st.write(" These operators, in order of highest precedence to lowest, make up the majority of arithmetic operators used in python")

elif st.session_state.expandtitle == "Unit 2.5":
    st.header("Unit 2 Quiz")
    # Question 1
    q1 = st.radio("What does the (%) operator do in Python?",
                  ("It performs addition",
                   "It performs subtraction",
                   "It calculates the remainder after division",
                   "It multiplies two numbers"),
                  index=None
                  )

    if q1 == "It calculates the remainder after division":
        st.markdown("Correct!")

        # Question 2
        q2 = st.radio("What is the result of '5 ** 3' in Python?",
                      ("8", "15", "125", "500"),
                      index=None
                      )
        if q2 == "125":
            st.markdown("Correct!")

            # Question 3
            q3 = st.radio("What does the (//) operator do in Python?",
                          ("It performs floor division",
                           "It calculates the square root",
                           "It multiplies two numbers",
                           "It performs exponentiation"),
                          index=None
                          )
            if q3 == "It performs floor division":
                st.markdown("Correct!")

                # Question 4
                q4 = st.radio("What is the result of '15 / 4' in Python?",
                              ("3.75", "3.0", "3", "4"),
                              index=None
                              )
                if q4 == "3.75":
                    st.markdown("Correct!")

                    # Question 5
                    q5 = st.radio("What is the purpose of the '//' operator in Python?",
                                  ("To perform addition",
                                   "To calculate the remainder after division",
                                   "To perform floor division",
                                   "To calculate the square root"),
                                  index=None
                                  )
                    if q5 == "To perform floor division":
                        st.markdown("Correct!")

                        # Question 6
                        q6 = st.radio("What is the result of '8 - 3' in Python?",
                                      ("11", "5", "2", "24"),
                                      index=None
                                      )
                        if q6 == "5":
                            st.markdown("Correct!")

                            # Question 7
                            q7 = st.radio("Which operator is used for exponentiation in Python?",
                                          ("^", "//", "**", "exp()"),
                                          index=None
                                          )
                            if q7 == "**":
                                st.markdown("Correct!")

                                # Question 8
                                q8 = st.radio("What is the result of '20 % 7' in Python?",
                                              ("2", "6", "3", "0"),
                                              index=None
                                              )
                                if q8 == "6":
                                    st.markdown("Correct!")

                                    # Question 9
                                    q9 = st.radio("What is the result of '10 / 3' in Python?",
                                                  ("3.333", "3", "3.0", "33"),
                                                  index=None
                                                  )
                                    if q9 == "3.333":
                                        st.markdown("Correct!")

                                        # Question 10
                                        q10 = st.radio("What is the purpose of the '%' operator in Python?",
                                                       ("To perform addition",
                                                        "To calculate the square root",
                                                        "To calculate the remainder after division",
                                                        "To perform floor division"),
                                                       index=None
                                                       )
                                        if q10 == "To calculate the remainder after division":
                                            st.markdown("Correct!")
                                            if st.button("Next Section!"):
                                                st.session_state.expandtitle = "Unit 2.2"

                                        elif (q10 == "To perform addition"
                                              or q10 == "To calculate the square root"
                                              or q10 == "To perform floor division"):
                                            st.markdown("Try Again!")
                                    elif (q9 == "3"
                                          or q9 == "3.0"
                                          or q9 == "33"):
                                        st.markdown("Try Again!")
                                elif (q8 == "2"
                                      or q8 == "3"
                                      or q8 == "0"):
                                    st.markdown("Try Again!")
                            elif (q7 == "^"
                                  or q7 == "//"
                                  or q7 == "exp()"):
                                st.markdown("Try Again!")
                        elif (q6 == "11"
                              or q6 == "2"
                              or q6 == "24"):
                            st.markdown("Try Again!")
                    elif (q5 == "To perform addition"
                          or q5 == "To calculate the square root"
                          or q5 == "To calculate the remainder after division"):
                        st.markdown("Try Again!")
                elif (q4 == "3"
                      or q4 == "3.0"
                      or q4 == "4"):
                    st.markdown("Try Again!")
            elif (q3 == "It calculates the square root"
                  or q3 == "It multiplies two numbers"
                  or q3 == "It performs exponentiation"):
                st.markdown("Try Again!")
        elif (q2 == "8"
              or q2 == "15"
              or q2 == "500"):
            st.markdown("Try Again!")
    elif (q1 == "It performs addition"
          or q1 == "It performs subtraction"
          or q1 == "It multiplies two numbers"):
        st.markdown("Try Again!")

elif st.session_state.expandtitle == "Unit 3.1":
    st.header("Unit 3.1: If Statements")
    st.title("If-Else Statements, Conditional, and Logical Operators")

    # Explanation of conditional statements, comparison operators, and logical operators
    st.write("""
    Conditional statements determine if one or multiple conditions have been met and perform an action based on whether the condition is fulfilled or not.

    Conditional statements use logical operators. Here are the comparison operators:
    - Greater than (>)
    - Less than (<)
    - Equal to (==)
    - Not equal to (!=)
    - Greater than or equal to (>=)
    - Less than or equal to (<=)

    And here are the logical operators:
    - And (If both statements are true, the condition is fulfilled)
    - Or (If either condition is true, the condition is fulfilled)
    - Not (Reverses the Boolean value of a statement)

    Values are compared, and if the statement is true (returning True, a Boolean value), then the code under the condition will get executed.

    Let's see an example using the if statement:
    """)
    st.code("x = 15\n"
            "if x > 10 or x != 10:\n"
            "    print('Hello')",
            language='python')

    st.write("""
    In the code above, the if statement checks if x is greater than 10 or not equal to 10. If the condition is met, it prints 'Hello'.

    Note the indented portion of the code and the colon at the end of the condition that signifies that everything below that is indented only happens if the condition is met.

    If-else statements are similar to if statements, but they allow you to specify an action to perform if the original condition is not fulfilled. Here's an example:
    """)
    st.code("x = int(input('Enter a number'))\n"
            "\n"
            "if x > 10:\n"
            "    print('X is greater than 10.')\n"
            "else:\n"
            "    print('X is either less than 10')\n"
            "    print('Or 10.')",
            language='python')

    st.write("""
    In this code, we take user input for a number and use if-else statements to check whether it's greater than 10. Depending on the condition, different messages are printed. You can include multiple actions under one condition.

    Conditional statements, comparison operators, and logical operators are fundamental concepts in programming and are essential for making decisions in your code.
    """)
elif st.session_state.expandtitle == "Unit 3.2":
    st.header("Unit 3.2: Else Statements")
    st.title("Else-If Statements (elif) Explanation")

    # Explanation of else-if statements (elif)
    st.write("""
    Else-if statements, also known as "elif" statements, are used for more complex branching in your code. They allow you to handle multiple conditions and perform different actions depending on which condition is met. 

    Here's a more detailed look at else-if statements:

    Else-if statements are used when you have two or more conditions to check, and you want to execute specific code blocks based on those conditions.

    In the following example, we'll create a program that asks for the user's name and greets them differently based on their name:
    """)
    st.code("name = input('Enter your name: ')\n"
            "\n"
            "if name == 'Tom':\n"
            "    print('Hi Tom')\n"
            "elif name == 'John':\n"
            "    print('Hi John')\n"
            "elif name == 'June':\n"
            "    print('Hi June')\n"
            "else:\n"
            "    print('Hello')",
            language='python')

    st.write("""
    In this code, we first ask the user to enter their name. Then, we use else-if statements (elif) to check multiple conditions. If the user's name matches one of the conditions, a specific greeting is printed. If none of the conditions are met, a default greeting is printed using the else statement.

    Here's a breakdown of the code:
    - We ask for the user's name using the `input` function.
    - We use if-elif-else statements to check the name against multiple conditions.
    - If the name is 'Tom', it prints 'Hi Tom.'
    - If the name is 'John', it prints 'Hi John.'
    - If the name is 'June', it prints 'Hi June.'
    - If none of the conditions are met, it prints 'Hello.'

    You can include as many elif statements as needed to handle various cases.

    Else-if statements are useful for creating complex decision trees in your code, allowing you to execute different actions based on different conditions. They make your code more flexible and capable of handling a wide range of scenarios.
    """)

    # More content here (copy and paste the above section to extend it)
    st.write("""
    Here's another example of using elif statements to determine the season based on the month entered by the user:
    """)
    st.code("month = input('Enter the month (e.g., January): ')\n"
            "\n"
            "if month == 'December' or month == 'January' or month == 'February':\n"
            "    print('It's winter.')\n"
            "elif month == 'March' or month == 'April' or month == 'May':\n"
            "    print('It's spring.')\n"
            "elif month == 'June' or month == 'July' or month == 'August':\n"
            "    print('It's summer.')\n"
            "elif month == 'September' or month == 'October' or month == 'November':\n"
            "    print('It's autumn.')\n"
            "else:\n"
            "    print('Month not recognized.')",
            language='python')

    st.write("""
    In this code, we take the user's input for the month and use elif statements to determine the season. Depending on the entered month, it prints the corresponding season. If the month is not recognized, it prints 'Month not recognized.'

    This demonstrates how elif statements can handle a range of conditions and make your code more comprehensive and adaptable.

    Feel free to use elif statements in your code whenever you need to make decisions based on multiple conditions, as they help structure your logic effectively.
    """)

    # More content here (copy and paste the above section to extend it)
    st.write("""
    Here's a more complex example that uses elif statements to determine the category of a product based on its price:
    """)
    st.code("price = float(input('Enter the price of the product: '))\n"
            "\n"
            "if price < 10:\n"
            "    print('Category: Low-cost')\n"
            "elif price >= 10 and price < 50:\n"
            "    print('Category: Mid-range')\n"
            "elif price >= 50 and price < 100:\n"
            "    print('Category: Premium')\n"
            "else:\n"
            "    print('Category: Luxury')",
            language='python')

    st.write("""
    In this code, we take the price of a product as input, and based on the price range, we determine its category. If the price is less than 10, it's considered low-cost. If it falls between 10 and 50, it's mid-range, and so on.

    This example illustrates how elif statements can handle more intricate decision-making processes, allowing your code to respond intelligently to various scenarios.

    Else-if statements are a powerful tool for branching logic in your code, making it more versatile and capable of handling complex decision-making tasks.
    """)

elif st.session_state.expandtitle == "Unit 3.3":
    st.header("Unit 3.3: Nested Conditionals")
    st.title("Nested If Statements Explanation")

    # Explanation of nested if statements
    st.write("""
    Nested if statements are used when you need to evaluate multiple conditions within another condition. This allows for more complex decision-making in your code.

    Nested if statements are essentially if statements inside other if statements. They are used to create hierarchical decision structures, where you check multiple conditions in a structured manner.

    Example 1: Categorizing a product based on price and availability
    """)
    st.code("price = float(input('Enter the price of the product: '))\n"
            "availability = input('Is the product available (yes/no): ')\n"
            "\n"
            "if price < 10:\n"
            "    if availability == 'yes':\n"
            "        print('Low-cost and available')\n"
            "    else:\n"
            "        print('Low-cost but not available')\n"
            "elif price < 50:\n"
            "    if availability == 'yes':\n"
            "        print('Mid-range and available')\n"
            "    else:\n"
            "        print('Mid-range but not available')\n"
            "else:\n"
            "    if availability == 'yes':\n"
            "        print('Premium and available')\n"
            "    else:\n"
            "        print('Premium but not available')",
            language='python')

    st.write("""
    Example 2: Determining a student's grade
    """)
    st.code("score = int(input('Enter the student's score: '))\n"
            "\n"
            "if score >= 90:\n"
            "    if score == 100:\n"
            "        print('Grade: A+ (Perfect score!)')\n"
            "    else:\n"
            "        print('Grade: A')\n"
            "elif score >= 80:\n"
            "    print('Grade: B')\n"
            "elif score >= 70:\n"
            "    print('Grade: C')\n"
            "elif score >= 60:\n"
            "    print('Grade: D')\n"
            "else:\n"
            "    print('Grade: F (Fail)')",
            language='python')

    st.write("""
    Example 3: Checking eligibility for a driving license
    """)
    st.code("age = int(input('Enter your age: '))\n"
            "driving_test = input('Have you passed the driving test (yes/no): ')\n"
            "\n"
            "if age >= 18:\n"
            "    if driving_test == 'yes':\n"
            "        print('Eligible for a driving license.')\n"
            "    else:\n"
            "        print('You need to pass the driving test to be eligible.')\n"
            "else:\n"
            "    print('Must be 18 or older to apply for a driving license.')",
            language='python')

    st.write("""
    Nested if statements allow you to create complex decision trees in your code, making it capable of handling detailed scenarios effectively.
    """)
elif st.session_state.expandtitle == "Unit 3.4":
    st.header("Unit 3 Summary")
elif st.session_state.expandtitle == "Unit 3.5":
    st.header("Unit 3 Quiz")
elif st.session_state.expandtitle == "Unit 4.1":
    st.header("Unit 4.1: For Loops")
elif st.session_state.expandtitle == "Unit 4.2":
    st.header("Unit 4.2: While Loops")
    st.title("Understanding While Loops")

    # Explanation
    st.write("While loops continuously perform an action as long as a condition is fulfilled.")
    st.write("They are useful when you don't know how many iterations your statement will have.")
    st.write("Here's an example:")

    # Initialize x
    x = 1

    # While loop example
    st.code(
        """
    while x < 10:
        st.write("x is less than 10")
        x += 1
        """
    )

    st.write("In this example, the while loop will execute until x becomes greater than or equal to 10.")
    st.write(
        "Each time the loop runs, it checks if x is less than 10. If that's true, it prints 'x is less than 10' and increments x by 1.")
    st.write("Now, let's run the loop to see it in action:")

    # While loop execution
    x = 1  # Reset x
    while x < 10:
        st.write(f"x is {x}. It is less than 10.")
        x += 1

    st.write("The loop stops when x reaches 10 because the condition (x < 10) is no longer fulfilled.")
    st.write("While loops are powerful for tasks where you need to repeat an action until a certain condition is met.")

    # More complex example
    st.header("Example: Counting Odd Numbers")

    st.write("Let's use a while loop to count and display the first 10 odd numbers.")
    st.write("We'll start with 1 and keep adding 2 until we have 10 odd numbers.")

    # Initialize variables
    count = 1
    odd_numbers = []

    # While loop to count odd numbers
    while count <= 10:
        odd_numbers.append(count)
        count += 2

    st.write(f"The first 10 odd numbers are: {odd_numbers}")

elif st.session_state.expandtitle == "Unit 4.3":
    st.header("Unit 4.3: Nested Loops")
    st.title("Unit 4.3: Nested Loops")

    st.write(
        "Nested loops are loops within loops. They are used when you need to perform repetitive tasks within repetitive tasks.")

    # Example of a nested loop
    st.write("Example:")
    st.code("""
    for i in range(3):
        for j in range(2):
            st.write(f"Outer loop iteration {i}, Inner loop iteration {j}")
    """)
    st.write(
        "In this example, we have an outer loop that iterates three times and an inner loop that iterates two times for each outer loop iteration.")

    st.write("Key points about nested loops:")

    st.subheader("Nested Loop Structure")
    st.write("Nested loops consist of an outer loop and one or more inner loops.")

    st.subheader("Order of Execution")
    st.write("The inner loop runs completely for each iteration of the outer loop.")

    st.subheader("Common Use Cases")
    st.write(
        "Nested loops are often used for tasks like matrix traversal, working with multi-dimensional data, or generating combinations.")

    st.subheader("Indentation")
    st.write("Proper indentation is crucial to distinguish between the outer and inner loops.")

    st.write("Nested loops can be powerful but require careful design to avoid excessive execution.")

    # Conclusion
    st.header("Conclusion")
    st.write("In this unit, you've learned about nested loops, a concept where loops are placed inside other loops.")
    st.write("Nested loops are useful for tasks that involve repetitive actions within repetitive actions.")
    st.write("Proper indentation and understanding of loop order are essential when working with nested loops.")
elif st.session_state.expandtitle == "Unit 4.4":
    st.header("Unit 4 Summary")
elif st.session_state.expandtitle == "Unit 4.5":
    st.header("Unit 4 Quiz")
elif st.session_state.expandtitle == "Unit 5.1":
    st.header("Unit 5.1: Lists")
    st.title("Unit 5.1: Lists")

    st.write("Lists store multiple values within one variable. Any data type can be stored within a list, "
             "and differing data types can be stored within the same list. Any value stored within a list is called an element.")

    # Example list
    devices = ["Phone", "Laptop", "Tablet"]

    st.write("Example:")
    st.code("Devices = ['Phone', 'Laptop', 'Tablet']")

    st.write("Below are functions that can be used on lists:")
    st.code("""
    import random

    Y = [1, 3, 2, 5]
    X = 3

    Value1 = Y.append(X)  # Adds an element to the end of a list
    Value2 = Y.count(X)   # Returns the number of elements that have the value X
    Value3 = Y.sort()     # Sorts the list
    Value5 = random.choice(Y)  # Picks a random value within a list
    """)

    st.write(
        "In this unit, you've learned about lists, versatile data structures that can store multiple values of any data type. "
        "Lists are fundamental in programming and provide a convenient way to work with collections of data.")

    # Conclusion
    st.header("Conclusion")
    st.write(
        "Lists are an essential data structure in programming, allowing you to store and manipulate collections of data efficiently.")
    st.write("You've also seen some common functions that can be used to modify and work with lists, "
             "such as appending elements, counting occurrences, sorting, and selecting random values.")
    st.write(
        "Mastering lists is crucial for a wide range of programming tasks, and they are widely used in various applications.")
elif st.session_state.expandtitle == "Unit 5.2":
    st.header("Unit 5.2: Traversing Through Lists")

    st.title("Unit 5.2: Traversing Through Lists")

    st.write("Traversing through lists means accessing and processing each element in a list one by one. "
             "This is a fundamental operation when working with lists.")

    # Example list
    numbers = [1, 2, 3, 4, 5]

    st.write("Example:")
    st.code("numbers = [1, 2, 3, 4, 5]")

    st.write("Here are common techniques for traversing through lists:")

    st.subheader("1. Using a For Loop")
    st.write("You can use a 'for' loop to iterate through each element in the list.")
    st.code("""
    for num in numbers:
        st.write(f"Element: {num}")
    """)

    st.subheader("2. Using List Indexing")
    st.write("You can access elements by their index in the list.")
    st.code("""
    for i in range(len(numbers)):
        st.write(f"Element {i + 1}: {numbers[i]}")
    """)

    st.subheader("3. Using Enumerate")
    st.write("Enumerate allows you to access both the index and the value of each element.")
    st.code("""
    for idx, num in enumerate(numbers):
        st.write(f"Element {idx + 1}: {num}")
    """)

    st.write(
        "Traversing through lists is essential for performing various operations, such as calculations, filtering, and data processing.")

    # Conclusion
    st.header("Conclusion")
    st.write(
        "In this unit, you've learned about traversing through lists, a fundamental operation when working with collections of data.")
    st.write("You've seen different techniques, including 'for' loops, list indexing, and 'enumerate,' "
             "that allow you to access and process each element in a list.")
    st.write("Mastering these techniques is crucial for working efficiently with lists in programming.")

elif st.session_state.expandtitle == "Unit 5.3":
    st.header("Unit 5.3: Appending/Removing")
    st.title("Unit 5.3: Appending and Removing from Lists")

    st.write("Appending and removing elements from lists are common operations when working with data in programming. "
             "These operations allow you to modify the contents of a list.")

    # Example list
    fruits = ["Apple", "Banana", "Cherry"]

    st.write("Example:")
    st.code("fruits = ['Apple', 'Banana', 'Cherry']")

    st.write("Here are common techniques for appending and removing elements from lists:")

    st.subheader("1. Appending Elements")
    st.write("You can add elements to the end of a list using the 'append' method.")
    st.code("""
    fruits.append("Orange")
    st.write(fruits)
    """)

    st.subheader("2. Inserting Elements")
    st.write("You can insert elements at a specific position in the list using the 'insert' method.")
    st.code("""
    fruits.insert(1, "Grape")
    st.write(fruits)
    """)

    st.subheader("3. Removing Elements by Value")
    st.write("You can remove elements by their value using the 'remove' method.")
    st.code("""
    fruits.remove("Banana")
    st.write(fruits)
    """)

    st.subheader("4. Removing Elements by Index")
    st.write("You can remove elements by their index using the 'pop' method.")
    st.code("""
    removed_fruit = fruits.pop(0)
    st.write(f"Removed: {removed_fruit}")
    st.write(fruits)
    """)

    st.write(
        "Appending and removing elements from lists are essential for data manipulation and management in programming.")

    # Conclusion
    st.header("Conclusion")
    st.write(
        "In this unit, you've learned how to append and remove elements from lists, fundamental operations when working with data.")
    st.write("You've seen different techniques, including 'append,' 'insert,' 'remove,' and 'pop,' "
             "that allow you to modify the contents of a list.")
    st.write("These operations are crucial for dynamic data handling and list maintenance in programming.")

elif st.session_state.expandtitle == "Unit 5.4":
    st.header("Unit 5.4: 2-D Lists")
    st.write("Example:")
    st.code("matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")

    st.write("Here are common techniques for working with 2-D lists:")

    st.subheader("1. Accessing Elements")
    st.write("You can access elements in a 2-D list using two indices: one for the row and one for the column.")
    st.code("""
    element = matrix[1][2]  # Accessing the element in the second row and third column
    st.write(f"Element: {element}")
    """)

    st.subheader("2. Iterating Through Rows")
    st.write("You can iterate through the rows of a 2-D list using 'for' loops.")
    st.code("""
    for row in matrix:
        st.write(row)
    """)

    st.subheader("3. Iterating Through Elements")
    st.write("You can iterate through all elements in a 2-D list using nested 'for' loops.")
    st.code("""
    for row in matrix:
        for element in row:
            st.write(element)
    """)

    st.write("2-D lists are useful for representing and working with structured data, such as tables and grids.")

    # Conclusion
    st.header("Conclusion")
    st.write(
        "In this unit, you've learned about 2-D lists, a versatile data structure for organizing data in rows and columns.")
    st.write(
        "You've seen how to access elements, iterate through rows and elements, and perform operations on 2-D lists.")
    st.write(
        "2-D lists are essential for tasks that involve structured data representation, such as matrices and tables.")
elif st.session_state.expandtitle == "Unit 5.5":
    st.header("Unit 5 Summary")
elif st.session_state.expandtitle == "Unit 5.6":
    st.header("Unit 5 Quiz")
elif st.session_state.expandtitle == "Unit 6.1":
    st.header("Unit 6.1: Function Declaration")
    st.title("Unit 6.1: Function Declaration")

    st.write("A function is a reusable block of code that performs a specific task or set of tasks. "
             "Declaring a function involves defining its name, parameters, and the code to execute when the function is called.")

    # Example function declaration
    st.write("Example:")
    st.code("""
    def greet(name):
        st.write(f"Hello, {name}!")

    # Calling the function
    greet("Alice")
    """)
    st.write(
        "In this example, we've declared a function named 'greet' that takes a 'name' parameter and prints a greeting message.")

    st.write("Here are the components of a function declaration:")

    st.subheader("Function Name")
    st.write("The name of the function, which should be descriptive and relevant to its purpose.")

    st.subheader("Parameters")
    st.write("Values that the function accepts as input. Parameters are enclosed in parentheses.")

    st.subheader("Function Body")
    st.write(
        "The block of code that defines what the function does. It is indented and follows the function declaration.")

    st.subheader("Calling a Function")
    st.write(
        "To execute the code within a function, you need to call the function by its name and provide any required arguments.")

    st.write("Functions are essential for code organization, reusability, and modularity.")

    # Conclusion
    st.header("Conclusion")
    st.write("In this unit, you've learned about function declaration, a fundamental concept in programming.")
    st.write("Functions allow you to encapsulate code, making it reusable and organized.")
    st.write(
        "You've seen how to declare functions with names, parameters, and a function body, as well as how to call them.")

elif st.session_state.expandtitle == "Unit 6.2":
    st.header("Unit 6.2: Parameters")

    st.title("Unit 6.2: Function Parameters")

    st.write("Function parameters are values that you can pass to a function to customize its behavior. "
             "They allow functions to work with different input data.")

    # Example function with parameters
    st.write("Example:")
    st.code("""
    def greet(name):
        st.write(f"Hello, {name}!")

    # Calling the function with a parameter
    greet("Alice")
    """)
    st.write(
        "In this example, we have a function 'greet' that takes a 'name' parameter and prints a greeting message with that name.")

    st.write("Here are common aspects of function parameters:")

    st.subheader("Parameter Declaration")
    st.write("Parameters are declared within the parentheses when defining the function.")

    st.subheader("Passing Arguments")
    st.write("When calling a function, you pass arguments that match the function's parameters.")

    st.subheader("Multiple Parameters")
    st.write("Functions can have multiple parameters separated by commas.")

    st.subheader("Default Values")
    st.write("You can assign default values to parameters, making them optional when calling the function.")

    st.subheader("Positional and Keyword Arguments")
    st.write(
        "Arguments can be passed either by position (matching the order of parameters) or by keyword (matching parameter names).")

    st.write("Function parameters make functions versatile and adaptable to different scenarios.")

    # Conclusion
    st.header("Conclusion")
    st.write(
        "In this unit, you've learned about function parameters, which allow you to customize a function's behavior "
        "by passing different values as arguments.")
    st.write(
        "You've seen how to declare parameters, pass arguments, use multiple parameters, and assign default values.")
    st.write(
        "Understanding and effectively using parameters is essential for creating flexible and reusable functions.")
elif st.session_state.expandtitle == "Unit 6.3":
    st.header("Unit 6.3: Returning Values in Functions")
    st.title("Unit 6.3: Returning Values in Functions")

    st.write(
        "Functions not only perform actions but can also return values. A return statement is used to specify what value the function should return.")

    # Example function with a return value
    st.write("Example:")
    st.code("""
    def add_numbers(a, b):
        result = a + b
        return result

    # Calling the function and storing the result
    sum_result = add_numbers(5, 3)
    st.write(f"The sum is: {sum_result}")
    """)
    st.write(
        "In this example, we have a function 'add_numbers' that takes two parameters, adds them, and returns the result.")

    st.write("Here are important aspects of returning values in functions:")

    st.subheader("Return Statement")
    st.write("The 'return' statement is used to specify the value to be returned from the function.")

    st.subheader("Function Output")
    st.write("The value returned by a function can be assigned to a variable when calling the function.")

    st.subheader("Multiple Return Statements")
    st.write("A function can have multiple 'return' statements, each with different conditions.")

    st.subheader("Void Functions")
    st.write("Functions that don't have a 'return' statement implicitly return 'None'.")

    st.write(
        "Returning values from functions allows you to obtain results and use them in other parts of your program.")

    # Conclusion
    st.header("Conclusion")
    st.write(
        "In this unit, you've learned about returning values in functions, which enables functions to provide results that can be used elsewhere in your code.")
    st.write("The 'return' statement is used to specify the value to be returned from a function.")
    st.write(
        "Understanding how to use return values is crucial for creating functions that perform specific tasks and provide meaningful results.")
elif st.session_state.expandtitle == "Unit 6.4":
    st.header("Unit 6 Summary")
elif st.session_state.expandtitle == "Unit 6.5":
    st.header("Unit 6 Quiz")
elif st.session_state.expandtitle == "Unit 7.1":
    st.header("Recap")
elif st.session_state.expandtitle == "Unit 7.2":
    st.header("Final Exam")
elif st.session_state.expandtitle == "Unit 7.3":
    st.header("Final Project")


elif st.session_state.expandtitle == "Cheatsheet":
    st.header("Cheatsheet")
    # Add content for Cheatsheet

elif st.session_state.expandtitle == "Flashcards":
    st.header("Flashcards")

    # Check if flashcards have been created previously
    if 'flashcards' not in st.session_state:
        st.session_state.flashcards = {}

    # Input fields to add new flashcards
    st.subheader("Create Flashcards")
    term = st.text_input("Term:")
    definition = st.text_input("Definition:")
    if st.button("Add Flashcard"):
        if term and definition:
            st.session_state.flashcards[term] = definition
            st.success("Flashcard added successfully!")

    # Main content area to display flashcards
    st.subheader("Your Flashcards")

    if not st.session_state.flashcards:
        st.info("No flashcards created yet. Use the input fields above to add flashcards.")
    else:
        for term, definition in st.session_state.flashcards.items():
            st.write(f"**Term:** {term}")
            st.write(f"**Definition:** {definition}")


    # Add content for Flashcards

elif st.session_state.expandtitle == "Home":
    st.header("Home")
    tab1, tab2, tab3 = st.tabs(["Welcome", "Get Started", "About Us"])
    with tab1:
        # Header
        st.title("Welcome to eduPY")
        st.subheader("Your Gateway to Python Education")

        # Introduction
        st.write(
            "Are you ready to embark on a Python learning journey? Whether you're a beginner taking your first steps "
            "in coding or an experienced developer looking to enhance your skills, eduPY is here to support your "
            "Python education.")

        # Key Features
        st.markdown("## Key Features")
        st.subheader("Comprehensive Python Curriculum")
        st.write("Our comprehensive curriculum covers Python programming from the fundamentals to advanced topics. "
                 "Explore a wide range of Python applications, including data science, web development, and more.")

        st.subheader("Interactive Learning")
        st.write("Learn by doing with our interactive courses and hands-on coding exercises. Engage with practical "
                 "coding challenges that reinforce your skills.")

        st.subheader("Experienced Instructors")
        st.write("Benefit from the expertise of our experienced Python instructors. They bring real-world experience "
                 "and a passion for teaching to every lesson.")

        st.subheader("Community and Support")
        st.write("Join our vibrant learning community. Connect with fellow students, ask questions, and collaborate on "
                 "projects. Our support team is here to assist you on your journey.")

        st.subheader("Flexible Learning Options")
        st.write("Choose the learning style that suits you best. Whether you prefer self-paced learning or structured "
                 "courses with deadlines, we have options to fit your needs.")

        # Get Started
        st.markdown("## Get Started")
        st.write("Ready to begin? Dive into the world of Python programming with eduPY today!")

        if st.button("Start Learning"):
            # Redirect to the curriculum page or the first unit
            st.session_state.expandtitle = "Unit 1.1"
            # You can change the expandtitle value based on where you want to redirect the user

        # Footer
        st.write("Thank you for choosing eduPY. We look forward to helping you achieve your Python programming goals!")
    with tab2:
        # Header
        st.title("Installing Python and PyCharm")
        st.subheader("Getting Started with Python Development")

        # Introduction
        st.write(
            "Before you begin your Python programming journey, you'll need to set up your development environment. "
            "This guide will walk you through the process of installing Python and PyCharm, a popular Python IDE.")

        # Installing Python
        st.markdown("## Installing Python")
        st.subheader("Step 1: Download Python")
        st.write("To install Python, you can download the latest version from the official Python website. "
                 "Choose the appropriate installer for your operating system (Windows, macOS, or Linux).")

        st.subheader("Step 2: Run the Installer")
        st.write("Run the downloaded installer and follow the installation wizard. Be sure to check the box that says "
                 "'Add Python X.X to PATH' (X.X represents the Python version number). This ensures that Python is added "
                 "to your system's PATH environment variable.")

        st.subheader("Step 3: Verify Installation")
        st.write("To verify that Python has been installed correctly, open a command prompt or terminal and enter the "
                 "following command:")
        st.code("python --version", language="shell")

        st.write("You should see the Python version displayed, indicating a successful installation.")

        # Installing PyCharm
        st.markdown("## Installing PyCharm")
        st.subheader("Step 1: Download PyCharm")
        st.write(
            "PyCharm is a popular Python IDE developed by JetBrains. You can download the Community edition, which is "
            "free, or the Professional edition for additional features. Visit the PyCharm website to download the installer.")

        st.subheader("Step 2: Run the Installer")
        st.write("Run the downloaded PyCharm installer and follow the installation instructions. You can choose to "
                 "customize your installation options if desired.")

        st.subheader("Step 3: First Launch")
        st.write(
            "After installation, launch PyCharm. You'll be prompted to import settings or customize the IDE to your liking. "
            "Follow the setup wizard to configure PyCharm as you prefer.")

        st.write("You're now ready to start coding with Python in PyCharm!")

        # Next Steps
        st.markdown("## Next Steps")
        st.write("With Python and PyCharm installed, you're ready to explore the world of Python programming. "
                 "Consider taking our introductory courses to begin your learning journey.")

        st.link_button("Syllabus", "https://docs.google.com/document/d/18pOZAv8kwUpfFii0ko1iciQv3-eyxOmcmdLVdaqvjVg/edit?usp=sharing")

        # Footer
        st.write("Thank you for choosing eduPY. We wish you success in your Python development endeavors!")

    with tab3:
        # Header
        st.title("About eduPY")
        st.markdown("## Welcome to eduPY – Your Gateway to Python Education!")

        # Introduction
        st.write("At eduPY, we are passionate about spreading the knowledge and power of Python programming "
                 "to learners of all levels, from beginners taking their first steps in coding to seasoned "
                 "developers looking to enhance their skills. Our mission is to make Python education accessible, "
                 "engaging, and effective.")

        # What Sets Us Apart
        st.markdown("## What Sets Us Apart")
        st.subheader("Comprehensive Python Curriculum")
        st.write("We offer a comprehensive curriculum that covers Python programming from the fundamentals "
                 "to advanced topics. Whether you're interested in mastering Python basics, data science, web "
                 "development, or artificial intelligence, our courses have you covered.")

        st.subheader("Interactive Learning")
        st.write("Learning Python doesn't have to be boring! Our interactive courses and hands-on coding exercises "
                 "keep you engaged and motivated throughout your learning journey. You'll learn by doing, making "
                 "your knowledge practical and immediately applicable.")

        st.subheader("Experienced Instructors")
        st.write("Our team of experienced Python instructors is dedicated to your success. They bring real-world "
                 "experience and a passion for teaching to every lesson. You'll benefit from their guidance and "
                 "insights as you progress in your Python education.")

        st.subheader("Community and Support")
        st.write(
            "Join a thriving community of learners who share your passion for Python. Connect with fellow students, "
            "ask questions, and collaborate on projects. Our support team is always here to assist you on your learning path.")

        st.subheader("Flexible Learning Options")
        st.write(
            "We understand that everyone's learning journey is unique. That's why we offer flexible learning options. "
            "Whether you prefer self-paced learning or structured courses with deadlines, we have options to suit your needs.")

        # Our Vision
        st.markdown("## Our Vision")
        st.write(
            "Our vision is to empower individuals with the skills and knowledge they need to excel in the world of Python "
            "programming. We believe that Python is not just a programming language; it's a tool that opens doors to countless "
            "possibilities.")

        # Get Started
        st.markdown("## Get Started Today!")
        st.write(
            "Are you ready to embark on your Python learning adventure? Join eduPY today and take your first steps towards "
            "becoming a Python pro! Whether you're looking to build a career in tech, launch a data science project, or "
            "simply explore the world of coding, we're here to support you every step of the way.")

        st.write("Thank you for choosing eduPY. We look forward to helping you achieve your Python programming goals!")


    # Add content for Home
