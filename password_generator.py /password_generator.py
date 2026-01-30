import random

# Lists of characters
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '^', '(', ')', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

# Add random letters
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random numbers
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Add random symbols
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Shuffle password characters
random.shuffle(password_list)

# Convert list to string
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
