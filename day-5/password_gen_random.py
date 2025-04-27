# Letters
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Symbols
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|', ';',
    ':', ',', '.', '<', '>', '/', '?'
]

nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbol = int(input("How many symbols would you like in your password?\n"))
nr_number = int(input("How many numbers would you like in your password?\n"))

password_chars = []
if nr_letter > 0:
    for _ in range(0,nr_letter):
        password_chars.append(random.choice(letters))

if nr_symbol > 0:
    for _ in range(0,nr_symbol):
        password_chars.append(random.choice(symbols))


if nr_number > 0:
    for _ in range(0,nr_number):
        password_chars.append(random.choice(numbers))

print(password_chars)
random.shuffle(password_chars)
print(password_chars)

generated_password = "";
for char in password_chars:
    generated_password+=char

print(f"Your password is {generated_password}")