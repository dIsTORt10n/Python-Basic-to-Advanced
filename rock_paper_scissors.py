import random  # Import the random module to generate random choices for the computer

# ASCII art representations for Rock, Paper, and Scissors
rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_ascii = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Welcome message for the game
print("Welcome to the Rock, Paper, Scissors game:")
# Prompt user to continue or view help
confirm = input(
    "Enter to continue or type (Help) to print the help page. ").lower()

# Display game rules if the user requests help
if confirm == "help":
    print("""           ********** RULES **********
        1) You choose and the computer chooses
        2) Rock smashes Scissors -> Rock wins
        3) Scissors cut Paper -> Scissors win
        4) Paper covers Rock -> Paper wins
        """)

# List of valid choices
items = ["Rock", "Paper", "Scissors"]

# Get the player's choice and capitalize it for consistency
Player = input("Enter your choice (rock, paper, scissors): ").capitalize()

# Map player's choice to ASCII art
if Player == "Rock":
    Player = rock_ascii
    Player_name = "Rock"
elif Player == "Paper":
    Player = paper_ascii
    Player_name = "Paper"
elif Player == "Scissors":
    Player = scissors_ascii
    Player_name = "Scissors"
else:
    # Handle invalid input
    print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")
    exit()  # Exit the program if the input is invalid

print(f"You chose: {Player}")

# Generate a random choice for the computer
computer_choice = random.choice(items)
if computer_choice == "Rock":
    computer = rock_ascii
    computer_name = "Rock"
elif computer_choice == "Paper":
    computer = paper_ascii
    computer_name = "Paper"
elif computer_choice == "Scissors":
    computer = scissors_ascii
    computer_name = "Scissors"

print(f"Computer chose: {computer}")

# Determine the winner based on the player's and computer's choices
# Display the results of the game
if Player == computer:
    print("It's a tie!")
elif (
    (Player == "Rock" and computer == "Scissors")
    or
    (Player == "Paper" and computer == "Rock")
    or
    (Player == "Scissors" and computer == "Paper")
):
    print(f"You win! {Player_name} beats {computer_name}.")
else:
    print(f"You lose! {computer_name} beats {Player_name}")


# import random  # Import the random module to generate random choices for the computer

# # ASCII art representations for Rock, Paper, and Scissors
# rock_ascii = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """

# paper_ascii = """
#     _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# scissors_ascii = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """

# # List of choices and their corresponding ASCII art
# choices = ["Rock", "Paper", "Scissors"]
# ascii_art = [rock_ascii, paper_ascii, scissors_ascii]

# # Welcome message for the game
# print("Welcome to the Rock, Paper, Scissors game:")
# # Prompt user to continue or view help
# confirm = input("Enter to continue or type (Help) to print the help page. ").lower()

# # Display game rules if the user requests help
# if confirm == "help":
#     print("""           ********** RULES **********
#         1) You choose and the computer chooses
#         2) Rock smashes Scissors -> Rock wins
#         3) Scissors cut Paper -> Scissors win
#         4) Paper covers Rock -> Paper wins
#         """)

# # Get the player's choice and capitalize it for consistency
# player_choice = input("Enter your choice (rock, paper, scissors): ").capitalize()

# # Validate player's choice
# if player_choice not in choices:
#     print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")
#     exit()  # Exit the program if the input is invalid

# # Map player's choice to ASCII art
# if player_choice == "Rock":
#     player_art = rock_ascii
# elif player_choice == "Paper":
#     player_art = paper_ascii
# elif player_choice == "Scissors":
#     player_art = scissors_ascii

# # Generate a random choice for the computer
# computer_choice = random.choice(choices)

# # Map computer's choice to ASCII art
# if computer_choice == "Rock":
#     computer_art = rock_ascii
# elif computer_choice == "Paper":
#     computer_art = paper_ascii
# elif computer_choice == "Scissors":
#     computer_art = scissors_ascii

# # Determine the winner
# if player_choice == computer_choice:
#     winner = "Tie!"
# elif (player_choice == "Rock" and computer_choice == "Scissors") or \
#      (player_choice == "Scissors" and computer_choice == "Paper") or \
#      (player_choice == "Paper" and computer_choice == "Rock"):
#     winner = "Player wins!"
# else:
#     winner = "Computer wins!"

# # Display the results of the game
# print(f"You chose:\n{player_art}\nComputer chose:\n{computer_art}\n{winner}")


# import random  # Import the random module to generate random choices for the computer

# # ASCII art representations for Rock, Paper, and Scissors
# ascii_art = {
#     "Rock": """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """,
#     "Paper": """
#     _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """,
#     "Scissors": """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """
# }

# # Welcome message for the game
# print("Welcome to the Rock, Paper, Scissors game:")
# # Prompt user to continue or view help
# confirm = input("Enter to continue or type (Help) to print the help page. ").lower()

# # Display game rules if the user requests help
# if confirm == "help":
#     print("""           ********** RULES **********
#         1) You choose and the computer chooses
#         2) Rock smashes Scissors -> Rock wins
#         3) Scissors cut Paper -> Scissors win
#         4) Paper covers Rock -> Paper wins
#         """)

# # List of valid choices
# items = list(ascii_art.keys())

# # Get the player's choice and capitalize it for consistency
# player_choice = input("Enter your choice (rock, paper, scissors): ").capitalize()

# # Validate player's choice
# if player_choice not in ascii_art:
#     print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")
#     exit()  # Exit the program if the input is invalid

# # Generate a random choice for the computer
# computer_choice = random.choice(items)

# # Determine the winner
# winning_conditions = {
#     "Rock": "Scissors",
#     "Scissors": "Paper",
#     "Paper": "Rock"
# }

# if player_choice == computer_choice:
#     winner = "Tie!"
# else:
#     winner = "Player wins!" if winning_conditions[player_choice] == computer_choice else "Computer wins!"

# # Display the results of the game
# print(f"You chose:\n{ascii_art[player_choice]}\nComputer chose:\n{ascii_art[computer_choice]}\n{winner}")
