import re  # For regex checks
import random  # For generating random passwords
import string  # For character sets
import math  # For entropy calculations

# Password Generator Function
def gen_password(min_length, numbers=True, special_characters=True):
    # Define character sets
    letters = string.ascii_letters  # All uppercase and lowercase letters
    digits = string.digits  # Digits 0-9
    special = string.punctuation  # Special characters like !@#$%^&*

    # Start with letters as the base character set
    characters = letters
    if numbers:
        characters += digits  # Add digits to the character set if numbers are allowed
    if special_characters:
        characters += special  # Add special characters to the character set if allowed

    # Initialize the password with a random letter to ensure it starts with a letter
    pwd = random.choice(letters)
    meets_criteria = False  # Flag to check if the password meets all criteria
    has_number = False  # Flag to check if the password contains at least one number
    has_special = False  # Flag to check if the password contains at least one special character

    # Generate the password until it meets the criteria and has the required length
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)  # Randomly select a character from the character set
        pwd += new_char  # Append the character to the password

        # Check if the new character is a digit
        if new_char in digits:
            has_number = True
        # Check if the new character is a special character
        elif new_char in special:
            has_special = True

        # Update the meets_criteria flag based on the requirements
        meets_criteria = True
        if numbers:
            meets_criteria = has_number  # Ensure at least one number is present if required
        if special_characters:
            meets_criteria = meets_criteria and has_special  # Ensure at least one special character is present if required

    return pwd  # Return the generated password


# Defining a function to check password validity
def checker(password):
    feedback = []

    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long")
    if not re.search("[A-Z]", password):
        feedback.append("Password must contain at least one uppercase letter")
    if not re.search("[a-z]", password):
        feedback.append("Password must contain at least one lowercase letter")
    if not re.search("[0-9]", password):
        feedback.append("Password must contain at least one digit")
    if not re.search(r'[!@#$%^&*(),.?": =+\-/\\%[\]{}|<>]', password):
        feedback.append("Password must contain at least one special character")

    if not feedback:
        feedback.append("☑️All basic password rules passed!")

    return feedback


# Defining a function to calculate the entropy of the password
# The entropy is a measure of the unpredictability or randomness of the password.
def entropy(password):
    pool_size = 0
    if re.search("[A-Z]", password):
        pool_size += 26
    if re.search("[a-z]", password):
        pool_size += 26
    if re.search("[0-9]", password):
        pool_size += 10
    if re.search(r'[!@#$%^&*(),.?": =+\-/\\%[\]{}|<>]', password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return "Very Weak"

    bits = len(password) * math.log2(pool_size)  # Calculating the bits of entropy

    if bits < 40:
        strength = "Very Weak"
    elif bits < 60:
        strength = "Weak"
    elif bits < 80:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength  # Return just the strength (no entropy in the output)
