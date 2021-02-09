"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730142451"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

a: int = randint(1, 4)
if a >= 2:
    if a >= 3:
        if a == 3:
            print("Swimming is easy. Staying afloat is hard.")
        else: 
            print("A fresh start will put you on your way.")
    else:
        print("A friend asks only for your time not your money.")
else: 
    print("Your ideals are well within your reach.")


print("Now, go spread positive vibes!")
