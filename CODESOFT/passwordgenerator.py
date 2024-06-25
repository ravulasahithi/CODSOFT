import string
import random

def generate_password(length, complexity):
    characters = string.ascii_letters # Basic complexity with letters
    if complexity >= 2:
        characters += string.digits # Add digits for higher complexity
    if complexity >= 3:
        characters += string.punctuation # Add special characters for even higher complexity

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# User input for length and complexity
length = int(input("Enter the desired length of the password: "))
complexity = int(input("Enter the desired complexity (1-3): "))

# Generate and display the password
print(f"Your new password is: {generate_password(length, complexity)}")
