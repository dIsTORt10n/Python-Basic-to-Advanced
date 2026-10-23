# Prompt the user to enter the first and last names of friends, separated by commas
names = input(
    "Enter the first and last name of your friends separated by a comma:\n").split(", ")

# Initialize lists to store full names and abbreviated names
name_1st_2nd = []
abbreviated_names = []

# Iterate through each name provided by the user
for name in names:
    # Split the name into parts (first and last name)
    name_parts = name.split()
    name_1st_2nd.append(name_parts)  # Store the split name parts

    # Create an abbreviated name using the first letters of the first and last names
    abb_name = name_parts[0][0].upper() + "." + name_parts[1][0].upper()
    abbreviated_names.append(abb_name)  # Store the abbreviated name

    # Print the full name parts and the abbreviated name
    print(f"Full name parts: {name_parts}")
    print(f"Abbreviated name: {abb_name}")

# Optionally, print the list of abbreviated names
print("\nList of abbreviated names:", abbreviated_names)
