tictac = [ ["", "", ""],
           ["", "", ""],
           ["", "", ""] ]


def checkRow (myBoard, rowNum, gameover):
    if(gameover):
        return True
    if ((myBoard[rowNum][0] == myBoard[rowNum][1]) and (myBoard[rowNum][0] == myBoard[rowNum][2]) and myBoard[rowNum][0] != ""):
        print("{0} won!".format(myBoard[rowNum][0]))
        return True
    return False


def checkColumn (myBoard, colNum, gameover):
    if(gameover):
        return True
    if ((myBoard[0][colNum] == myBoard[1][colNum]) and (myBoard[0][colNum] == tictac[2][colNum]) and myBoard[0][colNum] != ""):
        print("{0} won!".format(myBoard[0][colNum]))
        return True
    return False


def checkDiagonals (myBoard, gameover):
    if(gameover):
        return True
    if ((myBoard[0][0] == myBoard[1][1]) and (myBoard[1][1] == myBoard[2][2]) and myBoard[0][0] != ""):
        print("{0} won!".format(myBoard[0][0]))
        return True
    if ((myBoard[0][2] == myBoard[1][1]) and (myBoard[1][1] == myBoard[2][0]) and myBoard[0][2] != ""):
        print("{0} won!".format(myBoard[0][2]))
        return True
    return False

def checkCat (myBoard, gameover):
    if(not gameover):
        catWin = True
    else:
        catWin = False
    for x in range(3):
        for y in range(3):
            if(myBoard[x][y] == "" and catWin == True):
                catWin = False
    if(catWin):
        print("The Cat Won :(")

def validate_winner (gameBoard):
    gameover = False
    for x in range(3):
        gameover = checkRow(gameBoard,x, gameover)
        gameover = checkColumn(gameBoard, x, gameover)
        gameover = checkDiagonals(gameBoard, gameover)
    checkCat(gameBoard, gameover)



