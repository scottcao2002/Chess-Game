#creates class for opponent
class Opponent:
    global chessboard
    global PPlayer
    global board
    global side
    global onePlayer
    global opponentTurn
    global playerTurn
    global moves
    def __init__(self):
        self.P1 = Pawn(1, 0, 2, 17)
        self.P2 = Pawn(1, 1, 2, 18)
        self.P3 = Pawn(1, 2, 2, 19)
        self.P4 = Pawn(1, 3, 2, 20)
        self.P5 = Pawn(1, 4, 2, 21)
        self.P6 = Pawn(1, 5, 2, 22)
        self.P7 = Pawn(1, 6, 2, 23)
        self.P8 = Pawn(1, 7, 2, 24)
        self.R1 = Rook(0, 0, 2, 25)
        self.N1 = Knight(0, 1, 2, 26)
        self.B1 = Bishop(0, 2, 2, 27)
        self.B2 = Bishop(0, 5, 2, 28)
        self.N2 = Knight(0, 6, 2, 29)
        self.R2 = Rook(0, 7, 2, 30)
        if side == 0:
            self.Q = Queen(0, 3, 2, 31)
            self.K = opponentKing(0, 4, 2, 32)
        else:
            self.Q = Queen(0, 4, 2, 31)
            self.K = opponentKing(0, 3, 2, 32)
        self.allPieces = [self.P1, self.P2, self.P3, self.P4, self.P5, self.P6, self.P7, self.P8, self.R1, self.N1, self.B1, self.Q, self.K, self.B2, self.N2, self.R2]
    def getAllPieces(self):
        return self.allPieces
    def setAllPieces(self, pieces):
        self.allPieces = pieces
    def makesMove(self, lr = 0, lc = 0, cr = 0, cc = 0):
        #makes move for the opponent, AI opens with King's Indian defense
        for piece in self.allPieces:
            if type(piece) is Pawn:
                piece.movedTwo = False
        if onePlayer:
            bestScore = -maxsize - 1
            bestMove = []
            move = []
            depth = 2
            if moves == 1 and side == 1:
                move = [0, 1, 2, 2]
            else:
                if moves == 1:
                    if side == 0:
                        for piece in PPlayer.getAllPieces():
                            if type(piece) is Pawn:
                                if piece.getRow() == 4 and piece.getColumn() == 3:
                                    move = [0, 6, 2, 5]
                                    break
                                elif piece.getRow() == 4 and piece.getColumn() == 4:
                                    move = [1, 3, 2, 3]
                                    break
                            move = [0, 6, 2, 5]
                elif moves <= 7:
                    for piece in self.allPieces:
                        for possibility in piece.getPossibilities():
                            piece.tempMove(possibility[0],possibility[1])
                            score = minimax(1, -maxsize - 1, maxsize + 1, False)
                            piece.moveBack()
                            if score > bestScore:
                                bestScore = score
                                bestMove = [[piece.getRow(), piece.getColumn(), possibility[0], possibility[1]]]
                            elif score == bestScore:
                                bestMove.append([piece.getRow(), piece.getColumn(), possibility[0], possibility[1]])
                    if side == 0:
                        for possibility in bestMove:
                            if possibility == [0, 6, 2, 5]:
                                move = [0, 6, 2, 5]
                                break
                            elif possibility == [1, 3, 2, 3]:
                                move = [1, 3, 2, 3]
                                break
                            elif possibility == [1, 6, 2, 6]:
                                move = [1, 6, 2, 6]
                                break
                            elif possibility == [0, 5, 1, 6]:
                                move = [0, 5, 1, 6]
                                break
                            elif possibility == [0, 4, 0, 6]:
                                move = [0, 4, 0, 6]
                                break
                    else:
                        for possibility in bestMove:
                            if possibility == [1, 4, 2, 4]:
                                move = [1, 4, 2, 4]
                                break
                            elif possibility == [1, 1, 2, 1]:
                                move = [1, 1, 2, 1]
                                break
                            elif possibility == [0, 2, 1, 1]:
                                move = [0, 2, 1, 1]
                                break
                            elif possibility == [0, 3, 0, 1]:
                                move = [0, 3, 0, 1]
                                break
                if len(move) == 0:
                    for piece in self.allPieces:
                        for possibility in piece.getPossibilities():
                            piece.tempMove(possibility[0],possibility[1])
                            tempPlayerTurn = True
                            tempOpponentTurn = False
                            score = minimax(depth, -maxsize - 1, maxsize + 1, False)
                            piece.moveBack()
                            tempPlayerTurn = False
                            tempOpponentTurn = True
                            if score > bestScore:
                                bestScore = score
                                bestMove = [[piece.getRow(), piece.getColumn(), possibility[0], possibility[1]]]
                            elif score == bestScore:
                                bestMove.append([piece.getRow(), piece.getColumn(), possibility[0], possibility[1]])
                    move = bestMove[int(random.random()*len(bestMove))]
            for piece in self.allPieces:
                if piece.getRow() == move[0] and piece.getColumn() == move[1]:
                    movingPiece = piece
                    break
            pr = movingPiece.getRow()
            pc = movingPiece.getColumn()
            nr = move[2]
            nc = move[3]
        else:
            pr = lr
            pc = lc
            nr = cr
            nc = cc
            for piece in self.allPieces:
                if piece.getRow() == pr and piece.getColumn() == pc:
                    movingPiece = piece
        if type(movingPiece) is opponentKing and nc == pc - 2 and side != 0:
            self.castleKingSide()
            print("White castles kingside")
        elif type(movingPiece) is opponentKing and nc == pc - 2 and side == 0:
            self.castleQueenSide()
            print("Black castles queenside")
        elif type(movingPiece) is opponentKing and nc == pc + 2 and side != 0:
            self.castleQueenSide()
            print("White castles queenside")
        elif type(movingPiece) is opponentKing and nc == pc + 2 and side == 0:
            self.castleKingSide()
            print("Black castles kingside")
        elif type(movingPiece) is Pawn and chessboard[nr][nc].returnOccupant() == 0 and abs(nr - pr) == 1 and abs(nc - pc) == 1:
            print("Pawn captures En Passant:")
            movingPiece.moveManually(nr, nc)
            for piece in PPlayer.getAllPieces():
                if type(piece) is Pawn:
                    if piece.movedTwo:
                        chessboard[piece.getRow()][piece.getColumn()].setOccupant(0)
                        PPlayer.allPieces.remove(piece)
                        break
        else:
            if type(movingPiece) is Pawn and nr == pr +2:
                movingPiece.movedTwo = True
            if movingPiece.moveManually(nr, nc):
                PlayerPieces = PPlayer.getAllPieces()
                for piece in PlayerPieces:
                    if piece.getRow() == movingPiece.getRow() and piece.getColumn() == movingPiece.getColumn():
                        PlayerPieces.remove(piece)
                        break
                PPlayer.setAllPieces(PlayerPieces)
            if type(movingPiece) is Pawn and onePlayer:
                if movingPiece.getRow() == 7:
                    bestScore = -maxsize - 1
                    pieceRow = movingPiece.getRow()
                    pieceColumn = movingPiece.getColumn()
                    pieceID = movingPiece.ID
                    self.allPieces.remove(movingPiece)
                    choices = [Rook(pieceRow, pieceColumn, 2, pieceID),
                               Queen(pieceRow, pieceColumn, 2, pieceID),
                               Knight(pieceRow, pieceColumn, 2, pieceID),
                               Bishop(pieceRow, pieceColumn, 2, pieceID),]
                    for i in range(0, len(choices)):
                        self.allPieces.append(choices[i])
                        currentScore = POpponent.getScore()
                        if currentScore > bestScore:
                            choice = i
                            bestScore = currentScore
                        self.allPieces.pop()
                    self.allPieces.append(Pawn(pieceRow, pieceColumn, 2, pieceID))
                    self.promote(choice)
        if onePlayer:
            board.board[pr][pc].state = 3
            board.board[pr][pc].setColor((100, 0, 100))
            board.board[nr][nc].state = 3
            board.board[nr][nc].setColor((100, 0, 100))
    def getKing(self):
        return self.K
    def canMove(self):
        for piece in self.allPieces:
            if chessboard[piece.getRow()][piece.getColumn()].returnOccupant() == 2:
                if len(piece.getPossibilities()) != 0:
                    return 1
        if not self.K.isInCheck() and (opponentTurn or tempOpponentTurn):
            return 0
        else:
            return -1
    def canCastleKingSide(self):
        if side == 0:
            if not self.R2.hasMoved() and not self.K.hasMoved() and not self.K.isInCheck() and not self.R2.tempMoved and not self.K.tempMoved:
                if not chessboard[0][5].isAttackedByPlayer() and not chessboard[0][6].isAttackedByPlayer():
                    if chessboard[0][5].returnOccupant() == 0 and chessboard[0][6].returnOccupant() == 0 and chessboard[0][7].returnOccupant() == 2:
                        for piece in self.allPieces:
                            if type(piece) is Rook and piece.getRow() == 0 and piece.getColumn() == 7 and not piece.hasMoved() and not piece.tempMoved:
                                return True
            return False
        else:
            if not self.R1.hasMoved() and not self.K.hasMoved() and not self.K.isInCheck() and not self.R1.tempMoved and not self.K.tempMoved:
                if not chessboard[0][2].isAttackedByPlayer() and not chessboard[0][1].isAttackedByPlayer():
                    if chessboard[0][2].returnOccupant() == 0 and chessboard[0][1].returnOccupant() == 0 and chessboard[0][0].returnOccupant() == 2:
                        for piece in self.allPieces:
                            if type(piece) is Rook and piece.getRow() == 0 and piece.getColumn() == 0 and not piece.hasMoved() and not piece.tempMoved:
                                return True
            return False
    def canCastleQueenSide(self):
        if side == 0:
            if not self.R1.hasMoved() and not self.K.hasMoved() and not self.K.isInCheck() and not self.R1.tempMoved and not self.K.tempMoved:
                if not chessboard[0][2].isAttackedByPlayer() and not chessboard[0][3].isAttackedByPlayer():
                    if chessboard[0][2].returnOccupant() == 0 and chessboard[0][3].returnOccupant() == 0 and chessboard[0][0].returnOccupant() == 2:
                        for piece in self.allPieces:
                            if type(piece) is Rook and piece.getRow() == 0 and piece.getColumn() == 0 and not piece.hasMoved() and not piece.tempMoved:
                                return True
            return False
        else:
            if not self.R2.hasMoved() and not self.K.hasMoved() and not self.K.isInCheck() and not self.R2.tempMoved and not self.K.tempMoved:
                if not chessboard[0][5].isAttackedByPlayer() and not chessboard[0][4].isAttackedByPlayer():
                    if chessboard[0][5].returnOccupant() == 0 and chessboard[0][4].returnOccupant() == 0 and chessboard[0][7].returnOccupant() == 2:
                        for piece in self.allPieces:
                            if type(piece) is Rook and piece.getRow() == 0 and piece.getColumn() == 7 and not piece.hasMoved() and not piece.tempMoved:
                                return True
            return False
    def castleKingSide(self):
        if side == 0:
            self.R2.castleKingSide()
            self.K.castleKingSide()
        else:
            self.K.castleKingSide()
            self.R1.castleKingSide()
    def castleQueenSide(self):
        if side == 0:
            self.R1.castleQueenSide()
            self.K.castleQueenSide()
        else:
            self.K.castleQueenSide()
            self.R2.castleQueenSide()
    def canPromote(self):
        for piece in self.allPieces:
            if type(piece) is Pawn and piece.getRow() == 7:
                return True
        return False
    def promote(self, num):
        for piece in self.allPieces:
            if type(piece) is Pawn and piece.getRow() == 7:
                movingPiece = piece
        if num == 1:
            self.allPieces.append(Queen(movingPiece.getRow(), movingPiece.getColumn(), 2, movingPiece.ID))
            print("Pawn promotes to Queen")
        elif num == 2:
            self.allPieces.append(Knight(movingPiece.getRow(), movingPiece.getColumn(), 2, movingPiece.ID))
            print("Pawn promotes to Knight")
        elif num == 3:
            self.allPieces.append(Bishop(movingPiece.getRow(), movingPiece.getColumn(), 2, movingPiece.ID))
            print("Pawn promotes to Bishop")
        else:
            self.allPieces.append(Rook(movingPiece.getRow(), movingPiece.getColumn(), 2, movingPiece.ID))
            print("Pawn promotes to Rook")
        self.allPieces.remove(movingPiece)
    def getScore(self):
        #returns the score of the opponent's position for the AI
        if POpponent.canMove() == -1:
            return -maxsize
        elif PPlayer.canMove() == -1:
            return maxsize
        elif PPlayer.canMove() == 0 or POpponent.canMove() == 0:
            return 0
        else:
            valPlayer = 0
            for piece in PPlayer.getAllPieces():
                if chessboard[piece.getRow()][piece.getColumn()].piece == piece.ID:
                    if type(piece) is Pawn:
                        if piece.getRow() == 0:
                            valPlayer += 9
                        else:
                            valPlayer += 1
                    elif type(piece) is Knight:
                        valPlayer += 3
                    elif type(piece) is Bishop:
                        valPlayer += 3
                    elif type(piece) is Rook:
                        valPlayer += 5
                    elif type(piece) is Queen:
                        valPlayer += 9
            valOpponent = 0
            for piece in POpponent.getAllPieces():
                if chessboard[piece.getRow()][piece.getColumn()].piece == piece.ID:
                    if type(piece) is Pawn:
                        if piece.getRow() == 7:
                            valOpponent += 9
                        else:
                            valOpponent += 1
                    elif type(piece) is Knight:
                        valOpponent += 3
                    elif type(piece) is Bishop:
                        valOpponent += 3
                    elif type(piece) is Rook:
                        valOpponent += 5
                    elif type(piece) is Queen:
                        valOpponent += 9
            return valOpponent - valPlayer
