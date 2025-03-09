# Lists: Ordered, Mutable Collections
# creating list
fruits = ["apple", "banana", "cherry"] 
numbers = [1, 2, 3, 4, 5] 
mixed = [1, "hello", 3.5, True]

# accessing elements
print(fruits[0])  # First item: apple 
print(fruits[-1]) # Last item: cherry

# modifying elements
fruits[1] = "blueberry" 
print(fruits)  # ['apple', 'blueberry', 'cherry']

# adding elements
fruits.append("orange")  # Add at the end 
fruits.insert(1, "mango")  # Insert at index 1 
print(fruits)  # ['apple', 'mango', 'blueberry', 'cherry', 'orange']

# removing elements
fruits.remove("mango")  # Remove by value 
last_fruit = fruits.pop()  # Remove last item 
del fruits[0]  # Remove by index

# looping through list
for fruit in fruits:
    print(fruit)

# Practice Task: Create a list of 5 cities. Print the third city. Add a new city to the list. Remove one city.
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
print(cities[2])  # Chicago
cities.append("Philadelphia")
print(cities) # ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia']
cities.remove("Houston")
print(cities) # ['New York', 'Los Angeles', 'Chicago', 'Phoenix', 'Philadelphia']



# Tuples: Ordered, Immutable Collections
# creating tuple
colors = ("red", "green", "blue") 
single_item = ("hello",)  # Must include a comma 

# accesing elements
print(colors[1])  # green 

# tuples are immutable
colors[1] = "yellow"  # ❌ This will cause an error 

# looping through tuple
for color in colors:
    print(color)

# Practice Task: Create a tuple of 3 favorite foods. Print the second food.
foods = ("pizza", "burger", "pasta")
print(foods[1])  # burger



# Dictionaries: Key-Value Pairs
# creating dictionary
person = {
  "name": "Alice",
  "age": 25,     
  "city": "New York" 
}

# accessing elements
print(person["name"])  # Alice 
print(person.get("age"))  # 25

# modifying elements
person["age"] = 26  # Update value 
person["job"] = "Engineer"  # Add new key-value pair

# removing elements
del person["city"]  # Remove by key

# looping through dictionary
for key, value in person.items():     
  print(key, ":", value) 

# Practice Task: Create a dictionary for a car with brand, model, and year. Add a color key. Print the model.
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}
car["color"] = "blue"
print(car["model"])  # Camry



# Sets: Unordered, Unique Collections
# creating set
numbers = {1, 2, 3, 4, 5} 
fruits = {"apple", "banana", "cherry"}

# adding and removing elements
fruits.add("orange") 
fruits.remove("banana")

# checking membership
print("apple" in fruits)  # True

# set operations
set1 = {1, 2, 3} 
set2 = {3, 4, 5}  
print(set1 | set2)  # Union: {1, 2, 3, 4, 5} 
print(set1 & set2)  # Intersection: {3} 
print(set1 - set2)  # Difference: {1, 2}

# Practice Task: Create a set of 5 animals. Add a new animal. Remove one animal.
animals = {"dog", "cat", "rabbit", "hamster", "parrot"}
animals.add("fish")
print(animals)  # {'dog', 'cat', 'rabbit', 'hamster', 'fish', 'parrot'}
animals.remove("rabbit")
print(animals)  # {'dog', 'cat', 'hamster', 'fish', 'parrot'}



# Final Practice Challenge: Create a program that:
# Asks the user to enter 3 favorite movies and stores them in a list.
# Converts the list into a tuple (to prevent modification).
# Stores the movies in a dictionary with keys "Movie 1", "Movie 2", etc.
# Converts the dictionary values into a set and prints them.
movies = []
for i in range(3):
    movie = input(f"Enter movie {i + 1}: ")
    movies.append(movie)
movies_tuple = tuple(movies)
print(movies_tuple)
movies_dict = {}
for i, movie in enumerate(movies_tuple):
    movies_dict[f"Movie {i + 1}"] = movie
movies_set = set(movies_dict.values())
print(movies_set)
