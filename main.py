from board import Board
from gameplay import player_choice, computer_choice
import math


def game():
    numGames = int(input("Welcome to naughts and crosses! What would you like to play best of?"))
    winGames = math.ceil(((numGames + 1) / 2))
    print("Okay! First to " + str(winGames) + " game(s) win!")
    board = Board()
    board.start_board()
    print("The computer will go first :)")
    active = True
    while active:
        active = computer_choice(winGames)
        if active is True:
            active = player_choice(winGames)


game()
