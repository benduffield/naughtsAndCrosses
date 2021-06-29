from board import Board
import random

GameplayBoard = Board()


class Gameplay_Loop:
    player_count = 0
    computer_count = 0

    def computer_choice(self, winGames):
        random_entry = random.choice(GameplayBoard.mutableBoardList)
        GameplayBoard.mutableBoardDict[random_entry] = "O"
        GameplayBoard.mutableBoardList.remove(random_entry)
        GameplayBoard.print_board()
        if self.win_condition("O"):
            self.computer_count += 1
            print("COMPUTER SCORE:" + str(self.computer_count))
            print("PLAYER SCORE:" + str(self.player_count))
            GameplayBoard.clear_board()
            if self.computer_count == winGames:
                print("=============")
                print("OVERALL CHAMPION = COMPUTER")
                print("=============")
                return False
            elif self.computer_count == self.player_count == (winGames - 1):
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

    def player_choice(self, winGames, Name):
        PlayerPosition = int(input("Where would you like to go?"))
        if PlayerPosition in GameplayBoard.mutableBoardList:
            GameplayBoard.mutableBoardDict[int(PlayerPosition)] = "X"
            GameplayBoard.mutableBoardList.remove(PlayerPosition)
            GameplayBoard.print_board()
            if self.win_condition("X"):
                self.player_count += 1
                print("COMPUTER SCORE:" + str(self.computer_count))
                print(str(Name).upper() + "'S SCORE:" + str(self.player_count))
                GameplayBoard.clear_board()
                if self.player_count == winGames:
                    print("=============")
                    print("OVERALL CHAMPION = " + str(Name).upper())
                    print("=============")
                    return False
                elif self.computer_count == self.player_count == (winGames - 1):
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
        else:
            print("That space is already full!")
            return self.player_choice(winGames, Name)

    def win_condition(self, player):
        if GameplayBoard.check_for_filled_row(player, 1, 2, 3) or \
                GameplayBoard.check_for_filled_row(player, 4, 5, 6) or \
                GameplayBoard.check_for_filled_row(player, 7, 8, 9) or \
                GameplayBoard.check_for_filled_row(player, 1, 4, 7) or \
                GameplayBoard.check_for_filled_row(player, 2, 5, 8) or \
                GameplayBoard.check_for_filled_row(player, 3, 6, 9) or \
                GameplayBoard.check_for_filled_row(player, 1, 5, 9) or \
                GameplayBoard.check_for_filled_row(player, 3, 5, 7):
            print("WINNER OF ROUND = " + str(player))
            return True
