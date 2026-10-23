import random
import os


def clear():
    """
    Clears the terminal screen based on the operating system.
    'cls' is for Windows (nt), and 'clear' is for macOS/Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    # Initial setup: clear the screen and show a welcome message
    clear()
    input("Welcome to the dice rolling game! (Press Enter to start)")

    while True:
        clear()
        # Get user input and normalize it (remove whitespace and lowercase)
        choice = input("Roll the dice? (Y/n): ").strip().lower()

        # Exit condition: if the user types 'n'
        if choice == 'n':
            print("Quitting game...")
            exit()

        # Roll condition: accepts 'y', empty string (Enter), or a space
        elif choice == 'y' or choice == '' or choice == ' ':
            # Generate two random integers between -100 and 100
            num1 = random.randint(-100, 100)
            num2 = random.randint(-100, 100)

            # Display the result and wait for user to press Enter before clearing
            input(f"Result: ({num1}, {num2})")
            clear()

        # Error handling for invalid inputs
        else:
            input(
                f"Unexpected Error: '{choice}' is not an option. Press Enter to try again.")
            clear()
            continue


# Standard boilerplate to ensure the script runs only if executed directly
if __name__ == "__main__":
    main()
