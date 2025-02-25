import random
import string

def generate_password(length, use_numbers=True, use_symbols=True, use_uppercase=True):
    characters = string.ascii_lowercase  # Start with lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
length = int(input("Enter password length: "))
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

# Generate and display password
password = generate_password(length, use_numbers, use_symbols, use_uppercase)
print("\nGenerated Password:", password)
