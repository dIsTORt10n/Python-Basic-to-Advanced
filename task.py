# Prompt the user to enter tasks for today, separated by commas
tasks = input("Enter your tasks for today separated by a comma: ").split(", ")

# Initialize lists to keep track of completed and not completed tasks
tasks_done = []
tasks_not_done = []

# Iterate through each task to check if it has been completed
for task in tasks:
    done = input(f"Did you finish '{task}' already? (y/n)\n").lower()

    if done == "y" or done == "yes":
        print("Nice Job!")
        tasks_done.append(task)  # Add the task to the done list

    elif done == "n" or done == "no":
        print("Try not to put it off.")
        tasks_not_done.append(task)  # Add the task to the not done list

    else:
        print("Invalid choice, please restart the program again and follow the instructions.\n")
        exit()  # Exit the program on invalid input

    print("-----------------------------")

# Ask the user if they want to see their progress
show_progress = input(
    "Do you want to see your today's progress? (y/n)\n").lower()

if show_progress == "yes" or show_progress == "y":
    # Display the completed and ongoing tasks
    print(
        f"\n********** Done Tasks **********\n{tasks_done}\n********** Ongoing Tasks **********\n{tasks_not_done}")

# Wait for the user to press 'Enter' before exiting
input("Press 'Enter' to exit.")
