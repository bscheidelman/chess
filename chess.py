from colorama import Fore, Back, Style


class Pieces:
    def __init__(self, color, piece, ycord, xcord):
        self.color = color
        self.piece = piece
        self.ycord = ycord
        self.xcord = xcord

wp1 = Pieces("White", '1',6,0)
wp2 = Pieces("White", '1',6,1)
wp3 = Pieces("White", '1',6,2)
wp4 = Pieces("White", '1',6,3)
wp5 = Pieces("White", '1',6,4)
wp6 = Pieces("White", '1',6,5)
wp7 = Pieces("White", '1',6,6)
wp8 = Pieces("White", '1',6,7)
wr1 = Pieces("White", '4',7,0)
wr2 = Pieces("White", '4',7,7)
wk1 = Pieces("White", '2',7,1)
wk2 = Pieces("White", '2',7,6)
wb1 = Pieces("White", '3',7,2)
wb2 = Pieces("White", '3',7,5)
wq = Pieces("White", '5',7,3)
wk = Pieces("White", '6',7,4)
bp1 = Pieces("Black", '1',1,0)
bp2 = Pieces("Black", '1',1,1)
bp3 = Pieces("Black", '1',1,2)
bp4 = Pieces("Black", '1',1,3)
bp5 = Pieces("Black", '1',1,4)
bp6 = Pieces("Black", '1',1,5)
bp7 = Pieces("Black", '1',1,6)
bp8 = Pieces("Black", '1',1,7)
br1 = Pieces("Black", '4',0,0)
br2 = Pieces("Black", '4',0,7)
bk1 = Pieces("Black", '2',0,1)
bk2 = Pieces("Black", '2',0,6)
bb1 = Pieces("Black", '3',0,2)
bb2 = Pieces("Black", '3',0,5)
bq = Pieces("Black", '5',0,3)
bk = Pieces("Black", '6',0,4)

pli = [wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8, wr1, wr2, wk1, wk2, wb1,wb2, wq,wk,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8, br1, br2, bk1, bk2, bb1,bb2, bq,bk]

def viewBoard():
    temp = {}
    for tick in range(8):
        temp[tick] = []
        for tack in range(8):
            temp[tick].append('0')
    for obj in pli:
        temp[obj.ycord][obj.xcord] = obj.piece
    for key in temp:
        print(temp[key])
    print("")

def potentialMoves(x,y):
    objholder = None
    for obj in pli:
        if obj.ycord == y:
            if obj.xcord == x:
                objholder = obj
    if objholder == None:
        print(123213)
        return False
    temp = {}
    for tick in range(8):
        temp[tick] = []
        for tack in range(8):
            temp[tick].append('0')
    for obj in pli:
        temp[obj.ycord][obj.xcord] = obj.piece
    pairs = []
    if temp[objholder.ycord][objholder.xcord] == '1':
        init = 97
        pairs = []
        if objholder.color == "Black":
            if temp[objholder.ycord + 1][objholder.xcord] == '0':
                pairs.append([chr(init),objholder.ycord+1,objholder.xcord])
                init += 1
            if objholder.ycord == 1:
                if temp[objholder.ycord + 2][objholder.xcord] == '0':
                    pairs.append([chr(init),objholder.ycord+2,objholder.xcord])
                    init += 1
            if objholder.ycord != 0:
                for obj in pli:
                    if obj.ycord == objholder.ycord +1 and obj.xcord == objholder.xcord -1:
                        if obj.color == "White":
                            pairs.append([chr(init),objholder.ycord+1,objholder.xcord+-1])
                            init += 1
            if objholder.ycord != 7:
                for obj in pli:
                    if obj.ycord == objholder.ycord +1 and obj.xcord == objholder.xcord + 1:
                        if obj.color == "White":
                            pairs.append([chr(init),objholder.ycord+1,objholder.xcord+1])
                            init += 1
        else:
            if temp[objholder.ycord - 1][objholder.xcord] == '0':
                pairs.append([chr(init),objholder.ycord-1,objholder.xcord])
                init += 1
            if objholder.ycord == 1:
                if temp[objholder.ycord - 2][objholder.xcord] == '0':
                    pairs.append([chr(init),objholder.ycord-2,objholder.xcord])
                    init += 1
            if objholder.ycord != 0:
                for obj in pli:
                    if obj.ycord == objholder.ycord -1 and obj.xcord == objholder.xcord -1:
                        if obj.color == "Black":
                            pairs.append([chr(init),objholder.ycord-1,objholder.xcord+-1])
                            init += 1
            if objholder.ycord != 7:
                for obj in pli:
                    if obj.ycord == objholder.ycord -1 and obj.xcord == objholder.xcord + 1:
                        if obj.color == "Black":
                            pairs.append([chr(init),objholder.ycord-1,objholder.xcord+1])
                            init += 1

    if pairs == []:
        return False
    print(objholder.piece, objholder.color, objholder.ycord, objholder.xcord)
    for pair in pairs:
        temp[pair[1]][pair[2]] = pair[0]
    for key in temp:
        print(temp[key])
    checker = False
    while checker == False:
        inp = input("Choose your letter:")
        for pair in pairs:
            if str(pair[0]) == str(inp):
                checker = True
                if temp[pair[1]][pair[2]] == 0:
                    objholder.ycord = pair[1]
                    objholder.xcord = pair[2]
                else:
                    for obj in pli:
                        if obj.ycord == pair[1] and obj.xcord == pair[2]:
                            obj.ycord = None
                            obj.xcord = None
                            pli.remove(obj)
                    objholder.ycord = pair[1]
                    objholder.xcord = pair[2]
    return True
def startGame():
    turn = 1
    playing = True
    while playing == True:
        print(f'It is Turn {turn}')
        if turn % 2 == 1:
            player = "White"
        else:
            player = "Black"
        print(f'{player}s Turn!')
        print("The current board is:")
        viewBoard()
        tof = False
        while tof == False:
            yc = int(input("Choose your Y Cord [0,7]"))
            xc = int(input("Choose your X cord [0,7]"))
            tof = potentialMoves(xc,yc)
        turn +=1 

startGame()
