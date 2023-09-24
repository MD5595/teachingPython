import streamlit as st
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

if st.session_state.get("question_number") is None:
    st.session_state.question_number = 0

with st.sidebar:
    account_manager()
    container = st.container()

    "Select:"
    if st.button("Home", use_container_width=True):
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
        if st.button("Unit 2.3: Modules", use_container_width=True):
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
        if st.button("Unit 5 Quiz", use_container_width=True):
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
    st.markdown("A Python file being formatted improperly or having inappropriately named components will cause it to "
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
                         ("print(\"Goodmorning!\')", "print(Goodmorning!\")", "print(\"Goodmorning!\")",
                          "print(\"Goodmorning!)"),
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
    # Question for 1.3
    question3 = st.radio("What would hello_world.py output?",
                         ("variable = 42", "42 = variable", "variable == 42", "variable: 42"),
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
    elif (question3 == "Converts the Age variable to an integer"
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
    if st.button("Next Section"):
        st.session_state.expandtitle = "Unit 1.6"
    
elif st.session_state.expandtitle == "Unit 1.6":

    st.title("Unit 1 Quiz")

    # Question 1
    q1 = st.radio(
        "If x = 3 and y = 5. A variable result is made that aims to find the product of the two, how would it be done?",
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
                                            if st.button("Next Unit!"):
                                                st.session_state.expandtitle = "Unit 2.1"

                                        elif (q10 == "To convert text to uppercase"
                                              or q10 == "To accept user input"
                                              or q10 == "To convert a value to an integer"):
                                            st.markdown("Try Again!")
                                    elif (q9 == "3.33"
                                          or q9 == "3.0"
                                          or q9 == "33"):
                                        st.markdown("Try Again!")
                                elif (q8 == "^"
                                      or q8 == "//"
                                      or q8 == "pwr()"):
                                    st.markdown("Try Again!")
                            elif (q7 == "# This is a comment"
                                  or q7 == "''' This is a comment '''"
                                  or q7 == "\"This is a comment\""):
                                st.markdown("Try Again!")
                        elif (q6 == "2"
                              or q6 == "7"
                              or q6 == "15"):
                            st.markdown("Try Again!")
                    elif (q5 == "To convert text to uppercase"
                          or q5 == "To display text on the screen"
                          or q5 == "To convert numbers to strings"):
                        st.markdown("Try Again!")
                elif (q4 == "It converts text to uppercase"
                      or q4 == "It converts text to lowercase"
                      or q4 == "It converts numbers to strings"):
                    st.markdown("Try Again!")
            elif (q3 == "It defines a function"
                  or q3 == "It performs mathematical calculations"
                  or q3 == "It converts text to lowercase"):
                st.markdown("Try Again!")
        elif (q2 == "To display text on the screen"
              or q2 == "To convert numbers to strings"
              or q2 == "To create comments"):
            st.markdown("Try Again!")
    elif (q1 == "3 * 5"
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
    question2_1 = st.radio("What is the result of the expression 5 + 3 * 2 / 4 in Python?",
                     ("4.0",
                      "6.0",
                      "5.5",
                      "7.0"),
                     index=None,
                     key="q3"
                     )

    if question2_1 == "5.5":
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 2.2"
    elif question2_1 ==  "4.0" or question2_1 == "6.0" or question2_1 =="7.0":
        st.markdown("Try Again!")
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
    question2_2 = st.radio("In Python, what is the correct order of operations for evaluating expressions?", 
                    ("Division, Addition, Multiplication, Subtraction",
                     "Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)",
                     "Exponents, Parentheses, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)",
                     "Exponents, Parentheses, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)",
                     "Subtraction, Addition, Multiplication, Division"),
                    index=None, key="q3")
    if question2_2 == "Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)":
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 2.3"
    elif question2_2 =="Division, Addition, Multiplication, Subtraction" or question2_2 =="Exponents, Parentheses, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)" or question2_2 == "Subtraction, Addition, Multiplication, Division":
        st.markdown("Try Again!")
        

elif st.session_state.expandtitle == "Unit 2.3":
    st.title("Unit 2.3: Modules Explanation")

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
        |    *,/    |    Multiplication - multiplies, Division - divides, |
        |     //    |   Floor Division - removes decimal after division,  |
        |     %     |  Modulo - Provides remainder after division         |
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
    st.write(
        " These operators, in order of highest precedence to lowest, make up the majority of arithmetic operators used in python")
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
                                            if st.button("Next Unit!"):
                                                st.session_state.expandtitle = "Unit 3.1"

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
    st.header("Unit 3.1: If Statements, If-Else Statements, Logical Operators")

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
    st.header("Unit 3.2: Else If (elif) Statements")

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
    question3_2 = st.radio(
        "Which of the following shows an accurate if,elif,else structure for a system that decides promotions, demotions, or a raise based on ranges of average scores out of 10? (0-4 score for demotion, 4-7 score for a raise, and 8-10 for a promotion)",
        (
        "if score > 8: status = 'promotion', elif score > 3 and score < 6: status = 'raise', else: status = 'demotion'",
        "if score >= 8: status = 'promotion', else: status = 'demotion'",
        "elif score >= 8: status = 'promotion', if score >=4 and score <= 7: status = 'raise', else: status = 'demotion'",
        "if score >= 8: status = 'promotion', elif score >=4 and score <= 7: status = 'raise', else: status = 'demotion'"),
        index=None,
        )

    if (
            question3_2 == "if score >= 8: status = 'promotion', elif score >=4 and score <= 7: status = 'raise', else: status = 'demotion'"):
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 3.3"
    elif question3_2 == "if score > 8: status = 'promotion', elif score > 3 and score < 6: status = 'raise', else: status = 'demotion'" or question3_2 == "if score >= 8: status = 'promotion', else: status = 'demotion'" or question3_2 == "elif score >= 8: status = 'promotion', if score >=4 and score <= 7: status = 'raise', else: status = 'demotion'":
        st.markdown("Try Again!")
elif st.session_state.expandtitle == "Unit 3.3":
    st.header("Unit 3.3: Nested Conditionals")

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
    question3_3 = st.radio("Which of the following demonstrates an accurate nested conditional structure for a simple program regarding beverage preference along with temperature preference)”,
                         ("If-else statements selecting temperature within an outer if-else statement selecting beverage", "if beverage == tea: print(“Tea rocks!”) else: print(“Coffee is better”)", "if-else statements followed by if-else statements of the same level", "if-elif-else statements are nested conditionals"),
                         index=None,
                        )

    if (question3_3 == "If-else statements selecting temperature within an outer if-else statement selecting beverage"):
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 3.4”
    elif question3_3 == "if beverage == tea: print(“Tea rocks!”) else: print(“Coffee is better”)" or question3_3 == "if-else statements followed by if-else statements of the same level" or question3_3 == "if-elif-else statements are nested conditionals":
        st.markdown("Try Again!")
elif st.session_state.expandtitle == "Unit 3.4":
    st.title("Unit 3: Conditionals Summary")

    st.write(
        "Unit 3 explores the world of conditionals, which are used to make decisions and control the flow of a program.")

    # Subsection 3.1: If Statements
    st.header("3.1: If Statements")
    st.write("In this section, you learned about 'if' statements, the most basic form of conditional statements.")

    st.subheader("Key Points")
    st.write("1. 'if' statements evaluate a condition and execute a block of code if the condition is true.")
    st.write("2. Proper indentation is crucial to define the code block that belongs to the 'if' statement.")
    st.write("3. 'if' statements allow your program to make decisions based on specific conditions.")

    # Subsection 3.2: Else if Statements
    st.header("3.2: Else if Statements")
    st.write("Else if statements allow you to consider multiple conditions in a controlled manner.")

    st.subheader("Key Points")
    st.write("1. 'else if' statements (also written as 'elif') are used to specify alternative conditions.")
    st.write("2. They are evaluated only if the preceding 'if' or 'elif' conditions are false.")
    st.write("3. 'else' can be used as a final fallback condition if none of the previous conditions are met.")

    # Subsection 3.3: Nested Statements
    st.header("3.3: Nested Statements")
    st.write(
        "Nested statements involve placing one conditional statement within another, allowing for complex decision-making.")

    st.subheader("Key Points")
    st.write("1. Nested statements involve 'if' or 'elif' statements inside other 'if' or 'elif' blocks.")
    st.write("2. Proper indentation is crucial to indicate the nesting level.")
    st.write("3. Nested statements enable you to consider multiple conditions and execute code accordingly.")

    # Conclusion
    st.header("Conclusion")
    st.write("In Unit 3, you've explored conditionals, a fundamental aspect of programming.")
    st.write("You've learned how 'if' statements allow you to make decisions based on specific conditions.")
    st.write("Else if statements expand your decision-making capabilities by considering multiple conditions.")
    st.write("Nested statements provide a way to handle complex scenarios by combining conditionals.")
    st.write(
        "Understanding and mastering these conditional structures is essential for creating responsive and flexible programs.")

elif st.session_state.expandtitle == "Unit 3.5":
    st.header("Unit 3 Quiz")
    # Question 1
    q1 = st.radio("What is the purpose of an 'if' statement in Python?",
                  ("To iterate through a list",
                   "To make decisions based on conditions",
                   "To define a function",
                   "To print text to the console"),
                  index=None
                  )

    if q1 == "To make decisions based on conditions":
        st.markdown("Correct!")
        q2 = st.radio("What is the correct syntax for an 'if' statement in Python?",
                      ("if condition:",
                       "if (condition)",
                       "if [condition]",
                       "if {condition}"),
                      index=None
                      )
        if q2 == "if condition:":
            st.markdown("Correct!")
            q3 = st.radio("What does the 'elif' keyword represent in an 'if-elif-else' statement?",
                          ("It specifies an alternative condition to check if the previous conditions are False",
                           "It represents the main condition",
                           "It indicates the end of the statement",
                           "It is used for comments"),
                          index=None
                          )
            if q3 == "It specifies an alternative condition to check if the previous conditions are False":
                st.markdown("Correct!")
                q4 = st.radio("What is the primary role of 'else' in an 'if-elif-else' statement?",
                              ("It defines the main condition",
                               "It specifies an alternative condition",
                               "It is used for comments",
                               "It handles the final fallback condition if none of the previous conditions are met"),
                              index=None
                              )
                if q4 == "It handles the final fallback condition if none of the previous conditions are met":
                    st.markdown("Correct!")
                    q5 = st.radio("How are nested if statements used?",
                                  ("To combine multiple conditions within another condition",
                                   "To create a loop",
                                   "To define a function",
                                   "To print text to the console"),
                                  index=None
                                  )
                    if q5 == "To combine multiple conditions within another condition":
                        st.markdown("Correct!")
                        q6 = st.radio("What is the significance of proper indentation in nested if statements?",
                                      ("It has no significance",
                                       "It is used for aesthetic purposes",
                                       "It helps define the code block that belongs to each if statement",
                                       "It defines the order of execution"),
                                      index=None
                                      )
                        if q6 == "It helps define the code block that belongs to each if statement":
                            st.markdown("Correct!")
                            q7 = st.radio("What do nested if statements enable you to do?",
                                          ("Consider multiple conditions and execute code accordingly",
                                           "Print text to the console",
                                           "Define functions",
                                           "Create loops"),
                                          index=None
                                          )
                            if q7 == "Consider multiple conditions and execute code accordingly":
                                st.markdown("Correct!")
                                q8 = st.radio(
                                    "In a nested if statement, where should the nested 'if' or 'elif' blocks be indented?",
                                    ("They should be indented to the same level as the outer if statement",
                                     "They should not be indented",
                                     "They should be indented in reverse",
                                     "The level of indentation doesn't matter"),
                                    index=None
                                )
                                if q8 == "They should be indented to the same level as the outer if statement":
                                    st.markdown("Correct!")
                                    q9 = st.radio(
                                        "What kind of decision-making scenarios are nested if statements useful for?",
                                        ("Complex scenarios where multiple conditions need to be considered",
                                         "Simple scenarios with only one condition",
                                         "Scenarios involving loops",
                                         "Scenarios involving functions"),
                                        index=None
                                    )
                                    if q9 == "Complex scenarios where multiple conditions need to be considered":
                                        st.markdown("Correct!")
                                        q10 = st.radio("What is the primary purpose of 'elif' statements?",
                                                       (
                                                           "To specify an alternative condition to check if the previous conditions are False",
                                                           "To define the main condition",
                                                           "To indicate the end of the statement",
                                                           "To create loops"),
                                                       index=None
                                                       )
                                        if q10 == "To specify an alternative condition to check if the previous conditions are False":
                                            st.markdown("Correct!")
                                            if st.button("Next Unit!"):
                                                st.session_state.expandtitle = "Unit 4.1"

                                        elif (q10 == "To define the main condition"
                                              or q10 == "To indicate the end of the statement"
                                              or q10 == "To create loops"):
                                            st.markdown("Try Again!")
                                    elif (q9 == "Simple scenarios with only one condition"
                                          or q9 == "Scenarios involving loops"
                                          or q9 == "Scenarios involving functions"):
                                        st.markdown("Try Again!")
                                elif (q8 == "They should not be indented"
                                      or q8 == "They should be indented in reverse"
                                      or q8 == "The level of indentation doesn't matter"):
                                    st.markdown("Try Again!")
                            elif (q7 == "Print text to the console"
                                  or q7 == "Define functions"
                                  or q7 == "Create loops"):
                                st.markdown("Try Again!")
                        elif (q6 == "It has no significance"
                              or q6 == "It is used for aesthetic purposes"
                              or q6 == "It defines the order of execution"):
                            st.markdown("Try Again!")
                    elif (q5 == "To create a loop"
                          or q5 == "To define a function"
                          or q5 == "To print text to the console"):
                        st.markdown("Try Again!")
                elif (q4 == "It defines the main condition"
                      or q4 == "It specifies an alternative condition"
                      or q4 == "It is used for comments"):
                    st.markdown("Try Again!")
            elif (q3 == "It represents the main condition"
                  or q3 == "It indicates the end of the statement"
                  or q3 == "It is used for comments"):
                st.markdown("Try Again!")
        elif (q2 == "if (condition)"
              or q2 == "if [condition]"
              or q2 == "if {condition}"):
            st.markdown("Try Again!")
    elif (q1 == "To iterate through a list"
          or q1 == "To define a function"
          or q1 == "To print text to the console"):
        st.markdown("Try Again!")

elif st.session_state.expandtitle == "Unit 4.1":
    st.header("Unit 4.1: For Loops")
    st.write(
        "For loops are used for iterating over sequences (such as lists, tuples, or strings) and performing actions on each item in the sequence.")

    # Example of a for loop
    st.write("Example:")
    st.code("""
        fruits = ["Apple", "Banana", "Cherry"]
        for fruit in fruits:
            st.write(f"Current fruit: {fruit}")
        """, language='python')
    st.write(
        "In this example, we have a list of fruits, and we use a for loop to iterate through each fruit and print its name.")

    st.write("Key points about for loops:")

    st.subheader("Iteration Over Sequences")
    st.write("For loops are commonly used to iterate over sequences like lists, tuples, or strings.")

    st.subheader("Iterable Element")
    st.write(
        "The loop variable (e.g., 'fruit' in the example) takes on each item in the sequence during each iteration.")

    st.subheader("Indentation")
    st.write("Proper indentation is crucial to indicate the code block that should be executed for each iteration.")

    st.subheader("Loop Control")
    st.write("You can use control statements like 'break' and 'continue' to control the flow of the loop.")

    st.write("For loops are fundamental for performing repetitive tasks in programming.")

    # Conclusion
    st.header("Conclusion")
    st.write(
        "In this unit, you've learned about for loops, which are essential for iterating over sequences and performing actions on each element.")
    st.write(
        "For loops are versatile and commonly used in programming for tasks like data processing and repetitive actions.")
    st.write("Understanding how to use for loops effectively is crucial for writing efficient and structured code.")

elif st.session_state.expandtitle == "Unit 4.2":
    st.header("Unit 4.2: While Loops")

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

    st.write(
        "Unit 4 explores the concept of loops, which are used to perform repetitive tasks and iterate through data structures.")

    # Subsection 4.1: While Loops
    st.header("4.1: While Loops")
    st.write(
        "In this section, you learned about 'while' loops, which repeatedly execute a block of code as long as a condition is true.")

    st.subheader("Key Points")
    st.write("1. 'while' loops continue executing as long as the specified condition remains true.")
    st.write("2. Proper indentation is crucial to define the code block that belongs to the 'while' loop.")
    st.write("3. 'while' loops are useful when you don't know the number of iterations in advance.")

    # Subsection 4.2: For Loops
    st.header("4.2: For Loops")
    st.write("For loops are used to iterate through sequences and perform actions on each item in the sequence.")

    st.subheader("Key Points")
    st.write("1. For loops are commonly used for iterating over sequences like lists, tuples, or strings.")
    st.write("2. A loop variable takes on each item in the sequence during each iteration.")
    st.write("3. Proper indentation is crucial to define the code block within the loop.")

    # Subsection 4.3: Nested For-Loops
    st.header("4.3: Nested For-Loops")
    st.write(
        "Nested for-loops involve placing one for-loop inside another, enabling complex iteration and data processing.")

    st.subheader("Key Points")
    st.write("1. Nested for-loops involve one for-loop within another, creating a nested structure.")
    st.write("2. Proper indentation indicates the level of nesting.")
    st.write("3. Nested for-loops are used for tasks like matrix traversal and multi-dimensional data processing.")

    # Conclusion
    st.header("Conclusion")
    st.write("In Unit 4, you've explored the concept of loops, a fundamental aspect of programming.")
    st.write("While loops allow you to repeat code execution based on a condition.")
    st.write("For loops simplify the process of iterating through sequences like lists.")
    st.write("Nested for-loops enable you to work with complex data structures and perform multi-level iterations.")
    st.write(
        "Mastering loops is crucial for automating repetitive tasks and processing data efficiently in your programs.")

elif st.session_state.expandtitle == "Unit 4.5":
    st.header("Unit 4 Quiz")
    q1 = st.radio("What is the purpose of a 'for' loop in Python?",
                  ("To make decisions based on conditions",
                   "To create a loop",
                   "To define a function",
                   "To print text to the console"),
                  index=None
                  )

    if q1 == "To create a loop":
        st.markdown("Correct!")
        q2 = st.radio("Which of the following is NOT a key point about 'while' loops?",
                      ("They continue executing as long as the specified condition remains true",
                       "Proper indentation is crucial to define the code block within the loop",
                       "They are useful when you know the exact number of iterations",
                       "They repeatedly execute a block of code as long as a condition is true"),
                      index=None
                      )
        if q2 == "They are useful when you know the exact number of iterations":
            st.markdown("Correct!")
            q3 = st.radio("What is the primary purpose of 'break' and 'continue' statements in loops?",
                          ("To define the main condition",
                           "To specify an alternative condition",
                           "To control the flow of the loop",
                           "To create loops"),
                          index=None
                          )
            if q3 == "To control the flow of the loop":
                st.markdown("Correct!")
                q4 = st.radio("What kind of tasks are 'while' loops particularly useful for?",
                              ("Tasks where you don't know the number of iterations in advance",
                               "Tasks with known and fixed numbers of iterations",
                               "Tasks involving multi-dimensional data",
                               "Tasks involving matrix traversal"),
                              index=None
                              )
                if q4 == "Tasks where you don't know the number of iterations in advance":
                    st.markdown("Correct!")
                    q5 = st.radio("In a 'for' loop, what does the loop variable do?",
                                  ("It specifies the alternative condition to check",
                                   "It defines the main condition",
                                   "It takes on each item in the sequence during each iteration",
                                   "It is used for comments"),
                                  index=None
                                  )
                    if q5 == "It takes on each item in the sequence during each iteration":
                        st.markdown("Correct!")
                        q6 = st.radio("What does proper indentation indicate in loops?",
                                      ("It has no significance",
                                       "It is used for aesthetic purposes",
                                       "It defines the order of execution",
                                       "It indicates the code block that belongs to the loop"),
                                      index=None
                                      )
                        if q6 == "It indicates the code block that belongs to the loop":
                            st.markdown("Correct!")
                            q7 = st.radio("What is the primary purpose of nested loops?",
                                          ("To make the code more complex",
                                           "To simplify code execution",
                                           "To perform repetitive tasks within repetitive tasks",
                                           "To create loops"),
                                          index=None
                                          )
                            if q7 == "To perform repetitive tasks within repetitive tasks":
                                st.markdown("Correct!")
                                q8 = st.radio(
                                    "What type of tasks are nested loops often used for?",
                                    ("Tasks involving simple iterations",
                                     "Tasks where you need to repeat an action until a certain condition is met",
                                     "Tasks with a single loop",
                                     "Tasks where you don't need to iterate"),
                                    index=None
                                )
                                if q8 == "Tasks involving simple iterations":
                                    st.markdown("Correct!")
                                    q9 = st.radio(
                                        "What is the order of execution in nested loops?",
                                        ("The inner loop runs completely for each iteration of the outer loop",
                                         "The outer loop runs completely for each iteration of the inner loop",
                                         "Both loops run in parallel",
                                         "The inner loop executes first, followed by the outer loop"),
                                        index=None
                                    )
                                    if q9 == "The inner loop runs completely for each iteration of the outer loop":
                                        st.markdown("Correct!")
                                        q10 = st.radio("What is a common use case for nested loops?",
                                                       (
                                                           "Matrix traversal and working with multi-dimensional data",
                                                           "Simple data processing tasks",
                                                           "Creating loops within functions",
                                                           "Printing text to the console"),
                                                       index=None
                                                       )
                                        if q10 == "Matrix traversal and working with multi-dimensional data":
                                            st.markdown("Correct!")

                                            if st.button("Next Unit!"):
                                                st.session_state.expandtitle = "Unit 5.1"

                                        elif (q10 == "Simple data processing tasks"
                                              or q10 == "Creating loops within functions"
                                              or q10 == "Printing text to the console"):
                                            st.markdown("Try Again!")
                                    elif (q9 == "The outer loop runs completely for each iteration of the inner loop"
                                          or q9 == "Both loops run in parallel"
                                          or q9 == "The inner loop executes first, followed by the outer loop"):
                                        st.markdown("Try Again!")
                                elif (q8 == "Tasks where you need to repeat an action until a certain condition is met"
                                      or q8 == "Tasks with a single loop"
                                      or q8 == "Tasks where you don't need to iterate"):
                                    st.markdown("Try Again!")
                            elif (q7 == "To make the code more complex"
                                  or q7 == "To simplify code execution"
                                  or q7 == "To create loops"):
                                st.markdown("Try Again!")
                        elif (q6 == "It has no significance"
                              or q6 == "It is used for aesthetic purposes"
                              or q6 == "It defines the order of execution"):
                            st.markdown("Try Again!")
                    elif (q5 == "It specifies the alternative condition to check"
                          or q5 == "It defines the main condition"
                          or q5 == "It is used for comments"):
                        st.markdown("Try Again!")
                elif (q4 == "Tasks with known and fixed numbers of iterations"
                      or q4 == "Tasks involving multi-dimensional data"
                      or q4 == "Tasks involving matrix traversal"):
                    st.markdown("Try Again!")
            elif (q3 == "To define the main condition"
                  or q3 == "To specify an alternative condition"
                  or q3 == "To create loops"):
                st.markdown("Try Again!")
        elif (q2 == "They continue executing as long as the specified condition remains true"
              or q2 == "Proper indentation is crucial to define the code block within the loop"
              or q2 == "They repeatedly execute a block of code as long as a condition is true"):
            st.markdown("Try Again!")
    elif (q1 == "To make decisions based on conditions"
          or q1 == "To define a function"
          or q1 == "To print text to the console"):
        st.markdown("Try Again!")
elif st.session_state.expandtitle == "Unit 5.1":
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

    #
    st.header("Conclusion")
    st.write(
        "Lists are an essential data structure in programming, allowing you to store and manipulate collections of data efficiently.")
    st.write("You've also seen some common functions that can be used to modify and work with lists, "
             "such as appending elements, counting occurrences, sorting, and selecting random values.")
    st.write(
        "Mastering lists is crucial for a wide range of programming tasks, and they are widely used in various applications.")
    st.title("Unit 5.1: Lists Question")


    st.write("Which of the following best describes the purpose of lists in programming?")

    #
    question2 = st.text_input("Enter your answer here:")

    # Check user's answer
    if question2 == "To store multiple values within a single variable":
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 5.2"
    else:
        st.markdown("Try Again!")
elif st.session_state.expandtitle == "Unit 5.2":
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
    st.title("Unit 5.2: Lists Question")

    # Question
    st.write("What is the main purpose of traversing through lists in programming?")

    # User input field
    question2 = st.text_input("Enter your answer here:")

    # Check user's answer
    if question2 == "To iterate through a list and perform actions on each element":
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 5.3"
    else:
        st.markdown("Try Again!")
elif st.session_state.expandtitle == "Unit 5.3":
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
    st.title("Unit 5.3: Lists Question")

    # Question
    st.write("What is the primary purpose of appending and removing elements from lists in programming?")

    # User input field
    question2 = st.text_input("Enter your answer here:")

    # Check user's answer
    if question2 == "To modify the content of a list by adding or removing elements":
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 5.4"
    else:
        st.markdown("Try Again!")

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
    st.title("Unit 5: Lists Summary")

    st.write(
        "Unit 5 explores the world of lists, a versatile data structure used to store and manipulate collections of values.")

    # Subsection 5.1: Lists
    st.header("5.1: Lists")
    st.write(
        "In this section, you learned about lists, which are used to store multiple values within a single variable.")

    st.subheader("Key Points")
    st.write("1. Lists can hold values of any data type and can mix different data types in the same list.")
    st.write("2. Each value stored within a list is called an element.")
    st.write("3. Lists are useful for managing collections of data, such as numbers, strings, or even other lists.")

    # Subsection 5.2: Traversing through Lists
    st.header("5.2: Traversing through Lists")
    st.write("Traversing through lists involves accessing and processing each element in a list, often using loops.")

    st.subheader("Key Points")
    st.write(
        "1. Loops, like 'for' loops and 'while' loops, are used to iterate through lists and perform actions on each element.")
    st.write(
        "2. Traversing through lists allows you to process data, make calculations, or apply functions to list elements.")

    # Subsection 5.3: Appending/Removing
    st.header("5.3: Appending/Removing")
    st.write("Lists can be modified by adding or removing elements, making them dynamic data structures.")

    st.subheader("Key Points")
    st.write("1. The 'append' method adds an element to the end of a list.")
    st.write("2. You can use 'insert' to add an element at a specific position in the list.")
    st.write("3. 'remove' and 'pop' methods are used to remove elements from a list.")
    st.write("4. Modifying lists allows you to update data or control the list's content.")

    # Subsection 5.4: 2D Lists
    st.header("5.4: 2D Lists")
    st.write(
        "2D lists, or nested lists, are lists of lists, enabling the creation of multi-dimensional data structures.")

    st.subheader("Key Points")
    st.write("1. 2D lists contain lists as their elements, creating a grid-like structure.")
    st.write("2. Accessing elements in a 2D list involves specifying both row and column indices.")
    st.write("3. 2D lists are used for tasks like representing grids, matrices, and tables.")

    # Conclusion
    st.header("Conclusion")
    st.write("In Unit 5, you've explored the power of lists, a fundamental data structure in programming.")
    st.write("Lists allow you to store and manipulate collections of values, providing flexibility in data management.")
    st.write("Traversing through lists, appending, and removing elements enable dynamic data processing.")
    st.write(
        "2D lists expand your data modeling capabilities, making them essential for various applications in programming.")
elif st.session_state.expandtitle == "Unit 5.6":
    st.header("Unit 5 Quiz")
    q1 = st.radio("What is the purpose of a 'for' loop in Python?",
                  ("To make decisions based on conditions",
                   "To create a loop",
                   "To define a function",
                   "To print text to the console"),
                  index=None
                  )
    if q1 == "To create a loop":
        st.markdown("Correct!")
        q2 = st.radio("Which of the following is NOT a key point about 'while' loops?",
                      ("They continue executing as long as the specified condition remains true",
                       "Proper indentation is crucial to define the code block within the loop",
                       "They are useful when you know the exact number of iterations",
                       "They repeatedly execute a block of code as long as a condition is true"),
                      index=None
                      )
        if q2 == "They are useful when you know the exact number of iterations":
            st.markdown("Correct!")
            q3 = st.radio("What is the primary purpose of 'break' and 'continue' statements in loops?",
                          ("To define the main condition",
                           "To specify an alternative condition",
                           "To control the flow of the loop",
                           "To create loops"),
                          index=None
                          )
            if q3 == "To control the flow of the loop":
                st.markdown("Correct!")
                q4 = st.radio("What kind of tasks are 'while' loops particularly useful for?",
                              ("Tasks where you don't know the number of iterations in advance",
                               "Tasks with known and fixed numbers of iterations",
                               "Tasks involving multi-dimensional data",
                               "Tasks involving matrix traversal"),
                              index=None
                              )
                if q4 == "Tasks where you don't know the number of iterations in advance":
                    st.markdown("Correct!")
                    q5 = st.radio("In a 'for' loop, what does the loop variable do?",
                                  ("It specifies the alternative condition to check",
                                   "It defines the main condition",
                                   "It takes on each item in the sequence during each iteration",
                                   "It is used for comments"),
                                  index=None
                                  )
                    if q5 == "It takes on each item in the sequence during each iteration":
                        st.markdown("Correct!")
                        q6 = st.radio("What does proper indentation indicate in loops?",
                                      ("It has no significance",
                                       "It is used for aesthetic purposes",
                                       "It defines the order of execution",
                                       "It indicates the code block that belongs to the loop"),
                                      index=None
                                      )
                        if q6 == "It indicates the code block that belongs to the loop":
                            st.markdown("Correct!")
                            q7 = st.radio("What is the primary purpose of nested loops?",
                                          ("To make the code more complex",
                                           "To simplify code execution",
                                           "To perform repetitive tasks within repetitive tasks",
                                           "To create loops"),
                                          index=None
                                          )
                            if q7 == "To perform repetitive tasks within repetitive tasks":
                                st.markdown("Correct!")
                                q8 = st.radio(
                                    "What type of tasks are nested loops often used for?",
                                    ("Tasks involving simple iterations",
                                     "Tasks where you need to repeat an action until a certain condition is met",
                                     "Tasks with a single loop",
                                     "Tasks where you don't need to iterate"),
                                    index=None
                                )
                                if q8 == "Tasks involving simple iterations":
                                    st.markdown("Correct!")
                                    q9 = st.radio(
                                        "What is the order of execution in nested loops?",
                                        ("The inner loop runs completely for each iteration of the outer loop",
                                         "The outer loop runs completely for each iteration of the inner loop",
                                         "Both loops run in parallel",
                                         "The inner loop executes first, followed by the outer loop"),
                                        index=None
                                    )
                                    if q9 == "The inner loop runs completely for each iteration of the outer loop":
                                        st.markdown("Correct!")
                                        q10 = st.radio("What is a common use case for nested loops?",
                                                       (
                                                           "Matrix traversal and working with multi-dimensional data",
                                                           "Simple data processing tasks",
                                                           "Creating loops within functions",
                                                           "Printing text to the console"),
                                                       index=None
                                                       )
                                        if q10 == "Matrix traversal and working with multi-dimensional data":
                                            st.markdown("Correct!")
                                            if st.button("Next Unit!"):
                                                st.session_state.expandtitle = "Unit 6.1"
                                        elif (q10 == "Simple data processing tasks"
                                              or q10 == "Creating loops within functions"
                                              or q10 == "Printing text to the console"):
                                            st.markdown("Try Again!")
                                    elif (q9 == "The outer loop runs completely for each iteration of the inner loop"
                                          or q9 == "Both loops run in parallel"
                                          or q9 == "The inner loop executes first, followed by the outer loop"):
                                        st.markdown("Try Again!")
                                elif (q8 == "Tasks where you need to repeat an action until a certain condition is met"
                                      or q8 == "Tasks with a single loop"
                                      or q8 == "Tasks where you don't need to iterate"):
                                    st.markdown("Try Again!")
                            elif (q7 == "To make the code more complex"
                                  or q7 == "To simplify code execution"
                                  or q7 == "To create loops"):
                                st.markdown("Try Again!")
                        elif (q6 == "It has no significance"
                              or q6 == "It is used for aesthetic purposes"
                              or q6 == "It defines the order of execution"):
                            st.markdown("Try Again!")
                    elif (q5 == "It specifies the alternative condition to check"
                          or q5 == "It defines the main condition"
                          or q5 == "It is used for comments"):
                        st.markdown("Try Again!")
                elif (q4 == "Tasks with known and fixed numbers of iterations"
                      or q4 == "Tasks involving multi-dimensional data"
                      or q4 == "Tasks involving matrix traversal"):
                    st.markdown("Try Again!")
            elif (q3 == "To define the main condition"
                  or q3 == "To specify an alternative condition"
                  or q3 == "To create loops"):
                st.markdown("Try Again!")
        elif (q2 == "They continue executing as long as the specified condition remains true"
              or q2 == "Proper indentation is crucial to define the code block within the loop"
              or q2 == "They repeatedly execute a block of code as long as a condition is true"):
            st.markdown("Try Again!")
    elif (q1 == "To make decisions based on conditions"
          or q1 == "To define a function"
          or q1 == "To print text to the console"):
        st.markdown("Try Again!")

elif st.session_state.expandtitle == "Unit 6.1":
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
    st.title("Unit 6.3: Returning Values in Functions Question")

    # Question
    st.write("What is the purpose of returning values from functions in programming?")

    # Multiple-choice options
    options = ["To allow functions to produce results and provide output to the caller.",
               "To determine the order of execution in a program.",
               "To define the name of the function.",
               "To pass data into a function when it is called."]

    # Radio buttons for options
    selected_option = st.radio("Select the correct option:", options)

    # Check if the selected option is correct
    if selected_option == options[0]:
        st.markdown("Correct!")
        if st.button("Next Section"):
            st.session_state.expandtitle = "Unit 4.1"
    else:
        st.markdown("Try Again!")
elif st.session_state.expandtitle == "Unit 6.4":

    st.title("Unit 6: Functions Summary")

    st.write(
        "Unit 6 explores the concept of functions, which are essential for organizing code and creating reusable blocks of logic.")

    # Subsection 6.1: Function Declaration
    st.header("6.1: Function Declaration")
    st.write(
        "In this section, you learned how to declare functions, which are named blocks of code that can be called and reused.")

    st.subheader("Key Points")
    st.write("1. Functions are declared using the 'def' keyword followed by a function name and parentheses.")
    st.write("2. Function names should be descriptive and follow naming conventions.")
    st.write("3. Functions are defined by a code block that performs specific tasks when the function is called.")

    # Subsection 6.2: Parameters
    st.header("6.2: Parameters")
    st.write("Parameters allow you to pass data into functions, making them flexible and versatile.")

    st.subheader("Key Points")
    st.write("1. Parameters are defined inside the parentheses of a function declaration.")
    st.write("2. Parameters act as placeholders for data that will be provided when the function is called.")
    st.write("3. Functions can have multiple parameters, and you can specify default values for them.")

    # Subsection 6.3: Returning Values in Functions
    st.header("6.3: Returning Values in Functions")
    st.write("Functions can return values, allowing them to produce results and data that can be used in your code.")

    st.subheader("Key Points")
    st.write("1. Use the 'return' statement to send a value back from a function.")
    st.write("2. The data type of the return value can be specified, and functions can return various data types.")
    st.write("3. Returned values are useful for performing calculations, making decisions, or storing results.")

    st.header("Conclusion")
    st.write("In Unit 6, you've explored the concept of functions, a crucial building block in programming.")
    st.write("Function declaration allows you to define reusable blocks of code.")
    st.write("Parameters make functions flexible by accepting input data.")
    st.write("Returning values from functions allows you to obtain results and use them in your programs.")
    st.write("By mastering functions, you can write modular, organized, and efficient code.")
elif st.session_state.expandtitle == "Unit 6.5":
    st.header("Unit 6 Quiz")

    q1 = st.radio("What is the primary purpose of a function in programming?",
                  ("To create loops",
                   "To make decisions based on conditions",
                   "To perform a specific task or set of tasks",
                   "To define a variable"),
                  index=None
                  )
    if q1 == "To perform a specific task or set of tasks":
        st.markdown("Correct!")
        q2 = st.radio("What is a function declaration?",
                      ("A statement that defines a variable",
                       "A reusable block of code that performs a specific task",
                       "A way to create conditions",
                       "A data type in Python"),
                      index=None
                      )
        if q2 == "A reusable block of code that performs a specific task":
            st.markdown("Correct!")
            q3 = st.radio("What are parameters in a function?",
                          ("Values that the function returns",
                           "Variables used inside a function",
                           "Values that the function accepts as input",
                           "The name of the function"),
                          index=None
                          )
            if q3 == "Values that the function accepts as input":
                st.markdown("Correct!")
                q4 = st.radio("What does the 'return' statement do in a function?",
                              ("It defines the main condition of the function",
                               "It specifies the alternative condition to check",
                               "It sends a value back from the function",
                               "It creates a loop within the function"),
                              index=None
                              )
                if q4 == "It sends a value back from the function":
                    st.markdown("Correct!")
                    q5 = st.radio("Can a function have multiple parameters?",
                                  ("Yes, but they must be enclosed in square brackets",
                                   "No, a function can have only one parameter",
                                   "Yes, they can be separated by commas",
                                   "No, a function cannot have any parameters"),
                                  index=None
                                  )
                    if q5 == "Yes, they can be separated by commas":
                        st.markdown("Correct!")
                        q6 = st.radio("What is a default value for a parameter in a function?",
                                      ("A value that is required to call the function",
                                       "A value that is automatically assigned to the parameter if no value is provided when calling the function",
                                       "A value that cannot be changed",
                                       "A value that is returned by the function"),
                                      index=None
                                      )
                        if q6 == "A value that is automatically assigned to the parameter if no value is provided when calling the function":
                            st.markdown("Correct!")
                            q7 = st.radio("What is the purpose of returning values in functions?",
                                          ("To make the function more complex",
                                           "To provide results that can be used in other parts of the program",
                                           "To define multiple conditions within a function",
                                           "To create loops within functions"),
                                          index=None
                                          )
                            if q7 == "To provide results that can be used in other parts of the program":
                                st.markdown("Correct!")
                                q8 = st.radio("What is the data type of a returned value in a function?",
                                              ("It can only be an integer",
                                               "It must be a string",
                                               "It can be any data type",
                                               "It must be a list"),
                                              index=None
                                              )
                                if q8 == "It can be any data type":
                                    st.markdown("Correct!")
                                    q9 = st.radio("What happens if a function does not have a 'return' statement?",
                                                  ("The function returns the value 'None'",
                                                   "The function cannot be called",
                                                   "The function raises an error",
                                                   "The function returns an empty string"),
                                                  index=None
                                                  )
                                    if q9 == "The function returns the value 'None'":
                                        st.markdown("Correct!")
                                        q10 = st.radio("What is the main benefit of using functions in programming?",
                                                       (
                                                           "To make the code longer and more complex",
                                                           "To avoid using parameters",
                                                           "To organize and reuse code, making it more modular and readable",
                                                           "To create nested loops"),
                                                       index=None
                                                       )
                                        if q10 == "To organize and reuse code, making it more modular and readable":
                                            st.markdown("Correct!")
                                            if st.button("Next Unit!"):
                                                st.session_state.expandtitle = "Unit 7.1"
                                        elif (q10 == "To make the code longer and more complex"
                                              or q10 == "To avoid using parameters"
                                              or q10 == "To create nested loops"):
                                            st.markdown("Try Again!")
                                    elif (q9 == "The function cannot be called"
                                          or q9 == "The function raises an error"
                                          or q9 == "The function returns an empty string"):
                                        st.markdown("Try Again!")
                                elif (q8 == "It must be a string"
                                      or q8 == "It can only be an integer"
                                      or q8 == "It must be a list"):
                                    st.markdown("Try Again!")
                            elif (q7 == "To make the function more complex"
                                  or q7 == "To define multiple conditions within a function"
                                  or q7 == "To create loops within functions"):
                                st.markdown("Try Again!")
                        elif (q6 == "A value that is required to call the function"
                              or q6 == "A value that cannot be changed"
                              or q6 == "A value that is returned by the function"):
                            st.markdown("Try Again!")
                    elif (q5 == "No, a function can have only one parameter"
                          or q5 == "No, a function cannot have any parameters"):
                        st.markdown("Try Again!")
                elif (q4 == "It defines the main condition of the function"
                      or q4 == "It specifies the alternative condition to check"
                      or q4 == "It creates a loop within the function"):
                    st.markdown("Try Again!")
            elif (q3 == "Values that the function returns"
                  or q3 == "Variables used inside a function"
                  or q3 == "The name of the function"):
                st.markdown("Try Again!")
        elif (q2 == "A way to create conditions"
              or q2 == "A data type in Python"):
            st.markdown("Try Again!")
    elif (q1 == "To create loops"
          or q1 == "To make decisions based on conditions"
          or q1 == "To define a variable"):
        st.markdown("Try Again!")

elif st.session_state.expandtitle == "Unit 7.1":
    st.header("Recap")
    st.title("Recap of Key Concepts")


    st.header("Unit 1: Introduction")
    st.subheader("1.1: Hello World")
    st.write("Your first step in programming, writing and running a basic 'Hello World' program.")

    st.subheader("1.2: Syntax and Formatting Conventions")
    st.write("Understanding proper code formatting and syntax for readable and error-free code.")

    st.subheader("1.3: Variables and Naming Conventions")
    st.write("Introduction to variables and the importance of clear naming conventions.")

    st.subheader("1.4: Printing and Input")
    st.write("Learning how to display information using 'print' and obtain user input.")

    st.subheader("1.5: Data Types")
    st.write("Exploring fundamental data types like integers, floats, strings, and booleans.")


    st.header("Unit 2: Math")
    st.subheader("2.1: Basic Symbols")
    st.write("Covering basic mathematical symbols for addition, subtraction, multiplication, division, and exponentiation.")

    st.subheader("2.2: Order of Operations")
    st.write("Exploring the order of operations (PEMDAS/BODMAS) for correct mathematical calculations.")

    st.subheader("2.3: Modules")
    st.write("Introduction to modules like 'math' and 'random' for advanced mathematical operations and randomness.")


    st.header("Unit 3: Conditionals")
    st.subheader("3.1: If Statements")
    st.write("Learning to use 'if' statements to make decisions based on conditions.")

    st.subheader("3.2: Else if Statements")
    st.write("Exploring 'else if' statements to consider multiple conditions in a controlled manner.")

    st.subheader("3.3: Nested Statements")
    st.write("Introduction to nested statements, allowing complex decision-making.")


    st.header("Unit 4: Loops")
    st.subheader("4.1: While Loops")
    st.write("Covering 'while' loops for executing code repeatedly as long as a condition is true.")

    st.subheader("4.2: For Loops")
    st.write("Exploring 'for' loops, useful for iterating through sequences like lists.")

    st.subheader("4.3: Nested For-Loops")
    st.write("Introduction to nested for-loops for multi-level iterations and complex data processing.")


    st.header("Unit 5: Lists")
    st.subheader("5.1: Lists")
    st.write("Learning about lists, versatile data structures for storing multiple values.")

    st.subheader("5.2: Traversing Through Lists")
    st.write("Exploring ways to iterate through lists, performing actions on each element.")

    st.subheader("5.3: Appending/Removing")
    st.write("Covering modifying lists by adding or removing elements.")

    st.subheader("5.4: 2D Lists")
    st.write("Introduction to 2D lists, used for representing multi-dimensional data.")


    st.header("Unit 6: Functions")
    st.subheader("6.1: Function Declaration")
    st.write("Learning how to declare and define functions, encapsulating reusable blocks of code.")

    st.subheader("6.2: Parameters")
    st.write("Exploring the use of parameters to pass data into functions, enhancing their flexibility.")

    st.subheader("6.3: Returning Values in Functions")
    st.write("Covering returning values from functions, allowing them to produce results.")

elif st.session_state.expandtitle == "Unit 7.2":
    st.header("Final Exam")

    questions = [
        {
            'unit': "Unit 1: Intro",
            'question': "Write a Python comment that says comment.",
            'expected_answer': "# comment"
        },
        {
            'unit': "Unit 2: Math Operators",
            'question': "Write Python code to calculate the sum of two numbers, 5 and 3.",
            'expected_answer': "5 + 3"
        },
        {
            'unit': "Unit 3: Conditionals",
            'question': "Write an 'if' statement that checks if a variable 'x' is greater than 10.",
            'expected_answer': "if x > 10:"
        },
        {
            'unit': "Unit 4: Loops",
            'question': "Write a 'for' loop that iterates through a list named 'numbers'.",
            'expected_answer': "for number in numbers:"
        },
        {
            'unit': "Unit 5: Lists",
            'question': "Write Python code to add an element 'apple' to a list named 'fruits'.",
            'expected_answer': "fruits.append('apple')"
        },
        {
            'unit': "Unit 6: Functions",
            'question': "Write a function named 'multiply' that takes two arguments, 'a' and 'b', and returns their product.",
            'expected_answer': "def multiply(a, b):\n    return a * b"
        }
    ]

    question_number = st.session_state.question_number

    if question_number < len(questions):
        current_question = questions[question_number]
        st.subheader(f"Question {question_number + 1} ({current_question['unit']})")
        st.write(current_question['question'])
        user_answer = st.text_input("Your Answer:")

        if user_answer and user_answer.strip() == current_question['expected_answer']:
            st.markdown("Correct! Your answer matches the expected response.")
            st.session_state.question_number += 1
        elif user_answer:
            st.markdown("Incorrect. Please try again.")

    if question_number >= len(questions):
        st.header("Congratulations! You've completed the final exam.")


elif st.session_state.expandtitle == "Flashcards":
    st.header("Flashcards")

    if 'flashcards' not in st.session_state:
        st.session_state.flashcards = {}


    st.subheader("Create Flashcards")
    term = st.text_input("Term:")
    definition = st.text_input("Definition:")
    if st.button("Add Flashcard"):
        if term and definition:
            st.session_state.flashcards[term] = definition
            st.success("Flashcard added successfully!")


    st.subheader("Your Flashcards")

    if not st.session_state.flashcards:
        st.info("No flashcards created yet. Use the input fields above to add flashcards.")
    else:
        for term, definition in st.session_state.flashcards.items():
            st.write(f"**Term:** {term}")
            st.write(f"**Definition:** {definition}")

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

        st.link_button("Syllabus",
                       "https://docs.google.com/document/d/18pOZAv8kwUpfFii0ko1iciQv3-eyxOmcmdLVdaqvjVg/edit?usp=sharing")

        # Footer
        st.write("Thank you for choosing eduPY. We wish you success in your Python development endeavors!")

    with tab3:
        st.title("About eduPY")
        st.markdown("## Welcome to eduPY – Your Gateway to Python Education!")

        st.write("At eduPY, we are passionate about spreading the knowledge and power of Python programming "
                 "to learners of all levels, from beginners taking their first steps in coding to seasoned "
                 "developers looking to enhance their skills. Our mission is to make Python education accessible, "
                 "engaging, and effective.")

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

