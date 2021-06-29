from gameplay import Gameplay_Loop
from board import Board
import math

MainLoop = Gameplay_Loop()

def game():
    Name = input("Welcome to naughts and crosses! What is your name?")
    numGames = int(input("Hi " + str(Name) + ", What would you like to play best of?"))
    winGames = math.ceil(((numGames + 1) / 2))
    print("Okay! First to " + str(winGames) + " game(s) win!")
    board = Board()
    board.start_board()
    print("The computer will go first :)")
    active = True
    while active:
        active = MainLoop.computer_choice(winGames)
        if active is True:
            active = MainLoop.player_choice(winGames, Name)


game()
