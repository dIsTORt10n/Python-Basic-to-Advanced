import random  # Import the random module to generate random numbers

# Prompt the user to guess a number between 1 and 10
guessed_num = int(input("Guess a number between 1 and 10: "))

# Generate a random number between 1 and 10 (inclusive)
actual_num = random.randint(1, 10)

# Loop until the user guesses the correct number
while guessed_num != actual_num:
    # Check if the guessed number is higher than the actual number
    if guessed_num > actual_num:
        guessed_num = int(input("Too high! Guess again: ")
                          )  # Prompt for a new guess
    # Check if the guessed number is lower than the actual number
    else:
        guessed_num = int(input("Too low! Guess again: ")
                          )  # Prompt for a new guess

# Inform the user that they have guessed the correct number
print("Congratulations! You guessed the number!")
