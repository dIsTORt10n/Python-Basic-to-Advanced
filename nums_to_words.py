num_map = {
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four ",
    "5": "Five ",
    "6": "Six ",
    "7": "Seven ",
    "8": "Eight ",
    "9": "Nine ",
    "0": "Zero ",
}
num = input("Enter a number: ")
nums = ""
for key in num:
    nums += num_map[key]
print(nums + ".")
