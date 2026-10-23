import string

# Function to check if the shift value is valid


def check_key(shifts):
    if shifts < 1 or shifts > 25:
        print("Invalid key, please enter a shift value between 1 and 25.")
        exit()

# Function to encrypt the message using a Caesar cipher


def encrypt(message, shifts):
    encrypted_msg = ""
    for letter in message:
        # Check if the letter is in the alphabet
        if letter.lower() in letters:
            org_index = letters.index(letter.lower())  # Get the original index
            # Calculate the new index with the shift
            new_index = (org_index + shifts) % 26
            new_letter = letters[new_index]  # Get the new letter
            # Preserve the case of the original letter
            if letter.isupper():
                new_letter = new_letter.upper()
            encrypted_msg += new_letter  # Append the new letter to the encrypted message
        else:
            encrypted_msg += letter  # Preserve non-letter characters
    return encrypted_msg

# Function to decrypt the message using a Caesar cipher


def decrypt(message, shifts):
    decrypted_msg = ""
    for letter in message:
        # Check if the letter is in the alphabet
        if letter.lower() in letters:
            org_index = letters.index(letter.lower())  # Get the original index
            # Calculate the new index with the negative shift
            new_index = (org_index - shifts) % 26
            new_letter = letters[new_index]  # Get the new letter
            # Preserve the case of the original letter
            if letter.isupper():
                new_letter = new_letter.upper()
            decrypted_msg += new_letter  # Append the new letter to the decrypted message
        else:
            decrypted_msg += letter  # Preserve non-letter characters
    return decrypted_msg


# Define the lowercase letters for the cipher
letters = string.ascii_lowercase

# Prompt the user for the mode of operation
mode = input(
    "Do you want to encrypt or decrypt?\n[1] for encrypt.\n[2] for decrypt.\n")

# Handle encryption
if mode == "1":
    message = input("Enter your message: ")
    shifts = int(input("Enter the number of shifts: "))
    check_key(shifts)  # Validate the shift value
    msg = encrypt(message, shifts)  # Encrypt the message

# Handle decryption
elif mode == "2":
    message = input("Enter your message: ")
    shifts = int(input("Enter the number of shifts: "))
    check_key(shifts)  # Validate the shift value
    msg = decrypt(message, shifts)  # Decrypt the message

# Handle invalid option
else:
    print("Invalid option.")
    exit()

# Output the result
print(
    f"Here is your processed message: \"{msg}\"\nNo one can decrypt your message unless they have the keys, keep them safe.")
