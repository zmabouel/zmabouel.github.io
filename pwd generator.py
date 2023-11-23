# This program will generate a password for you
# Your password may contain only letters, letters and numbers, letters and special
# characters, or letters numbers and special characters.

import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters  # All uppercase and lowercase alphabets
    digits = string.digits         # All digits from 0 to 9
    special = string.punctuation   # All special characters
    
    # Start with just letters
    characters = letters
    # Add digits if requested
    if numbers:
        characters += digits
    # Add special characters if requested
    if special_characters:
        characters += special
    
    pwd = ""  # Initialize password string
    meets_criteria = False
    has_number = False
    has_special = False
    
    # Loop until the password meets the specified criteria
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)  # Randomly pick a character
        pwd += new_char  # Add it to the password
        
        # Check if the new character is a number or special character
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        # Check if the password meets the criteria
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
            
    return pwd

# User input for password criteria
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n) ").lower() == "y"
has_special = input("Do you want to have special characters (y/n) ").lower() == "y"

# Generate password
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)

def test_password(pwd):
    global weak_pwds, strong_pwds
    # Initialize lists if they don't exist
    if 'weak_pwds' not in globals():
        weak_pwds = []
    if 'strong_pwds' not in globals():
        strong_pwds = []

    # Check for digits and special characters
    has_digit = any(char in string.digits for char in pwd)
    has_special = any(char in string.punctuation for char in pwd)

    if has_digit or has_special:
        strong_pwds.append(pwd)
        print("This password is a strong password. It has been added to a list of strong passwords, good choice.")
    else:
        weak_pwds.append(pwd)
        print("This password is a weak password. It has been added to a list of weak passwords, try using numbers or special characters.")
    

test_password(pwd)