#creates class for the player
class HumanPlayer:
    #creates your player
    global chessboard
    global POpponent
    global side
    global opponentTurn
    global playerTurn
    global tempPlayerTurn
    global tempOpponentTurn
    def __init__(self):
        #initializes all your pieces
        self.P1 = Pawn(6, 0, 1, 1)
        self.P2 = Pawn(6, 1, 1, 2)
        self.P3 = Pawn(6, 2, 1, 3)
        self.P4 = Pawn(6, 3, 1, 4)
        self.P5 = Pawn(6, 4, 1, 5)
        self.P6 = Pawn(6, 5, 1, 6)
        self.P7 = Pawn(6, 6, 1, 7)
        self.P8 = Pawn(6, 7, 1, 8)
        self.R1 = Rook(7, 0, 1, 9)
        self.N1 = Knight(7, 1, 1, 10)
        self.B1 = Bishop(7, 2, 1, 11)
        self.B2 = Bishop(7, 5, 1, 12)
        self.N2 = Knight(7, 6, 1, 13)
        self.R2 = Rook(7, 7, 1, 14)
        if side == 0:
            self.Q = Queen(7, 3, 1, 15)
            self.K = playerKing(7, 4, 1, 16)
        else:
            self.Q = Queen(7, 4, 1, 15)
            self.K = playerKing(7, 3, 1, 16)
        self.allPieces = [self.P1, self.P2, self.P3, self.P4, self.P5, self.P6, self.P7, self.P8, self.R1, self.N1, self.B1, self.Q, self.K, self.B2, self.N2, self.R2]
    def getAllPieces(self):
        return self.allPieces
    def setAllPieces(self, pieces):
        self.allPieces = pieces
    def getKing(self):
        return self.K
    def canMove(self):
        #returns 0 for stalemate, -1 for checkmate, 1 if you can still move
        for piece in self.allPieces:
            if chessboard[piece.getRow()][piece.getColumn()].returnOccupant() == 1:
                if len(piece.getPossibilities()) != 0:
                    return 1
        if not self.K.isInCheck() and (playerTurn or tempPlayerTurn):
            return 0
        else:
            return -1
    def makesMove(self, pr, pc, nr, nc):
        #makes the move for the player
        for piece in self.allPieces:
            if type(piece) is Pawn:
                piece.movedTwo = False
        for piece in self.allPieces:
            if piece.getRow() == pr and piece.getColumn() == pc:
                movingPiece = piece
        if type(movingPiece) is playerKing and nc == pc - 2 and side != 0:
            self.castleKingSide()
            print("Black castles kingside")
        elif type(movingPiece) is playerKing and nc == pc - 2 and side == 0:
            self.castleQueenSide()
            print("White castles queenside")
        elif type(movingPiece) is playerKing and nc == pc + 2 and side != 0:
            self.castleQueenSide()
            print("Black castles queenside")
        elif type(movingPiece) is playerKing and nc == pc + 2 and side == 0:
            self.castleKingSide()
            print("White castles kingside")
        elif type(movingPiece) is Pawn and chessboard[nr][nc].returnOccupant() == 0 and abs(nr - pr) == 1 and abs(nc - pc) == 1:
            print("Pawn captures En Passant:")
            movingPiece.moveManually(nr, nc)
            for piece in POpponent.getAllPieces():
                if type(piece) is Pawn:
                    if piece.movedTwo:
                        chessboard[piece.getRow()][piece.getColumn()].setOccupant(0)
                        POpponent.allPieces.remove(piece)
                        break
        else:
            if type(movingPiece) is Pawn and nr == pr -2:
                movingPiece.movedTwo = True
            if movingPiece.moveManually(nr, nc):
                OpponentPieces = POpponent.getAllPieces()
                for piece in OpponentPieces:
                    if piece.getRow() == movingPiece.getRow() and piece.getColumn() == movingPiece.getColumn():
                        OpponentPieces.remove(piece)
                        break
                POpponent.setAllPieces(OpponentPieces)
    def canPromote(self):
        #determines whether a pawn can promote
        for piece in self.allPieces:
            if type(piece) is Pawn and piece.getRow() == 0:
                return True
        return False
    def promote(self, num):
        #promotes the pawn
        for piece in self.allPieces:
            if type(piece) is Pawn and piece.getRow() == 0:
                movingPiece = piece
        if num == 1:
            self.allPieces.append(Queen(movingPiece.getRow(), movingPiece.getColumn(), 1, movingPiece.ID))
            print("Pawn promotes to Queen")
        elif num == 2:
            self.allPieces.append(Knight(movingPiece.getRow(), movingPiece.getColumn(), 1, movingPiece.ID))
            print("Pawn promotes to Knight")
        elif num == 3:
            self.allPieces.append(Bishop(movingPiece.getRow(), movingPiece.getColumn(), 1, movingPiece.ID))
            print("Pawn promotes to Bishop")
        else:
            self.allPieces.append(Rook(movingPiece.getRow(), movingPiece.getColumn(), 1, movingPiece.ID))
            print("Pawn promotes to Rook")
        self.allPieces.remove(movingPiece)
    def canCastleKingSide(self):
        #determines whether kingside castling is possible
        if side == 0:
            if not self.R2.hasMoved() and not self.K.hasMoved() and not self.K.isInCheck() and not self.R2.tempMoved and not self.K.tempMoved:
                if not chessboard[7][5].isAttackedByOpponent() and not chessboard[7][6].isAttackedByOpponent():
                    if chessboard[7][5].returnOccupant() == 0 and chessboard[7][6].returnOccupant() == 0 and chessboard[7][7].returnOccupant()==1:
                        for piece in self.allPieces:
                            if piece.getRow() == 7 and piece.getColumn() == 7 and not piece.hasMoved() and not piece.tempMoved:
                                return True
            return False
        else:
            if not self.R1.hasMoved() and not self.K.hasMoved() and not self.K.isInCheck() and not self.R1.tempMoved and not self.K.tempMoved:
                if not chessboard[7][2].isAttackedByOpponent() and not chessboard[7][1].isAttackedByOpponent():
                    if chessboard[7][2].returnOccupant() == 0 and chessboard[7][1].returnOccupant() == 0 and chessboard[7][0].returnOccupant() == 1:
                        for piece in self.allPieces:
                            if type(piece) is Rook and piece.getRow() == 7 and piece.getColumn() == 0 and not piece.hasMoved() and not piece.tempMoved:
                                return True
            return False
    def canCastleQueenSide(self):
        #determines whether queenside castling is possible
        if side == 0:
            if not self.R1.hasMoved() and not self.K.hasMoved() and not self.K.isInCheck() and not self.R1.tempMoved and not self.K.tempMoved:
                if not chessboard[7][2].isAttackedByOpponent() and not chessboard[7][3].isAttackedByOpponent():
                    if chessboard[7][2].returnOccupant() == 0 and chessboard[7][3].returnOccupant() == 0 and chessboard[7][0].returnOccupant() == 1:
                        for piece in self.allPieces:
                            if type(piece) is Rook and piece.getRow() == 7 and piece.getColumn() == 0 and not piece.hasMoved() and not piece.tempMoved:
                                return True
            return False
        else:
            if not self.R2.hasMoved() and not self.K.hasMoved() and not self.K.isInCheck() and not self.R2.tempMoved and not self.K.tempMoved:
                if not chessboard[7][4].isAttackedByOpponent() and not chessboard[7][5].isAttackedByOpponent():
                    if chessboard[7][4].returnOccupant() == 0 and chessboard[7][5].returnOccupant() == 0 and chessboard[7][0].returnOccupant() == 1:
                        for piece in self.allPieces:
                            if type(piece) is Rook and piece.getRow() == 7 and piece.getColumn() == 7 and not piece.hasMoved() and not piece.tempMoved:
                                return True
            return False
    def castleKingSide(self):
        #to castle kingside
        if side == 0:
            self.K.castleKingSide()
            self.R2.castleKingSide()
        else:
            self.K.castleKingSide()
            self.R1.castleKingSide()
    def castleQueenSide(self):
        #to castle queenside
        if side == 0:
            self.K.castleQueenSide()
            self.R1.castleQueenSide()
        else:
            self.K.castleQueenSide()
            self.R2.castleQueenSide()
