"""Virtual MMA Fight, player fights a virutal opponents and whoever's health reaches 0 first loses."""

from random import randint

__author__ = "730142451"

# Global variables defined
player: str = input("What is your name? ")
points: int = 100


# main function, start with greet function.
def main() -> None: 
    """Main function to initiate the game."""
    greet()
    pathway_selection()


# Points tracks the players health throughout the fight, will change depending on
# choices and the random reponse back. 
opponent_points: int = 100
kick: int = randint(10, 20)
punch: int = randint(1, 20)
sad_face: str = "\U0001F622"
happy_face: str = "\U0001F642"
dizzy_face: str = "\U0001F635\U0001F4AB"


# greet function, printing welcome message and explaining game."
def greet() -> None: 
    """Welcome message and the game is explained."""
    print(f"{player}, welcome to the virtual MMA game.")
    print("In this game, you will engage in a MMA fight with a virutal opponent.")
    print(f"You and your opponent will begin the fight with {points} health points each.")
    print("Each round you will choose between kicking and punching.")
    print("Your attack will reduce your opponenets health.")
    print("Whoever's health points reaches 0 first loses.")
    

# 3 different pathways for the play to select from
def pathway_selection() -> None:
    """Player selects whether to surrender, have a practice round, or begin the fight."""
    pathway: str = input("Would you like to surrender, practice, or begin? ")
    if pathway == "surrender":
        print(f"Goodbye {player}.")
    else: 
        if pathway == "practice":
            practice()
        else: 
            fight()


def practice() -> None:
    """Play can perform a practice round and then returns to pathway selection."""
    practice_move: str = input("Would you like to punch or kick?")
    # The virutal opponents move will be randomly selected. 
    opponent_move: int = randint(1, 2)
    if opponent_move == 1: 
        global points
        points = points - punch
        print(f"{player}'s Health: {points}")
    else: 
        if opponent_move == 2: 
            points = points - kick
            print(f"{player}'s Health: {points}")
    if practice_move == "punch":
        global opponent_points
        opponent_points = opponent_points - punch
        print(f"Opponent's Health: {opponent_points}")
    else: 
        if practice_move == "kick":
            opponent_points = opponent_points - kick
            print(f"Opponent's Health: {opponent_points}")
        else: 
            print(f"Opponent's Health: {opponent_points}")
    pathway_selection()


# First round, then offer the player the option to surrender.
def fight() -> None:
    """First fight loop, continues until the players points reaches 50."""
    global points
    points = 100
    global opponent_points
    opponent_points = 100
    while points > 50 and opponent_points > 1: 
        opponent_move: int = randint(1, 2)
        move: str = input("Would you like to punch or kick? ")
        if opponent_move == 1: 
            points = points - punch
            print(f"{player}'s Health: {points}")
            if move == "punch":
                opponent_points = opponent_points - punch
                print(f"Opponent's Health: {opponent_points}")
            else: 
                if move == "kick":
                    opponent_points = opponent_points - kick
                    print(f"Opponent's Health: {opponent_points}")
                else: 
                    print(f"Opponent's Health: {opponent_points}")
        else: 
            points = points - kick
            print(f"{player}'s Health: {points}")
            if move == "punch":
                opponent_points = opponent_points - punch
                print(f"Opponent's Health: {opponent_points}")
            else: 
                if move == "kick":
                    opponent_points = opponent_points - kick
                    print(f"Opponent's Health: {opponent_points}")
                else: 
                    print(f"Opponent's Health: {opponent_points}")
        if opponent_points < 0:
            print(f"You win {happy_face}!")
            main()
    check_in(points)
    
        
def check_in(x: int) -> None: 
    """Function checks in with the player, and then may continue on to the second loop."""
    answer: str = input(f"Your health is getting low {dizzy_face}, do you want to surrender or continue? ")
    if answer == "surrender":
        print(f"Goodbye {player}")
    else: 
        if answer == "continue":
            global opponent_points
            while x > 1 and opponent_points > 1: 
                opponent_move: int = randint(1, 2)
                move: str = input("Would you like to punch or kick? ")
                if opponent_move == 1: 
                    x = x - punch
                    print(f"{player}'s Health: {x}.")
                    if move == "punch":
                        opponent_points = opponent_points - punch
                        print(f"Opponent's Health: {opponent_points}")
                    else: 
                        if move == "kick":
                            opponent_points = opponent_points - kick
                            print(f"Opponent's Health: {opponent_points}")
                        else: 
                            print(f"Opponent's Health: {opponent_points}")
                else: 
                    x = x - kick
                    print(f"{player}'s Health: {x}")
                    if move == "punch":
                        opponent_points = opponent_points - punch
                        print(f"Opponent's Health: {opponent_points}")
                    else: 
                        if move == "kick":
                            opponent_points = opponent_points - kick
                            print(f"Opponent's Health: {opponent_points}")
                        else: 
                            print(f"Opponent's Health: {opponent_points}")
        else:
            print(f"Goodbye {player}")
    if x < 1:
        print(f"You lose {sad_face}")
    else: 
        if opponent_points < 1:
            print(f"You win {happy_face}!")


# Call main function
if __name__ == "__main__":
    main()
