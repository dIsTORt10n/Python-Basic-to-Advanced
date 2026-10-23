# Prompt the user to enter the duration in seconds
time = int(input("Enter the duration in seconds:\n"))

# Calculate the number of hours
hours = time // (60 * 60)

# Calculate the number of minutes (remaining after hours)
minutes = (time % (60 * 60)) // 60

# Calculate the remaining seconds
seconds = time % 60

# Print the formatted duration
print(
    f"The duration is: {hours} hours, {minutes} minutes, and {seconds} seconds.\n")
