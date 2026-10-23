food = [['Apples', 'Bananas'], ['Milk', 'Water']]
print(food)

# Checking if the user wants to change the content of the basket
choice = input(
    "Type 'Yes' to change the the content of this basket ,or type 'No' if you don't want to.").lower()

# Applying the user command
print("Here is the updated content of this basket:")
if choice == '':
    # Remove 'Water' from the second list
    food[1].remove('Water')

    # Adding 'Tea' to the end of the second list
    food[1].append('Tea')

    # Adding 'Coffee' to the second list as the first item
    food[1].insert(0, 'Coffee')

    # Adding the list '[1,2,3]' to the end of the 'food' list
    food.append([1, 2, 3])

    # Insert 'Orange' at the beginning of the first list
    food[0].insert(0, 'Orange')

    # Insert 'Kiwis' at the end of the first list
    food[0].append('Kiwis')

    print(food)
else:
    print(food)
