"""Some examples of list concepts."""

rolls: list[int] # Declare a variable who type is a list of ints

rolls = [2, 3, 2, 6] # Intialize w/ list literal syntax

print(f"Lenth of rolls is {len(rolls)}")

print(f"The last item in the list is {rolls[len(rolls)-1]}")
from random import randint
rolls.append(randint(1, 6)) # List's append method adds an item to the end of a list
print(rolls)

rolls.pop() # List's pop method, with no argument, removes the last item of the list
rolls.pop(0) # List's pop mehtod, with one argument, pops a specific index
print(rolls)

words: list[str] = list() # Construct an empty list using a list constructor
words.append("Hello")
print(words)