class Board:
    boardDict = {1: " ", 2: " ", 3: " ",
                 4: " ", 5: " ", 6: " ",
                 7: " ", 8: " ", 9: " "}

    boardList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    mutableBoardDict = boardDict.copy()

    mutableBoardList = boardList.copy()

    def print_board(self):
        print("xxxxxxxxxxxx")
        print(self.mutableBoardDict[1] + "  | " + self.mutableBoardDict[2] + "  | " + self.mutableBoardDict[3])
        print("-  + -- +  -")
        print(self.mutableBoardDict[4] + "  | " + self.mutableBoardDict[5] + "  | " + self.mutableBoardDict[6])
        print("-  + -- +  -")
        print(self.mutableBoardDict[7] + "  | " + self.mutableBoardDict[8] + "  | " + self.mutableBoardDict[9])
        print("xxxxxxxxxxxx")

    @staticmethod
    def start_board():
        print("xxxxxxxxxxxx")
        print("1" + "  | " + "2" + "  | " + "3")
        print("-  + -- +  -")
        print("4" + "  | " + "5" + "  | " + "6")
        print("-  + -- +  -")
        print("7" + "  | " + "8" + "  | " + "9")
        print("xxxxxxxxxxxx")

    def check_for_filled_row(self, player, x, y, z):
        ret = False
        if self.mutableBoardDict[x] == player and self.mutableBoardDict[y] == player and self.mutableBoardDict[
            z] == player:
            ret = True
        return ret

    def clear_board(self):
        self.mutableBoardDict.clear()
        self.mutableBoardList.clear()
        self.mutableBoardDict = self.boardDict.copy()
        self.mutableBoardList = self.boardList.copy()
