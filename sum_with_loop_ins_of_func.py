# Prompt the user to enter numbers separated by spaces
numbers = input("Enter the numbers you want separated by a space:\n").split()

# Initialize an empty list to store the converted numbers
numbers_list = []

# Convert each input number from string to integer and add to the list
for num in numbers:
    num = int(num)  # Convert the string to an integer
    numbers_list.append(num)  # Append the integer to the list

# Initialize total to zero for summation
print("Let's add each number to the next:")
total = 0

# Iterate through the list of numbers to calculate the running total
for num in numbers_list:
    total += num  # Add the current number to the total
    print(f"-> {total}")  # Print the current total after adding

# Print the final total
print(f"\nThe total number is: {total}.\n")
