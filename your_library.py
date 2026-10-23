# Initialize an empty list to store owned books
library = []

# Prompt the user to enter the name of a book they own
bookname = input("Enter the name of a book you own: ")
library.append(bookname)

# Prompt for another book, allowing the user to skip by pressing 'Enter'
bookname = input(
    "Enter the name of another book you own (or press 'Enter' to skip): ")
if bookname:
    library.append(bookname)

# Display the user's library
print(f"Your library: {library}")

# Initialize an empty list for the wishlist
wishlist = []

# Prompt the user to enter a book they wish to have
bookname = input("Enter the name of the book you wish you to have: ")
wishlist.append(bookname)

# Prompt for another book on the wishlist, allowing the user to skip
bookname = input(
    "Enter the name of any other book you wish you to have (or press 'Enter' to skip): ")
if bookname:
    wishlist.append(bookname)

# Display the user's wishlist
print(f"Your wishlist: {wishlist}")

# Initialize an empty list for acquired books
acquired = []

# Prompt the user to enter a book from their wishlist that they've acquired
bookname = input(
    "Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if bookname in wishlist:
    library.append(bookname)  # Add the acquired book to the library
    wishlist.remove(bookname)  # Remove the book from the wishlist

# Display the updated library and wishlist
print(f"Updated Library: {library}\nUpdated Wishlist: {wishlist}")

# Initialize an empty list for donated books
donated = []

# Prompt the user to enter a book from their library they wish to donate
bookname = input(
    "Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
if bookname in library:
    library.remove(bookname)  # Remove the donated book from the library

# Display the final library after donations
print(f"Final library after Donations: {library}")
