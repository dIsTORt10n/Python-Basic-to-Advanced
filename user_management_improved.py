import os  # Import the os module to interact with the operating system

# Global variables to store hashed passwords and user data
hashed_passwords = {}  # Dictionary to store hashed passwords with user IDs as keys
user_id_counter = 1  # Counter to assign unique IDs to users
users = {}  # Dictionary to store user objects with user IDs as keys


def clear_terminal():
    """Clears the terminal screen based on the operating system."""
    # Use 'cls' for Windows and 'clear' for Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')


class User:
    """Represents a user with personal information."""

    def __init__(self, first_name, last_name, email, password, user_id, status="inactive"):
        """Initializes a new User object with the provided details."""
        self.first_name = first_name  # User's first name
        self.last_name = last_name  # User's last name
        self.email = email  # User's email address
        self.password = password  # User's password (not stored in plain text)
        self.status = status  # User's status (active or inactive)
        self.user_id = user_id  # Unique identifier for the user

    def display_info(self):
        """Displays the user's information in a formatted manner."""
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        # Display hashed password
        print(f"Password: {hashed_passwords[self.user_id]}")
        print(f"User ID: {self.user_id}")
        print(f"Status: {self.status}")
        print("=" * 30)  # Separator for better readability


def hash_password(password):
    """Hashes the password by replacing each character with an asterisk."""
    return "*" * len(password)  # Create a string of asterisks equal to the length of the password


def create_user():
    """Prompts for user details and creates a new User object."""
    global user_id_counter  # Access the global user_id_counter variable
    while True:  # Loop until a valid user is created
        clear_terminal()  # Clear the terminal for a fresh input
        # Get user details
        first_name = input("Enter first name: ").strip(
        ).capitalize()  # Capitalize the first letter
        last_name = input("Enter last name: ").strip(
        ).capitalize()  # Capitalize the first letter
        email = input("Enter email: ").strip()  # Get email input
        password = input("Enter password: ").strip()  # Get password input

        # Check if the password is empty
        if not password:
            input("Error: Password cannot be empty. Please enter a valid password.")
            continue  # Restart the loop to get valid input

        # Prompt for user status with a default option
        status = input(
            "Enter status [active/inactive] (default = \"inactive\"): ").strip().lower()
        if status not in ["active", "inactive", ""]:  # Validate status input
            print("Error: Invalid input. Please type \"active\" or \"inactive\" (or press 'Enter' for default = \"inactive\").")
            input("Press 'Enter' to continue...")
            continue  # Restart the loop to get valid input

        status = status if status else "inactive"  # Set to default if empty

        user_id = user_id_counter  # Assign a unique ID to the new user
        user_id_counter += 1  # Increment the user ID counter for the next user

        # Hash the password and store it
        hashed_passwords[user_id] = hash_password(password)
        print("\nUser created successfully!")  # Confirmation message
        break  # Exit the loop after successful user creation

    # Return the new User object
    return User(first_name, last_name, email, password, user_id, status)


def display_all_users():
    """Displays all users in the system."""
    if users:  # Check if there are any users
        print("\n============== All Users ==============\n")
        for user in users.values():  # Iterate through all user objects
            user.display_info()  # Display each user's information
    else:
        # Message if no users exist
        print("\n============== No users found ==============\n")


def search_user_by_id(user_id):
    """Searches for a user by ID and displays their information."""
    user = users.get(user_id)  # Retrieve the user object by user ID
    if user:  # Check if the user exists
        print("User found:\n")
        user.display_info()  # Display the user's information
    else:
        print("Error: User not found.")  # Message if the user does not exist


def search_user_by_first_name(first_name):
    """Searches for users by first name and displays their information."""
    found = False  # Flag to track if any user is found
    for user in users.values():  # Iterate through all user objects
        if user.first_name.lower() == first_name.lower():  # Case-insensitive comparison
            user.display_info()  # Display the user's information
            found = True  # Set the flag to True if a user is found
    if not found:  # If no user was found
        # Message indicating no matches
        print("Error: No users found with that first name.")


