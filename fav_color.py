# Initialize an empty list to store colors
colors = []

# Prompt the user to add the first color
color1 = input("Add the first color you like: \n")
colors.append(color1)

# Ask if the user wants to add more colors
more_colors = input("Do you want to add more colors? 'Yes' / 'No'\n")

# Check the user's response
if more_colors.lower() == "yes":
    # Loop to allow the user to add multiple colors
    while True:
        new_color = input(
            "Add another color to the list (or type 'done' to finish): \n")
        if new_color.lower() == 'done':
            break  # Exit the loop if the user is done
        colors.append(new_color)

elif more_colors.lower() == "no":
    print("No additional colors will be added.")

else:
    print("Please follow the instructions.\n")

# Display the list of colors the user likes
print(f"The colors you like are:\n{colors}")
