import os

all_users = {}
new_id_num = len(all_users) + 1
hashed_passwords = {}


def clear_terminal():
    """Clears the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


class User:
    """Represents a user with personal information."""

    def __init__(self, first_name, last_name, email, password, user_id, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status
        self.user_id = user_id

    def display_info(self):
        """Displays the user's information."""
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {hashed_passwords[self.user_id]}")
        print(f"ID: {self.user_id}")
        print(f"Status: {self.status}")
        print("=" * 20)


def hash_password(password):
    """Hashes the password by replacing each character with an asterisk."""
    return "*" * len(password)


def create_user():
    """Prompts for user details and creates a new User object."""
    global new_id_num
    while True:
        clear_terminal()
        first_name = input("Enter first name: ").capitalize()
        last_name = input("Enter last name: ").capitalize()
        email = input("Enter email: ")
        password = input("Enter password: ")
        if not password:
            print("Sorry, due to security reasons you have to make a password.")
            input()
            continue
        # Prompt for user status with a default option
        status = input(
            "Enter status [active/inactive] (default = \"inactive\"): ")
        if not status or status == "inactive":  # If no status is provided, set to default
            status = "inactive"
        elif status == "active":
            status = "active"
        else:
            print(
                "Sorry, please type \"active\" or \"inactive\" (or press 'Enter' for default = \"inactive\").")
            input()
            continue
        
        user_id = new_id_num

        hashed_passwords[user_id] = hash_password(password)
        print("\nUser created successfully!")
        break

    return User(first_name, last_name, email, password, user_id, status)


def display_all_users(all_users):
    """Displays all users in the system."""
    if all_users:
        print("\n============== All Users ==============\n")
        for user in all_users.values():
            user.display_info()  # Display each user's information
    else:
        print("\n============== No users found ==============\n")


def search_user_id(searched_id):
    if searched_id in all_users.values():
        print("User found:\n")
        key = all_users[f"{searched_id}"].display_info()
        searched_id.display_info()
    else:
        print("User not found.")


def search_first_name(searched_first_name):
    pass


def search_status(searched_status):
    pass


def main():
    while True:
        clear_terminal()
        print("=========== Welcome To User Management ===========\n")
        try:
            action = int(input(
                "\nChoose an Action:\n1. Add new user\n2. Display all users\n3. Search for a user\n4. Exit the program\n"))
        except ValueError:
            input("Please enter a valid action number.")
            continue

        clear_terminal()

        if action == 1:
            clear_terminal()
            user = create_user()
            all_users[user.user_id] = user
            input("\nPress 'Enter' to continue...")
            clear_terminal()

        elif action == 2:
            clear_terminal()
            display_all_users(all_users)
            input("\nPress 'Enter' to continue...")
            clear_terminal()

        elif action == 3:
            while True:
                clear_terminal()
                try:
                    search_action = int(input(
                        "Search by:\n\n1. ID\n2. First Name\n3. Status\n4. Email\n5. Go back\n6. Exit the program\n\nEnter the action number: "))
                    if search_action <= 0:
                        input("Please enter a valid ID.")
                        continue
                except ValueError:
                    input("Please enter a valid number.")
                    continue

                if search_action == 1:
                    try:
                        id_to_search = int(input("Enter the user's ID: "))
                    except ValueError:
                        input("Please enter a valid number.")
                        continue
                    search_user_id(id_to_search)
                    input("\nPress 'Enter' to continue...")
                    clear_terminal()

                elif search_action == 2:
                    first_name_to_search = input("Enter the user's first name: ")
                    search_first_name(first_name_to_search)
                    input("\nPress 'Enter' to continue...")
                    clear_terminal()

                elif search_action == 3:
                    status_to_search = input(
                        "Enter the user's status (active/inactive): ")
                    if status_to_search != "active" or status_to_search != "inactive":
                        input("\nInvalid status, no such status.\n")
                        continue
                    search_status(status_to_search)
                    input("\nPress 'Enter' to continue...")
                    clear_terminal()

                elif search_action == 4:
                    email_to_search = input("Enter the user's first name: ")
                    search_first_name(first_name_to_search)
                    input("\nPress 'Enter' to continue...")
                    clear_terminal()

                else:
                    input(
                        "\nInvalid action, please choose a number from the available actions.\n")
                    continue

            input("\nPress 'Enter' to continue...")
            clear_terminal()

        elif action == 4:
            print("\nExiting the program...")
            exit()

        elif not action:
            input("\nPlease enter a valid action number.\n")

        else:
            input("\nPlease enter a valid action number.\n")

if __name__ == "__main__":
    main()