def search_user_by_status(status):
    """Searches for users by status and displays their information."""
    found = False  # Flag to track if any user is found
    for user in users.values():  # Iterate through all user objects
        if user.status.lower() == status.lower():  # Case-insensitive comparison
            user.display_info()  # Display the user's information
            found = True  # Set the flag to True if a user is found
    if not found:  # If no user was found
        # Message indicating no matches
        print("Error: No users found with that status.")


def search_user_by_email(email):
    """Searches for users by email and displays their information."""
    found = False  # Flag to track if any user is found
    for user in users.values():  # Iterate through all user objects
        if user.email.lower() == email.lower():  # Case-insensitive comparison
            user.display_info()  # Display the user's information
            found = True  # Set the flag to True if a user is found
    if not found:  # If no user was found
        # Message indicating no matches
        print("Error: No users found with that email.")


def main():
    """Displays the main menu and handles user actions."""
    while True:  # Loop until the user decides to exit
        clear_terminal()  # Clear the terminal for a fresh display
        print("=========== Welcome To User Management ===========\n")
        try:
            # Prompt the user to choose an action
            action = int(input(
                "\nChoose an Action:\n1. Add new user\n2. Display all users\n3. Search for a user\n4. Exit the program\n"))
        except ValueError:  # Handle non-integer inputs
            # Prompt for valid input
            print("Error: Please enter a valid action number.")
            input("Press 'Enter' to continue...")
            continue  # Restart the loop to get valid input

        clear_terminal()  # Clear the terminal for the next action

        if action == 1:
            user = create_user()  # Create a new user
            # Store the user object in the users dictionary
            users[user.user_id] = user
            # Confirmation message
            input("\nUser added successfully! Press 'Enter' to continue...")

        elif action == 2:
            display_all_users()  # Display all users
            # Wait for user to acknowledge
            input("Press 'Enter' to continue...")

        elif action == 3:
            while True:  # Loop for searching users
                clear_terminal()  # Clear the terminal for fresh input
                try:
                    # Prompt the user to choose a search method
                    search_action = int(input(
                        "Search by:\n\n1. User ID\n2. First Name\n3. Status\n4. Email\n5. Go back\n6. Exit the program\n\nEnter the action number: "))
                    if search_action <= 0 or search_action > 6:  # Validate input
                        input("Error: Please enter a valid action number.")
                        continue  # Restart the loop to get valid input
                except ValueError:  # Handle non-integer inputs
                    input("Error: Please enter a valid number.")
                    continue  # Restart the loop to get valid input

                if search_action == 1:
                    try:
                        # Get user ID to search
                        user_id_to_search = int(input("Enter the user's ID: "))
                        # Search for user by ID
                        search_user_by_id(user_id_to_search)
                    except ValueError:  # Handle non-integer inputs
                        input("Error: Please enter a valid number.")
                    # Wait for user to acknowledge
                    input("Press 'Enter' to continue...")

                elif search_action == 2:
                    # Get first name to search
                    first_name_to_search = input(
                        "Enter the user's first name: ").strip()
                    # Search for user by first name
                    search_user_by_first_name(first_name_to_search)
                    # Wait for user to acknowledge
                    input("Press 'Enter' to continue...")

                elif search_action == 3:
                    status_to_search = input(
                        # Get status to search
                        "Enter the user's status (active/inactive): ").strip().lower()
                    # Validate status input
                    if status_to_search not in ["active", "inactive"]:
                        input(
                            "Error: Invalid status. Please enter either 'active' or 'inactive'.")
                        continue  # Restart the loop to get valid input
                    # Search for user by status
                    search_user_by_status(status_to_search)
                    # Wait for user to acknowledge
                    input("Press 'Enter' to continue...")

                elif search_action == 4:
                    # Get email to search
                    email_to_search = input("Enter the user's email: ").strip()
                    # Search for user by email
                    search_user_by_email(email_to_search)
                    # Wait for user to acknowledge
                    input("Press 'Enter' to continue...")

                elif search_action == 5:
                    break  # Go back to the main menu

                elif search_action == 6:
                    print("\nExiting the program...")  # Exit message
                    exit()  # Exit the program

        elif action == 4:
            print("\nExiting the program...")  # Exit message
            exit()  # Exit the program

        else:
            # Prompt for valid input
            input(
                "Error: Please enter a valid action number.\nPress 'Enter' to continue...")


if __name__ == "__main__":
    main()
