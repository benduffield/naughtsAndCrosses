from gameplay import Gameplay_Loop
from board import Board
import math


def game():
    Name = input("Welcome to naughts and crosses! What is your name?")
    numGames = int(input("Hi " + str(Name) + ", What would you like to play best of?"))
    winGames = math.ceil(((numGames + 1) / 2))
    print("Okay! First to " + str(winGames) + " game(s) win!")
    gameplay = Gameplay_Loop(winGames, Name, numGames)
    board = Board()
    board.start_board()
    gameplay.first_turn(Name)
    active = True
    while active:
        active = gameplay.computer_choice()
        if active is True:
            active = gameplay.player_choice()
    play_again = input("Would you like to play again? Yes [y] or no [n]")
    if play_again == "y":
        game()
    elif play_again == "n":
        print("Thanks for playing!")
        return
    else:
        "Please pick Yes [y] or no [n]"

game()
