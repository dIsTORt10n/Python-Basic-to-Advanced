# Prompt the user to enter the names of attendees, separated by commas
attendees = input(
    "Enter the names of attendees separated by commas: ").split(", ")

# Iterate through each person in the list of attendees
for person in attendees:
    # Ask if the current person is attending
    confirm = input(f"Is {person} attending? (y/n): ").lower()

    # Check the user's response
    if confirm == "n":
        print("\nAttendance not confirmed")
    elif confirm == "y":
        print("\nAttendance confirmed")
    else:
        # Handle invalid input
        print("Invalid choice, please restart the program again.")
        exit()  # Exit the program if the input is invalid

    # Print a separator for better readability
    print("----------------------")

# Wait for the user to press 'Enter' before exiting
input("Press 'Enter' to exit\n")
