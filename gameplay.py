from board import Board
import random

from player import Player

GameplayBoard = Board()


class Gameplay_Loop:
    def __init__(self, winGames, Name, numGames):
        self.Name = Name
        self.numGames = numGames
        self.winGames = winGames
        self.computer = Player("computer", "computer")
        self.computer.token = "O"
        self.player1 = Player("real", Name)
        self.player1.token = "X"

    def computer_choice(self):
        random_entry = random.choice(GameplayBoard.mutableBoardList)
        self.update_board(random_entry, self.computer.token)
        return self.check_win_game(self.computer)

    def player_choice(self):
        player_position = int(input("Where would you like to go?"))
        if player_position in GameplayBoard.mutableBoardList:
            self.update_board(player_position, self.player1.token)
            return self.check_win_game(self.player1)
        else:
            print("That space is already full!")
            return self.player_choice()

    def check_win_game(self, Player):
        if self.win_condition(Player):
            if Player.token == "O":
                self.computer.count += 1
            else:
                self.player1.count += 1
            self.print_scores(self.player1)
            self.print_scores(self.computer)
            GameplayBoard.clear_board()
            if Player.count == self.winGames:
                print("=============")
                print("OVERALL CHAMPION = " + str(Player.name).upper())
                print("=============")
                return False
            elif ((self.numGames % 2) == 0) and (self.computer.count == self.player1.count == (winGames - 1)):
                    print("=============")
                    print("OVERALL SCORE = DRAW")
                    print("=============")
                    return False
            else:
                return True
        elif len(GameplayBoard.mutableBoardList) == 0:
            print("DRAW")
            return False
        else:
            return True

    @staticmethod
    def print_scores(Player):
        print(str(Player.name).upper() + "'S SCORE:" + str(Player.count))

    def update_board(self, position, player):
        GameplayBoard.mutableBoardDict[position] = player
        GameplayBoard.mutableBoardList.remove(position)
        GameplayBoard.print_board()

    def win_condition(self, player):
        token = player.token
        if GameplayBoard.check_for_filled_row(token, 1, 2, 3) or \
                GameplayBoard.check_for_filled_row(token, 4, 5, 6) or \
                GameplayBoard.check_for_filled_row(token, 7, 8, 9) or \
                GameplayBoard.check_for_filled_row(token, 1, 4, 7) or \
                GameplayBoard.check_for_filled_row(token, 2, 5, 8) or \
                GameplayBoard.check_for_filled_row(token, 3, 6, 9) or \
                GameplayBoard.check_for_filled_row(token, 1, 5, 9) or \
                GameplayBoard.check_for_filled_row(token, 3, 5, 7):
            print("WINNER OF ROUND = " + str(player.name).upper())
            return True
