from board import Board
# import random
import math
#
# foo = ['b']
# print(random.choice(foo))

# entry_list = list(a_dict.items())
# random_entry = random.choice(entry_list)

# player_count = 0
#
#
# def test():
#     global player_count
#     x = input("add or subtract?")
#     if x == "add":
#         player_count += 1
#         print(player_count)
#         test()
#     if x == "subtract":
#         player_count -= 1
#         print(player_count)
#         test()
#
#
# test()

# def checkWinGames(numGames):
#     winGames = ((numGames + 1)/2)
#
#
# checkWinGames(9)

# def determineWinner(winGames, player):
#     global player_count
#     global computer_count
#     if win_condition(player):
#         player_count += 1
#         print("COMPUTER SCORE:" + str(computer_count))
#         print("PLAYER SCORE:" + str(player_count))
#         if player_count == winGames:
#             print("=============")
#             print("OVERALL CHAMPION = " + str(player))
#             print("=============")
#             return False
#         elif len(Board.boardList) == 0:
#             return False
#         else:
#             return True
#     else:
#         return True

numGames = int(input("Welcome to naughts and crosses! What would you like to play best of?"))
winGames = ((numGames + 1) / 2)
print(math.ceil(winGames))
