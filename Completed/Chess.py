ans = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease change your window settings to:\nFont:  Bodoni MT Condensed\nSize:  22\n"
            "(Options  -  Configure IDLE)\n\nPress enter when you are done")

#default font is Courier New at font size 10

def main():
    global turn
    global board                         #turn board clockwise to get what real board looks like
    
    board = [[{"name":"castle", "team":1, "moved":False},    {"name":"pawn", "team":1, "moved":False, "enpassant":False},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"pawn", "team":2, "moved":False, "enpassant":False},    {"name":"castle", "team":2, "moved":False}],
             [{"name":"knight", "team":1, "moved":False},    {"name":"pawn", "team":1, "moved":False, "enpassant":False},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"pawn", "team":2, "moved":False, "enpassant":False},    {"name":"knight", "team":2, "moved":False}],
             [{"name":"bishop", "team":1, "moved":False},    {"name":"pawn", "team":1, "moved":False, "enpassant":False},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"pawn", "team":2, "moved":False, "enpassant":False},    {"name":"bishop", "team":2, "moved":False}],
             [{"name":"queen" , "team":1, "moved":False},    {"name":"pawn", "team":1, "moved":False, "enpassant":False},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"pawn", "team":2, "moved":False, "enpassant":False},    {"name":"queen" , "team":2, "moved":False}],
             [{"name":"king"  , "team":1, "moved":False},    {"name":"pawn", "team":1, "moved":False, "enpassant":False},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"pawn", "team":2, "moved":False, "enpassant":False},    {"name":"king"  , "team":2, "moved":False}],
             [{"name":"bishop", "team":1, "moved":False},    {"name":"pawn", "team":1, "moved":False, "enpassant":False},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"pawn", "team":2, "moved":False, "enpassant":False},    {"name":"bishop", "team":2, "moved":False}],
             [{"name":"knight", "team":1, "moved":False},    {"name":"pawn", "team":1, "moved":False, "enpassant":False},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"pawn", "team":2, "moved":False, "enpassant":False},    {"name":"knight", "team":2, "moved":False}], 
             [{"name":"castle", "team":1, "moved":False},    {"name":"pawn", "team":1, "moved":False, "enpassant":False},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"empty", "team":0},    {"name":"pawn", "team":2, "moved":False, "enpassant":False},    {"name":"castle", "team":2, "moved":False}],
            ]

    symbols = [{"empty":"     "}, {"castle":"♜", "knight":"♞", "bishop":"♝", "queen":"♛", "king":"♚", "pawn":"♟"}, {"castle":"♖", "knight":"♘", "bishop":"♗", "queen":"♕", "king":"♔", "pawn":"♙"}]
    turns = [None, "black", "white"] #what colour is what turn number

    turn = 2
    quitGame = False

    while not quitGame:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nturn: {}\n\n      0     1      2     3     4      5     6     7".format(turns[turn]))

        #print board
        for y in range(8):
            row = str(y) + "  "
            for column in board:
                row += "[{}]".format(symbols[column[y]["team"]][column[y]["name"]])
            print(row)

        #excecute action
        action = input("\n\n\n\n\n\n\n\n>>>").lower().split(" ")
        if action[0] == "move" and action[3] == "to":
            action.append("queen")
            try:
                if move(int(action[1]), int(action[2]), int(action[4]), int(action[5]), action[6]):
                    turn = (None, 2, 1)[turn]
                else:
                    print("        Not a legal move")
                    ans = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nILLEGAL MOVE")
            except:
                ans = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWRONG ACTION SYNTAX")
        elif action[0] == "debug":      #Debugging command
            if action[1] == "pieceinfo":
                print(board[int(action[2])][int(action[3])])
            elif action[1] == "boardinfo":
                print(board)
            elif action[1] == "skip":
                turn = (None, 2, 1)[turn]
            else:
                ans = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWRONG ACTION SYNTAX")
        else:
            ans = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWRONG ACTION SYNTAX")

                            

