from gameplay import Gameplay_Loop
from board import Board
import math


def game():
    Name = input("Welcome to naughts and crosses! What is your name?")
    numGames = int(input("Hi " + str(Name) + ", What would you like to play best of?"))
    winGames = math.ceil(((numGames + 1) / 2))
    print("Okay! First to " + str(winGames) + " game(s) win!")
    board = Board()
    board.start_board()
    print("The computer will go first :)")
    active = True
    gameplay = Gameplay_Loop(winGames, Name, numGames)
    while active:
        active = gameplay.computer_choice()
        if active is True:
            active = gameplay.player_choice()


game()
