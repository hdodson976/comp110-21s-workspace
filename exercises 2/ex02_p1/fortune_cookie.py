"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730142451"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    x: int = randint(1, 4)
    if x < 2:
        return "Swimming is easy. Staying afloat is hard."
    else: 
        if x == 2:
            return "A friend asks only for your time not your money."
        else:
            if x == 3:
                return "A fresh start will put you on your way."
            else: 
                return "Your ideals are well within your reach."

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
