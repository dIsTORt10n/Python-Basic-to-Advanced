# Welcoming the user
print("Welcome to the Rabbit Game!\n")

# Setting the game enviroment 🌿
field = [['🌿', '🌿', '🌿'], ['🌿', '🌿', '🌿'], ['🌿', '🌿', '🌿']]
print(f"{field[0]}\n{field[1]}\n{field[2]}")

# How to play the game && Taking the user's choice of the rows and columns
location = input(
    "Where should the rabbit go?🐇\nEnter the number of the row and the column you want to move the rabbit to.\n")

# Setting the rows and columns based on the user input
# The -1 is because the computer counts from 0 and humans count from 1, so when the user types row 1 column 2 the computer reads it row 2 column 3.
row = int(location[0])
column = int(location[1])-1

# Changing the items in the 'field' list
field[row][column] = '🐇'

# Printing the changes 🐇
print(f"{field[0]}\n{field[1]}\n{field[2]}")

print("Sucsess!")
