tictac = [["x", "o", "o"],
          ["x", "o", "x"],
          ["o", "x", "o"]]

def checkRow (gameBoard, rowNum, gameover):
    if(gameover):
        return True
    if ((gameBoard[rowNum][0] == gameBoard[rowNum][1]) and (gameBoard[rowNum][0] == gameBoard[rowNum][2])
            and gameBoard[rowNum][0] != ""):
        return True
    return False

def checkColumn (gameBoard, colNum, gameover):
    if(gameover):
        return True
    if ((gameBoard[0][colNum] == gameBoard[1][colNum]) and (gameBoard[0][colNum] == tictac[2][colNum])
            and gameBoard[0][colNum] != ""):
        return True
    return False

def checkDiagonals (gameBoard, gameover):
    if(gameover):
        return True
    if ((gameBoard[0][0] == gameBoard[1][1]) and (gameBoard[1][1] == gameBoard[2][2]) and gameBoard[0][0] != ""):
        return True
    if ((gameBoard[0][2] == gameBoard[1][1]) and (gameBoard[1][1] == gameBoard[2][0]) and gameBoard[0][2] != ""):
        return True
    return False

def validate_winner (gameBoard):
    gameover = False
    for x in range(3):
        gameover = checkRow(gameBoard,x, gameover)
        gameover = checkColumn(gameBoard, x, gameover)
        gameover = checkDiagonals(gameBoard, gameover)
    return gameover

print(validate_winner(tictac))


