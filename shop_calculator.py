# Welcome message
print("------ Welcome to iShop Calculator -------\n")

# Prompt the user for the number of items in the basket
task_list = int(input("How many items are there in your basket today? "))
task_name = []
task_price = []

# Check if there are items in the basket
if task_list > 0:
    print("Let's get to counting them...")

    # Loop to collect item names and prices
    for i in range(task_list):
        name = input(f"Please type the name of item number {i + 1}:\n")
        task_name.append(name)
        # Changed to Euro symbol for clarity
        price = float(input(f"What is the price of '{name}'?\n€"))
        task_price.append(price)

    # Ask if the user wants to see the items in the basket
    choice = input(
        "Would you like to see your entire basket items? (y/n)\n").lower()
    if choice in ['y', 'yes']:
        print("Your basket items:", task_name)

        # Ask if the user wants to see the total cost
        choice = input(
            "Would you like to see how much it'll cost? (y/n)\n").lower()
        if choice in ['y', 'yes']:
            total_cost = sum(task_price)
            # Display total cost with two decimal places
            print(f"Buying these items will cost:\n€{total_cost:.2f}\n")

        else:
            input("Press 'Enter' to exit.")

    else:
        input("Press 'Enter' to exit.")

else:
    print("Seems like you are not in a shopping mood yet.")
