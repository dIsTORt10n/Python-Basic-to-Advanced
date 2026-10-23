# Prompt the user to enter a sentence and split it into a list of words
sentence = input("Enter a sentence:\n").split()

# Join the words back into a single string (this line is not necessary for the output)
# original_sentence = " ".join(sentence)  # This line is commented out as it's not used

# Reverse the list of words and join them into a single string
reversed_sentence = " ".join(sentence[::-1])

# Print the reversed sentence
print(f'\nReversed sentence:\n{reversed_sentence}')
input("Press [ENTER] to exit.")
