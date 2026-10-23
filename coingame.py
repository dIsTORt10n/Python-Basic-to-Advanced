import random

# Welcome message and method selection
print("Welcome to the Coin Guessing Game!\nChoose a method to toss the coin:\n1. Using random.random()\n2. Using random.randint()\n")

# User input for method choice
choice = input("Enter your choice (1 or 2): \n")

# Determine the computer's guess based on the chosen method
if choice == "1":
    # Using random.random() to simulate a coin toss
    toss_result = random.random()
    if toss_result >= 0.5:
        computerguess = "heads"
    else:
        computerguess = "tails"

elif choice == "2":
    # Using random.randint() to simulate a coin toss
    toss_result = random.randint(0, 1)
    if toss_result == 0:
        computerguess = "heads"
    else:
        computerguess = "tails"

else:
    print("Invalid choice, please select either (1) or (2)")
    exit()  # Exit the program if the choice is invalid

# User input for their guess
guess = input("Enter your guess (Heads) or (Tails):\n").lower()

# Determine the outcome of the game
if computerguess == guess:
    print("You Won!\n")
else:
    print("You lost!")

# Display the computer's guess
print(f"Computer guess was: {computerguess}.\n")
