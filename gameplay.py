from board import Board
import random

player_count = 0
computer_count = 0
boo = Board()


def computer_choice(winGames):
    random_entry = random.choice(boo.mutableBoardList)
    boo.mutableBoardDict[random_entry] = "O"
    boo.mutableBoardList.remove(random_entry)
    boo.print_board()
    global computer_count
    global player_count
    if win_condition("O"):
        computer_count += 1
        print("COMPUTER SCORE:" + str(computer_count))
        print("PLAYER SCORE:" + str(player_count))
        boo.clear_board()
        if computer_count == winGames:
            print("=============")
            print("OVERALL CHAMPION = COMPUTER")
            print("=============")
            return False
        elif computer_count == player_count == (winGames - 1):
            print("=============")
            print("OVERALL SCORE = DRAW")
            print("=============")
            return False
        else:
            return True
    elif len(boo.mutableBoardList) == 0:
        print("DRAW")
        return False
    else:
        return True


def player_choice(winGames):
    PlayerPosition = int(input("Where would you like to go?"))
    if PlayerPosition in boo.mutableBoardList:
        boo.mutableBoardDict[int(PlayerPosition)] = "X"
        boo.mutableBoardList.remove(PlayerPosition)
        boo.print_board()
        global player_count
        global computer_count
        if win_condition("X"):
            player_count += 1
            print("COMPUTER SCORE:" + str(computer_count))
            print("PLAYER SCORE:" + str(player_count))
            boo.clear_board()
            if player_count == winGames:
                print("=============")
                print("OVERALL CHAMPION = PLAYER")
                print("=============")
                return False
            elif computer_count == player_count == (winGames - 1):
                print("=============")
                print("OVERALL SCORE = DRAW")
                print("=============")
                return False
            else:
                return True
        elif len(boo.mutableBoardList) == 0:
            print("DRAW")
            return False
        else:
            return True
    else:
        return player_choice(winGames)


def win_condition(player):
    if boo.check_for_filled_row(player, 1, 2, 3) or \
            boo.check_for_filled_row(player, 4, 5, 6) or \
            boo.check_for_filled_row(player, 7, 8, 9) or \
            boo.check_for_filled_row(player, 1, 4, 7) or \
            boo.check_for_filled_row(player, 2, 5, 8) or \
            boo.check_for_filled_row(player, 3, 6, 9) or \
            boo.check_for_filled_row(player, 1, 5, 9) or \
            boo.check_for_filled_row(player, 3, 5, 7):
        print("WINNER OF ROUND = " + str(player))
        return True
