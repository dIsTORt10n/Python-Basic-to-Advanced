def multiply():
    number = int(input("Enter a number: "))
    for num in range(1, 13):
        print(f"{number}x{num} = {number*num}")


multiply()
