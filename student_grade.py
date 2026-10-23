import os

# Clears the terminal screen based on the operating system


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Asks the user how many subjects they want to input


def get_num_of_subjects():
    while True:
        clear()
        prompt = input(
            "Enter the number of subjects (or press 'ENTER' to finish): ").strip()

        # Exit if the user provides no input
        if not prompt:
            return None

        # Ensure the input is a positive number
        if prompt.isdigit() and int(prompt) > 0:
            return int(prompt)
        else:
            print("\n[!] Error: Please enter a valid integer greater than 0.")
            input("Press 'Enter' to try again...")

# Collects marks for each subject and stores them in the grades list


def get_and_calc_marks(grades, subjects):
    remaining = subjects
    while remaining > 0:
        try:
            clear()
            # Dynamic prompt to show which subject number is being entered
            grade_input = int(
                input(f"Enter mark for subject {subjects - remaining + 1}: "))

            # Validate that marks are within the standard 0-100 range
            if 0 <= grade_input <= 100:
                grades.append(grade_input)
                remaining -= 1  # Decrement the counter to eventually exit the loop
            else:
                print("\n[!] Error: Marks must be between 0 and 100.")
                input("Press 'Enter' to continue.")

        except ValueError:
            print("\n[!] Error: Please enter a valid number.")
            input("Press 'Enter' to continue.")

# Coordinates the program flow and calculates the final average


def main():
    grades = []
    clear()
    name = input("Enter the student's name: ")

    # Get total subject count from the user
    subjects = get_num_of_subjects()

    # Stop the program if the user chose to exit
    if subjects is None:
        print("Operation cancelled.")
        return

    # Gather all grades
    get_and_calc_marks(grades, subjects)

    # Calculate and display the final result if grades were entered
    if grades:
        clear()
        average = sum(grades) / len(grades)
        status = "Passed!" if average >= 60 else "Failed!"

        print("--- RESULTS ---")
        print(f"Name:    {name}")
        print(f"Average: {average:.2f}")
        print(f"Status:  {status}")
    else:
        print("No grades recorded.")


# Entry point of the script
if __name__ == "__main__":
    main()
