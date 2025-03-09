# can run this by clicking the play button in the top right corner

# print() is a built-in function in Python that prints the specified message to the screen
print("Hello, Python!")

# Variables and Data Types in Python
name = "Alice"  # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>
print(type(is_student))  # <class 'bool'>

# script to ask for user input
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")


# in terminal, type python to run the python shell
# type print("This is interactive mode!"), then press enter
# type exit() or ctrl + d to exit the shell


# Simple Practice Exercises:
# Create a script that asks for the user's age and prints it.
age = input("Please enter your age: ")
print(f"Your age is {age}")

# Declare three variables (name, age, country) and print them in a sentence.
name = "John"
age = 30
country = "USA"
print(f"My name is {name}, I am {age} years old, and I live in {country}.")

# Check the type of a variable using type()
print(f"The type of the variable 'name' is {type(name)}")
print(f"The type of the variable 'age' is {type(age)}")
print(f"The type of the variable 'country' is {type(country)}")