def move(locationX, locationY, destinationX, destinationY, promotion):
    print("Moving piece...")
    global turn
    global board

    prevBoard = board
    
    legalMove = checkLegalMove(locationX, locationY, destinationX, destinationY, False)
    
    if legalMove: #check if move is actually legal
        print("    Passed legal move check")
        if legalMove == True: #ordinary move
            print("    Ordinary move")
            board[destinationX][destinationY] = board[locationX][locationY]
            board[locationX][locationY] = {"name":"empty", "team":0}
            if board[destinationX][destinationY]["name"] == "pawn":
                board[destinationX][destinationY]["enpassant"] = False
            print("    Moved piece")
                
        elif legalMove == "double": #double pawn movement
            print("    Double pawn jump move")
            board[destinationX][destinationY] = board[locationX][locationY]
            board[locationX][locationY] = {"name":"empty", "team":0}
            board[destinationX][destinationY]["enpassant"] = True
            print("    Moved piece")

        elif legalMove == "promote": #pawn promotion
            print("    Pawn promotion move")
            if promotion == "castle" or promotion == "knight" or promotion == "bishop" or promotion == "queen":
                board[destinationX][destinationY] = {"name":promotion, "team":turn, "moved":True}
                board[locationX][locationY] = {"name":"empty", "team":0}
                print("    Moved piece")
            else:
                print("    Invalid promotion")
                return False

        elif legalMove == "castle right":
            print("    Castle move to the right")
            board[destinationX][destinationY] = board[locationX][locationY]
            board[locationX][locationY] = {"name":"empty", "team":0}
            board[locationX][5] = board[locationX][7]
            board[locationX][7] = {"name":"empty", "team":0}
            print("    Moved piece")

        elif legalMove == "castle left":
            print("    Castle move to the left")
            board[destinationX][destinationY] = board[locationX][locationY]
            board[locationX][locationY] = {"name":"empty", "team":0}
            board[locationX][3] = board[locationX][0]
            board[locationX][0] = {"name":"empty", "team":0}
            print("    Moved piece")

        elif legalMove == "enpassant": #special move case called 'en passant'
            print("    Special 'En passant' move")
            board[destinationX][destinationY] = board[locationX][locationY]
            board[locationX][locationY] = {"name":"empty", "team":0}
            board[destinationX][destinationY + 1] = {"name":"empty", "team":0}
            print("    Moved piece")
        else:
            print("    Error 01")

        board[destinationX][destinationY]["moved"] = True

        if not checkNoPotentialCheck():
            print("    Player is trying to move to a position of check")
            board = prevBoard
            return False

        print("    Player is not trying to move to a position of check")
        return True

    else:
        return False
            

def checkNoPotentialCheck():
    print("Checking if king is in check...")
    
    global turn
    global board
    
    #find king
    x = 0
    for column in board:
        y = 0
        for piece in column:
            if piece["name"] == "king" and piece["team"] == turn:
                kingX = x
                kingY = y
                break
                break
                
            y += 1

        x += 1
    print("    Found king")

    #check if the king can be killed by another piece
    x = 0
    for column in board:
        y = 0
        for piece in column:
            if piece["name"] != "empty" and piece["team"] != turn:
                if checkLegalMove(x, y, kingX, kingY, True):
                    return False

            y += 1
                
        x += 1

    return True


