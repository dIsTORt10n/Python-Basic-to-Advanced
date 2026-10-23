import string  # Import the string module to access punctuation characters

# Prompt the user to input a sentence
sentence = input("Please type a sentence:\n")

# Initialize an empty string to store the new sentence without punctuation
newsentence = ""

# Iterate through each character in the input sentence
for letter in sentence:
    # Check if the character is not a punctuation mark
    if letter not in string.punctuation:
        # If it's not punctuation, add it to the new sentence
        newsentence += letter

# Print the result, showing the sentence without punctuation
print(
    f"\n*** Here is the same sentence without punctuation ***\n\n{newsentence}")
