def makeBoard():
    board = {}
    for tick in range(8):
        board[tick] = []
        for tack in range(8):
            board[tick].append(0)
    return board

def viewBoard(inp):
    for key in inp:
        print(inp[key])

def defaultBoard(inp):
    for key in inp:
        if key == 1 or key == 6:
            for val in range(len(inp[key])):
                inp[key][val] = 1
        if key == 0 or key == 7:
            for val in range(len(inp[key])):
                if val == 0 or val == 7:
                    inp[key][val] = 4
                elif val == 1 or val == 6:
                    inp[key][val] = 2
                elif val == 2 or val == 5:
                    inp[key][val] = 3
                elif val == 3:
                    inp[key][val] = 6
                elif val == 4:
                    inp[key][val] = 5

def checkTurn(turnnum):
    if turnnum % 2 == 0: 
        return "Black"
    return "White"

pieces = {0:"Empty", 1:"Pawn", 2:"Knight",3:"Bishop",4:"Rook",5:"Queen",6:"King"}

board = makeBoard()
defaultBoard(board)
viewBoard(board)
print(pieces)

turn = 1
game = "In Play"
countw = 1
countb = 6
while game == "In Play":
    if checkTurn(turn) == "White":
        print(checkTurn(turn), "to move!")
        

        boardinp = False
        while boardinp == False:
            ycord = int(input("YCord [0,7]"))
            xcord = int(input("Xcord [0,7]"))
            if board[ycord][xcord] != 0:
                if board[ycord][xcord] == 1:
                    if board[ycord+1][xcord] == 0:
                        board[ycord+1][xcord] = 1
                        board[ycord][xcord] = 0
            boardinp = True
        
    else:
        print(checkTurn(turn), "to move!")


        boardinp = False
        while boardinp == False:
            ycord = int(input("YCord [0,7]"))
            xcord = int(input("Xcord [0,7]"))
            if board[ycord][xcord] != 0:
                if board[ycord][xcord] == 1:
                    if board[ycord-1][xcord] == 0:
                        board[ycord-1][xcord] = 1
                        board[ycord][xcord] = 0
            boardinp = True
    viewBoard(board)
    print(pieces)
    turn += 1