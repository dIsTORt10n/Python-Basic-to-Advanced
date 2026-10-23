# Welcome message
print("------ Welcome to the Multiplication Table ------")

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Print the header for the multiplication table
print(f"\nMultiplication table for {number}:\n")

# Loop through numbers 1 to 12 to generate the multiplication table
for x in range(1, 13):
    product = number * x  # Calculate the product
    print(f"{number} x {x} = {product}")  # Print the multiplication result

input("Press [ENTER] to exit.")
