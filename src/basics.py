# VARIABLES
name = "Monica"
age = 35
print("Hello, my name is", name, "and I am", age, "years old.")

# LOOPS
for i in range(3):
    print("Loop number:", i)

# FUNCTIONS
def greet(person):
    return f"Hello {person}, welcome to Python!"

print(greet("Monica"))
print(greet("Mason"))
# QUIZ 1: Variables
apples = 4
bananas = 6
total_fruit = apples + bananas
print("Total fruit:", total_fruit)
# QUIZ 1: Variables
apples = 4
bananas = 6
total_fruit = apples + bananas
print("Total fruit:", total_fruit)
# QUIZ 2: Loops
animals = ["dog", "cat", "bird"]
for animal in animals:
    print("I love my", animal)
animals = ["dog", "cat", "bird", "turtle", "hamster"]
print(animal, "is my favorite!")
# QUIZ 3: Functions

# Define a function that multiplies two numbers
def multiply(a, b):
    return a * b

# Call the function with different values
print("3 x 4 =", multiply(3, 4))
print("7 x 8 =", multiply(7, 8))
# Call the function with different values
print("3 x 4 =", multiply(3, 4))
print("7 x 8 =", multiply(7, 8))
# MINI PROJECT: Multiplication Table Generator

def multiplication_table(number, up_to=10):
    print(f"\nMultiplication Table for {number}")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {multiply(number, i)}")

# Generate tables for 2, 3, and 5
multiplication_table(2)
multiplication_table(3)
multiplication_table(5)
