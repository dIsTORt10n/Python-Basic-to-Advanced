# import os
# import time


# def clear():
#     os.system("cls" if os.name == "nt" else "clear")
    

# def main():
#     loading = True
#     while loading:
#         print("/")
#         time.sleep(0.4)
#         clear()
#         print("|")
#         time.sleep(0.4)
#         clear()
#         print("\\")
#         time.sleep(0.4)
#         clear()
        


# main()


# import time


# def loading():
#     a = ('Loading')
#     for i in range(4):
#         i = ('.')
#         time.sleep(1)
#         a = a + i
#         if(len(a) <= len('Loading...')):
#             print(a, end='\r')
#         else:
#             return loading()
# loading() 



# print("test\r.",end="\r")



# Source - https://stackoverflow.com/a/59886015
# Posted by PanicKk
# Retrieved 2026-03-06, License - CC BY-SA 4.0

# import time
# import os



# import time
# import os
# for i in range(101):
#     # The 'end="\r"' prevents a new line and moves the cursor back
#     print(f"Processing: {i}%", end='\r') 
#     time.sleep(0.05)
# def loading():
#     a = ('Loading')
#         else:
#             os.system('cls')
# loading() 

# print("\nTask finished.") # Print a newline at the end


import time

# Without flush=True, output may be delayed until the program finishes
# print("Loading...", end="", flush=False) # Default behavior

# With flush=True, output appears instantly
print("Loading...", end="\r", flush=True)
time.sleep(3)
for i in range(4):
    i = ('.')
    time.sleep(0.8)
    a = "Loading" + i
    if(len(a) <= len('Loading...')):
        print(a, end='\r')
print("done.")