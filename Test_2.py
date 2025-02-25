import random
import string
import pyperclip

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

def generate_multiple_passwords(count, length, use_numbers=True, use_symbols=True, use_uppercase=True):
    passwords = [generate_password(length, use_numbers, use_symbols, use_uppercase) for _ in range(count)]
    return passwords

def save_passwords_to_file(passwords, filename):
    with open(filename, 'w') as file:
        for pwd in passwords:
            file.write(pwd + '\n')

def copy_to_clipboard(password):
    pyperclip.copy(password)
    print("Password copied to clipboard!")

# User input
count = int(input("Enter the number of passwords to generate: "))
length = int(input("Enter password length: "))
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

# Generate and display passwords
passwords = generate_multiple_passwords(count, length, use_numbers, use_symbols, use_uppercase)
print("\nGenerated Passwords:")
for pwd in passwords:
    print(pwd)

# Save passwords to a file
filename = input("Enter the filename to save passwords: ")
save_passwords_to_file(passwords, filename)
print(f"Passwords saved to {filename}")

# Copy the first generated password to clipboard
copy_to_clipboard(passwords[0])
