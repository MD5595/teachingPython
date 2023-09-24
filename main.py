import streamlit as st
import math
import random
from account import account_manager


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
elif st.session_state.expandtitle == "Unit 2.2":
    # Title of the web app
    st.title("Order of Operations in Python")

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
elif st.session_state.expandtitle == "Unit 2.5":
    st.header("Unit 2 Quiz")

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
