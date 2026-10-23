import random

# Generate a random 16-digit PIN
genpasswd = ''.join(str(random.randint(0, 9)) for _ in range(16))

# Prompt the user to enter their 16-digit PIN
userpasswd = input("Enter the 16-digit PIN:\n")

# Check if the entered PIN is 16 digits long
if len(userpasswd) != 16:
    print("Please enter a 16-digit PIN:\n")
else:
    # Compare the entered PIN with the generated PIN
    if userpasswd == genpasswd:
        print("PIN matched! Welcome.\n")
    else:
        print(
            f"PIN didn't match, please try again later.\nGenerated PIN was: {genpasswd}\n")