def checkLegalMove(locationX, locationY, destinationX, destinationY, ignoreTurn): #Y increases as you go downwards
    print("    Checking if move is legal...")
    
    global turn
    global board
    
    piece = board[locationX][locationY]
    print("        Piece to move is {}".format(piece))
    destPiece = board[destinationX][destinationY]
    print("        Destination piece is {}".format(destPiece))
    up = (turn * 2) - 3                                        #If it is black's turn (1) then X 2 = 2 and -3 = -1
                                                               #So up (forward) is downwards
    print("        Up direction is {}".format(up))

    if (piece["team"] == turn and destPiece["team"] != turn) or ignoreTurn:
        print("        Player is moving their own piece")
        if destinationX >= 0 and destinationX < 8 and destinationY >= 0 and destinationY < 8:
            print("        Destination is inside the playing board")
            if locationX != destinationX or locationY != destinationY:
                print("        Player is actually moving their piece to a NEW location")
                if piece["name"] == "pawn":
                    print("        Detected piece - pawn")
                    if destinationY != 0 and destinationY != 7:
                        print("        Not a pawn promotion")
                        if locationY - destinationY == up:
                            print("        Pawn is moving in the correct direction and is not doing a double move")
                            if locationX == destinationX:
                                print("        Pawn doing single step foward (not diagonal)")
                                if destPiece["team"] == 0:
                                    print("        Moving to empty tile")
                                    return True
                            elif locationX - destinationX == 1 or locationX - destinationX == -1:
                                print("        Pawn doing single step to the diagonal")
                                if destPiece["team"] != 0:
                                    print("        Pawn moving to an opponent's square")
                                    return True
                                elif destPiece["team"] == 0:
                                    print("        Pawn moving to empty tile")
                                    if board[destinationX][destinationY + up]["enpassant"]:
                                        print("        Pawn performing En passant")
                                        return "enpassant"
                        elif locationY - destinationY == up * 2 and locationX == destinationX:
                            print("        Pawn is moving in the correct direction and is doing a double move")
                            if piece["moved"] == False and board[locationX][locationY - up]["name"] == "empty":
                                print("        Correct double move performance")
                                return "double"
                    else:
                        print("        The move is a pawn promotion")
                        if locationY - destinationY == up:
                            print("        Pawn is moving in the correct direction")
                            if locationX == destinationX:
                                print("        Pawn doing single step forward")
                                return "promote"
                            elif locationX - destinationX == 1 or locationX - destinationX == -1:
                                print("        Pawn moving diagonally to kill an opponent simultaneously")
                                if destPiece["team"] != 0:
                                    print("        Pawn moving to an opponent's square")
                                    return "promote"

                elif piece["name"] == "castle":
                    print("        Detected piece - castle")
                    if locationX == destinationX:
                        diff = locationY - destinationY
                        if diff > 0:
                            print("        Moving forward")
                            for i in range(diff):
                                if board[locationX][locationY - up * i]["name"] != "empty":
                                    if i != 0:
                                        return False
                            print("        No pieces in the way")
                            return True 
                        elif diff < 0:
                            print("        Moving backward")
                            for i in range(-diff):
                                if board[locationX][locationY + up * i]["name"] != "empty":
                                    if i != 0:
                                        return False
                            print("        No pieces in the way")
                            return True
                        else:
                            print("        Error 02")
                    elif locationY == destinationY:
                        diff = destinationX - locationX
                        if diff > 0:
                            print("        Moving to the right")
                            for i in range(diff):
                                if board[locationX + i][locationY]["name"] != "empty":
                                    if i != 0:
                                        return False
                            print("        No pieces in the way")
                            return True
                        elif diff < 0:
                            print("        Moving to the left")
                            for i in range(-diff):
                                if board[locationX - i][locationY]["name"] != "empty":
                                    if i != 0:
                                        return False
                            print("        No pieces in the way")
                            return True
                        else:
                            print("        Error 02")

                elif piece["name"] == "knight":
                    print("        Detected piece - knight")
                    if locationY - destinationY == up * 2:
                        if destinationX - locationX == 1 or destinationX - locationX == -1:
                            print("        Correct knight move")
                            return True
                    elif locationY - destinationY == up * 1:
                        if destinationX - locationX == 2 or destinationX - locationX == -2:
                            print("        Correct knight move")
                            return True
                    elif locationY - destinationY == -up * 1:
                        if destinationX - locationX == 2 or destinationX - locationX == -2:
                            print("        Correct knight move")
                            return True
                    elif locationY - destinationY == -up * 2:
                        if destinationX - locationX == 1 or destinationX - locationX == -1:
                            print("        Correct knight move")
                            return True

                elif piece["name"] == "bishop":
                    print("        Detected piece - bishop")
                    if locationY - destinationY == destinationX - locationX or locationY - destinationY == -(destinationX - locationX):
                        print("        Correctly moving diagonally")
                        Xdiff = destinationX - locationX
                        Ydiff = locationY - destinationY

                        absXdiff = abs(Xdiff)
                        absYdiff = abs(Ydiff)

                        Xdirection = int(Xdiff / absXdiff)
                        Ydirection = int(Ydiff / absYdiff)
                        
                        for i in range(absXdiff):
                            if board[locationX + (Xdirection * i)][locationY - up * (Ydirection * i)]["name"] != "empty":
                                if i != 0:
                                    return False
                        print("        Nothing in Bishop's way")
                        return True


                elif piece["name"] == "queen":
                    print("        Detected piece - queen")
                    if locationX == destinationX:
                        diff = locationY - destinationY
                        if diff > 0:
                            print("        Moving forward")
                            for i in range(diff):
                                if board[locationX][locationY - up * i]["name"] != "empty":
                                    if i != 0:
                                        return False
                            print("        No pieces in queen's way")
                            return True
                        elif diff < 0:
                            print("        Moving backward")
                            for i in range(-diff):
                                if board[locationX][locationY + up * i]["name"] != "empty":
                                    if i != 0:
                                        return False
                            print("        No pieces in queen's way")
                            return True
                    elif locationY == destinationY:
                        diff = destinationX - locationX
                        if diff > 0:
                            print("        Moving to the right")
                            for i in range(diff):
                                if board[locationX + i][locationY]["name"] != "empty":
                                    if i != 0:
                                        return False
                            print("        No pieces in queen's way")
                            return True
                        elif diff < 0:
                            print("        Moving to the left")
                            for i in range(-diff):
                                if board[locationX - i][locationY]["name"] != "empty":
                                    if i != 0:
                                        return False
                            print("        No pieces in queen's way")
                            return True

                    elif locationY - destinationY == destinationX - locationX or locationY - destinationY == -(destinationX - locationX):
                        print("        Moving diagonally")
                        Xdiff = destinationX - locationX
                        Ydiff = locationY - destinationY

                        absXdiff = abs(Xdiff)
                        absYdiff = abs(Ydiff)

                        Xdirection = int(Xdiff / absXdiff)
                        Ydirection = int(Ydiff / absYdiff)
                        
                        for i in range(absXdiff):
                            if board[locationX + (Xdirection * i)][locationY - up * (Ydirection * i)]["name"] != "empty":
                                if i != 0:
                                    return False
                        print("        No pieces in queen's way")
                        return True

                elif piece["name"] == "king":
                    print("        detected piece - king")
                    if locationY - destinationY <= 1 and locationY - destinationY >= -1:
                        if destinationX - locationX <= 1 and destinationX - locationX >= -1:
                            print("        ing moving only 1 step in any direction")
                            return True
                        elif locationY == destinationY:
                            if destinationX - locationX == 2 and destPiece["name"] == "empty" and board[locationX + 1][locationY]["name"] == "empty":
                                print("        King castling to the right")
                                return "castle right"
                            elif destinationX - locationX == -2 and destPiece["name"] == "empty" and board[locationX - 1][locationY]["name"] == "empty" and board[locationX - 3][locationY]["name"] == "empty":
                                print("        King castling to the left")
                                return "castle left"

    return False


main()
