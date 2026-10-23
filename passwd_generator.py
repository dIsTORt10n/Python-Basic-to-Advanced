import random  # Import the random module for generating random choices
import string  # Import the string module for easy access to character sets

# Welcome message for the user
print("Welcome to the Password Generator!\n")

# Get user input for the total password length and the number of each character type
length = int(input("Enter the total number of characters in the password: "))
num_num = int(input("Enter the number of numbers in the password: "))
lett_num = int(input("Enter the number of letters in the password: "))
sym_num = int(input("Enter the number of symbols in the password: "))

# Calculate the total number of specified characters
sum_num_char = num_num + lett_num + sym_num

# Check if the sum of specified characters matches the total length
if sum_num_char != length:
    print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password length.\n")
    exit()  # Exit the program if the input is invalid

# Initialize a list to hold the password characters
password_chars = []

# Add the specified number of random digits to the password
password_chars += random.choices(string.digits, k=num_num)

# Add the specified number of random letters (both uppercase and lowercase) to the password
password_chars += random.choices(string.ascii_letters, k=lett_num)

# Add the specified number of random symbols to the password
password_chars += random.choices(string.punctuation, k=sym_num)

# Shuffle the list of password characters to ensure randomness
random.shuffle(password_chars)

# Join the list of characters into a single string to form the final password
final_password = ''.join(password_chars)

# Display the generated password to the user
print(f"Your generated password is: {final_password}")
input("Press [ENTER] to exit.")
