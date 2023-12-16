import sys
from rps import rps
from guess_number import guess_number


def play_game(name="PlayerOne"):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")
        
        playerchoice = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissors\n2= Guess My Number\n\nOr press \"x\" to exit the Arcade\n\n"
        )
        
        if playerchoice not in ['1', '2', '3']:
            print(f"\n{name}, please enter 1, 2, or 3")
            
        else:
            decide_winner()
                

        
        
def decide_winner():
    if playerchoice == 1 and computerchoice == 2:
        print("Player wins")
    elif playerchoice == 2 and computerchoice == 3:
        print("Player wins")            













if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )
    
    parser.add_argument(
        '-n', '--name', metavar='name', required=True, help='The name of the person playing the game'
    )

    args = parser.parse_args()
    
    guess_my_number = guess_number(args.name)
    guess_my_number()
