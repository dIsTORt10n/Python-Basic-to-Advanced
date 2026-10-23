# Initialize an empty list to store numbers
numbers_list = []

# Prompt the user to enter numbers separated by commas
numbers = input("Enter the numbers separated by a comma (,) :\n")

# Split the input string into a list of numbers (as strings)
numbers_list = numbers.split(", ")

# Iterate through each number in the list
for x in numbers_list:
    # Convert the string to an integer for processing
    x = int(x)

    # Check if the number is even
    if x % 2 == 0:
        print(f"\n{x}")  # Print the even number

# Indicate that the loop has finished successfully
print("\nFinished the loop successfully!")
