"""An exercise in remainders and boolean logic."""

__author__ = "730142451"


# Begin your solution here...
prompt: str = input("Enter an int: ")

if (int(prompt) % 2) == 0:
    if (int(prompt) % 7) == 0:
            print("TAR HEELS")
    else:
         print("TAR")
else: 
    if (int(prompt) % 7) == 0:
        print("HEELS")
    else:
        print("CAROLINA")
