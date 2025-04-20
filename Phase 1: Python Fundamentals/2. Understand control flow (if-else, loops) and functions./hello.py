# if-else statements
# script that checks if a user’s age is 18 or older and prints a message
age = int(input("Enter your age: "))
if age > 18:
    print("You are an adult.")
elif age == 18: # else if
    print("You just became an adult!")
else:
    print("You are a minor.")


# for and while loops
# loop that prints numbers from 1 to 5
for i in range(1, 6):
    print(i) # The range function in Python generates a sequence of numbers starting from the first argument (inclusive) up to, but not including, the second argument (exclusive).
# loop that prints each movie in a list
movies = ["Inception", "Interstellar", "The Matrix"]
for movie in movies:
    print(movie)

# use while loop to print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
# asks the user to guess a number between 1 and 5, it keeps asking until the correct number is guessed.
secret = 3
guess = 0
while guess != secret:
    guess = int(input("Guess a number (1-5): "))
    if guess != secret:
        print("Try again!")
print("You guessed it!")


# functions
# function that prints a greeting w/ parameter
def greet(name):
    print(f"Hello, {name}!")
user_name = input("Enter your name: ")
greet(user_name)
# function that calculates and returns the square of a number
def square(n):
    return n * n
result = square(4)
print("Square:", result)


# mini-project
# asks for a number, checks if it's even or odd using a function, prints a message repeatedly until they enter 0
def is_even(n):
    return n % 2 == 0
number = int(input("Enter a number: "))
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# modify previous code to ask the user repeatedly (using a loop) until they enter 0
while True:
    number = int(input("Enter a number (0 to exit): "))
    if number == 0:
        print("Exiting program...")
        break
    elif is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")