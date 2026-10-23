import random

# Welcome message
print("Welcome to 'Whose Wallet?'\nYou will give me a list of names, and I will pick a person to pay.")

# Prompt the user to enter names separated by commas
name = input(
    "If you're ready, enter the names separated by a comma:\n").split(", ")

# Randomly select a name from the list
selected_name = random.choice(name)

# Print the selected name
print(
    f"Please ask '{selected_name}' to take his wallet out. Dinner is on him.")
