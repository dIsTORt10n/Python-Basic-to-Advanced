import os

# Dictionary to store tasks
tasks = {}


class Task():
    def __init__(self, task_id, title, description, duedate, priority='normal', note='', status='incomplete'):
        # Initialize task attributes
        self.task_id = task_id
        self.title = title
        self.description = description
        self.duedate = duedate
        self.priority = priority
        self.note = note
        self.status = status

    def display_task(self):
        # Display task details in a formatted manner
        print(f"""
================================
Task ID: {self.task_id}
Task Title: {self.title}
Description: {self.description}
Due Date: {self.duedate}
Priority: {self.priority}
Note: {self.note}
Status: {self.status}
================================
\n""")


def clear_terminal():
    # Clear the terminal screen for better readability
    os.system('cls' if os.name == 'nt' else 'clear')


def add_task():
    global tasks
    # Generate a unique ID for the new task
    task_id = len(tasks) + 1
    while True:
        clear_terminal()
        # Normalize title to lowercase
        title = input("Enter a title for the task: ").strip().lower()

        if not title:
            input("\nERROR: Please enter a title.")
            continue

        # Gather additional task details
        description = input(
            "Enter a description for the task (Press 'Enter' to skip): ").strip()
        duedate = input(
            "Enter the due-date of the task (Press 'Enter' to skip): ").strip()
        priority = input(
            "Enter the priority of the task, or press 'Enter' for the default 'normal': ").strip().lower()

        if not priority:
            priority = "normal"

        note = input(
            "Would you like to add any more notes (Press 'Enter' to skip): ").strip()
        status = 'incomplete'

        # Create a new Task object and store it in the tasks dictionary
        task = Task(task_id, title, description,
                    duedate, priority, note, status)
        tasks[title] = task  # Use the title as the key
        input(f"\n{"=" * 5} Task created successfully {"=" * 5}\n")
        break


def task_exists(title):
    # Check if a task with the given title exists
    return title in tasks


def remove_task():
    global tasks
    if not tasks:
        print(f"\n{"=" * 5} There are no tasks yet {"=" * 5}\n")
        input("\nPress 'Enter' to go back to the main menu.")
    else:
        while True:
            clear_terminal()
            task2remove = input(
                "Enter the title of the task you want to remove: ").strip().lower()
            if task_exists(task2remove):
                # Remove the task from the dictionary
                tasks.pop(task2remove)
                input(f"\n{"=" * 5} Task removed successfully {"=" * 5}\n")
                break
            else:
                choice = input(
                    "\nERROR: There is no task with that title, try again? (Y/n)").strip().lower()
                if choice in ['y', '', 'yes']:
                    continue
                else:
                    break


def mark_task_complete():
    global tasks
    if not tasks:
        print(f"\n{"=" * 5} There are no tasks yet {"=" * 5}\n")
        input("\nPress 'Enter' to go back to the main menu.")
    else:
        while True:
            clear_terminal()
            completed_task = input(
                "Enter the title of the task that you have completed: ").strip().lower()
            if task_exists(completed_task):
                # Mark the task as completed
                tasks[completed_task].status = 'completed'
                input(f"\n{"=" * 5} Task completed successfully {"=" * 5}\n")
                break
            else:
                choice = input(
                    "\nERROR: There is no task with that title, try again? (Y/n)").strip().lower()
                if choice in ['y', '', 'yes']:
                    continue
                else:
                    break


def view_tasks():
    # Display all tasks in the tasks dictionary
    if not tasks:
        print(f"\n{"=" * 5} No tasks found {"=" * 5}\n")
    else:
        for task in tasks.values():
            task.display_task()

    input("\nPress 'Enter' to go back to the main menu.")


def main():
    global tasks
    while True:
        clear_terminal()
        print(f"{"=" * 10} To-Do-List {"=" * 10}\n")
        print(
            "Options: \n[1]. Add Task \n[2]. Remove Task \n[3]. Mark Complete \n[4]. View Tasks \n[5]. Exit\n")

        try:
            choice = int(input("Choose an option: "))

            # Validate the choice input
            if len(str(choice)) != 1:
                input(
                    "\nERROR: Invalid option, please enter a single digit number from the options.\n")
                continue

            elif choice <= 0 or choice > 5:
                input(
                    "\nERROR: Invalid option, please enter a valid option number from the shown options.\n")
                continue

        except ValueError:
            input(
                "\nERROR: Invalid option, please enter a valid option number from the shown options.\n")
            continue

        clear_terminal()

        # Execute the chosen option
        if choice == 1:
            add_task()  # Add a new task

        elif choice == 2:
            remove_task()  # Remove an existing task

        elif choice == 3:
            mark_task_complete()  # Mark a task as complete

        elif choice == 4:
            view_tasks()  # View all tasks

        elif choice == 5:
            # Confirm exit
            confirm_exit = input(
                "Are you sure you want to exit? (Y/n): ").strip().lower()
            if confirm_exit in ['y', '', 'yes']:
                exit()  # Exit the application

        else:
            input(
                "\nERROR: Invalid option, please enter a valid option number from the shown options.\n")
            continue


if __name__ == "__main__":
    main()
