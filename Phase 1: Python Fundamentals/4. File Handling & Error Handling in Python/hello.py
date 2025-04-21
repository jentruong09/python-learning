# opening a file
file = open("Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/example.txt", "r")

# reading the file
file = open("Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/example.txt", "r")
content = file.read()  
print(content)
file.close()

# Practice Task: Create a file named "data.txt" with some text. Open and read it.
with open("Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/data.txt", "r") as file:
    content = file.read()
    print(content)


# writing to a file 
file = open("Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/example.txt", "w")
file.write("Hello, World!")  # writing to the file
file.close()  # closing the file

# Practice Task: Write "Learning Python is fun!" to a file.
file = open("Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/data.txt", "w")
file.write("Learning Python is fun!")  # writing to the file
file.close()  # closing the file


# appending to a file
file = open("Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/text.txt", "a")
file.write("\nLet's keep learning!")
file.close()

# Practice Task: Append "Keep going!" to the file.
file = open("Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/new.txt", "a")
file.write("\nKeep going!")  # appending to the file


# using with statement
with open("Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/example.txt", "r") as file:
    content = file.read()
    print(content)  # file automatically closes after this block

# Practice Task: Read a file using with open() method.
with open("Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/data.txt", "r") as file:
    content = file.read()
    print(content)  # file automatically closes after this block

# handling multiple errors
try:
    num = int("abc")  # Error: Cannot convert string to int
except ValueError:
    print("Invalid input!")

# Practice Task: Handle the error when a user enters a non-integer value.
try:
    num = int(input("Enter a number: "))  # Error: Cannot convert string to int
except ValueError:
    print("Invalid input! Please enter a valid integer.")


# using finally block
try:
    file = open("Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This will always run.")

# Practice Task: Try to open a non-existent file and handle the error.
try:
    file = open("Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/non_existent.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found! Please check the file name and path.")
finally:
    print("This will always run.")


# raising errors
# age = -5
# if age < 0:
#     raise ValueError("Age cannot be negative!")

# Practice Task: Raise an error if the user enters a negative number.
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative! Please enter a valid age.")


# Final Challenge: Asks for a filename. Tries to open the file. If the file does not exist, catch the error and create it. If the file exists, read and print its content.
filename = input("Enter the filename: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"{filename} not found. Creating the file.")
    with open(filename, "w") as file:
        file.write("This is a new file created because the original was not found.")
        print(f"{filename} has been created.")
# Phase 1: Python Fundamentals/4. File Handling & Error Handling in Python/final.txt <- paste this