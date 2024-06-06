import random

board=["-","-","-",
       "-","-","-",
       "-","-","-"]

currentPlayer="x"
winner=None
gamearunning=True

#planning the game board

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

#printBoard(board)

#take player input

def playerInput(board):
    inp=int(input("Enter a number 1-9:"))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1]=currentPlayer
    else:
        print("Oops player already in the spot!")


#check win or draw

def checkHorizontle(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[6]
        return True
    elif board[0]==board[5]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[3]==board[5]==board[6] and board[3]!="-":
        winner=board[3]
        return True
    elif board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True

def checkDraw(board):
    if "-"not in board:
        printBoard(board)
        print("It's Draw")
        gamearunning=False

def checkForWin():
    if checkHorizontle(board):
        print(f"The winner is {winner}")
    
#switch the olayer

def switchPlayer(board):
    global currentPlayer
    if currentPlayer=="x":
        currentPlayer="0"
    else:
        currentPlayer="x"

def computer(board):
    while currentPlayer=="0":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="0"
            switchPlayer(board)



#check for won or tie again

while gamearunning:
    printBoard(board)
    playerInput(board)
    checkForWin()
    checkDraw(board)
    switchPlayer(board)
    computer(board)
    checkForWin()
    checkDraw(board)
