class Knight:
    global chessboard
    def __init__(self, row, column, player, ID):
        self.row = row
        self.column = column
        self.player = player
        self.ID = ID
        self.orow = []
        self.ocol = []
        self.oocc = []
        self.ppieces = []
        chessboard[row][column].setOccupant(player)
        chessboard[row][column].piece = ID
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def getPossibilities(self):
        possibilities = chessboard[self.row][self.column].KnightCanMove()
        return possibilities
    def AllPossibilities(self):
        possibilities = chessboard[self.row][self.column].KnightCanAttack()
        return possibilities
    def moveManually(self, newRow, newColumn):
        print("Knight from " , chessboard[self.row][self.column], " to ", chessboard[newRow][newColumn])
        isCapture = False
        if chessboard[newRow][newColumn].returnOccupant()!=0:
            isCapture = True
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
        return isCapture
    def tempMove(self, newRow, newColumn):
        self.oocc.append(chessboard[newRow][newColumn].returnOccupant())
        self.ppieces.append(chessboard[newRow][newColumn].piece)
        self.orow.append(self.row)
        self.ocol.append(self.column)
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
    def moveBack(self):
        chessboard[self.row][self.column].setOccupant(self.oocc.pop())
        chessboard[self.row][self.column].piece = self.ppieces.pop()
        chessboard[self.orow[-1]][self.ocol[-1]].setOccupant(self.player)
        self.row = self.orow.pop()
        self.column = self.ocol.pop()
        chessboard[self.row][self.column].piece = self.ID
class Bishop:
    global chessboard
    def __init__(self, row, column, player, ID):
        self.row = row
        self.column = column
        self.player = player
        self.ID = ID
        self.orow = []
        self.ocol = []
        self.oocc = []
        self.ppieces= []
        chessboard[row][column].setOccupant(player)
        chessboard[row][column].piece = ID
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def getPossibilities(self):
        possibilities = chessboard[self.row][self.column].BishopCanMove()
        return possibilities
    def AllPossibilities(self):
        possibilities = chessboard[self.row][self.column].BishopCanAttack()
        return possibilities
    def moveManually(self, newRow, newColumn):
        print("Bishop from " , chessboard[self.row][self.column], " to ", chessboard[newRow][newColumn])
        isCapture = False
        if chessboard[newRow][newColumn].returnOccupant()!=0:
            isCapture = True
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
        return isCapture
    def tempMove(self, newRow, newColumn):
        self.oocc.append(chessboard[newRow][newColumn].returnOccupant())
        self.ppieces.append(chessboard[newRow][newColumn].piece)
        self.orow.append(self.row)
        self.ocol.append(self.column)
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
    def moveBack(self):
        chessboard[self.row][self.column].setOccupant(self.oocc.pop())
        chessboard[self.row][self.column].piece = self.ppieces.pop()
        chessboard[self.orow[-1]][self.ocol[-1]].setOccupant(self.player)
        self.row = self.orow.pop()
        self.column = self.ocol.pop()
        chessboard[self.row][self.column].piece = self.ID
class Queen:
    global chessboard
    def __init__(self, row, column, player, ID):
        self.row = row
        self.column = column
        self.player = player
        self.ID = ID
        self.orow = []
        self.ocol = []
        self.oocc = []
        self.ppieces = []
        chessboard[row][column].setOccupant(player)
        chessboard[row][column].piece = ID
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def getPossibilities(self):
        possibilities = chessboard[self.row][self.column].QueenCanMove()
        return possibilities
    def AllPossibilities(self):
        possibilities = chessboard[self.row][self.column].QueenCanAttack()
        return possibilities
    def moveManually(self, newRow, newColumn):
        print("Queen from " , chessboard[self.row][self.column], " to ", chessboard[newRow][newColumn])
        isCapture = False
        if chessboard[newRow][newColumn].returnOccupant()!=0:
            isCapture = True
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
        return isCapture
    def tempMove(self, newRow, newColumn):
        self.oocc.append(chessboard[newRow][newColumn].returnOccupant())
        self.ppieces.append(chessboard[newRow][newColumn].piece)
        self.orow.append(self.row)
        self.ocol.append(self.column)
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
    def moveBack(self):
        chessboard[self.row][self.column].setOccupant(self.oocc.pop())
        chessboard[self.row][self.column].piece = self.ppieces.pop()
        chessboard[self.orow[-1]][self.ocol[-1]].setOccupant(self.player)
        self.row = self.orow.pop()
        self.column = self.ocol.pop()
        chessboard[self.row][self.column].piece = self.ID
class Rook:
    global chessboard
    global side
    def __init__(self, row, column, player, ID):
        self.row = row
        self.column = column
        self.player = player
        self.ID = ID
        self.moved = 0
        self.orow = []
        self.ocol = []
        self.oocc = []
        self.ppieces = []
        self.tempMoved = 0
        chessboard[row][column].setOccupant(player)
        chessboard[row][column].piece = ID
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def getPossibilities(self):
        possibilities = chessboard[self.row][self.column].RookCanMove()
        return possibilities
    def AllPossibilities(self):
        possibilities = chessboard[self.row][self.column].RookCanAttack()
        return possibilities
    def moveManually(self, newRow, newColumn):
        print("Rook from " , chessboard[self.row][self.column], " to ", chessboard[newRow][newColumn])
        self.moved = 1
        isCapture = False
        if chessboard[newRow][newColumn].returnOccupant()!=0:
            isCapture = True
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
        return isCapture
    def castleKingSide(self):
        if side == 0:
            if self.player == 1:
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][5].setOccupant(self.player)
                chessboard[7][5].piece = self.ID
                self.row = 7
                self.column = 5
            elif self.player == 2:
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][5].setOccupant(self.player)
                chessboard[0][5].piece = self.ID
                self.row = 0
                self.column = 5
        else:
            if self.player == 1:
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][2].setOccupant(self.player)
                chessboard[7][2].piece = self.ID
                self.row = 7
                self.column = 2
            elif self.player == 2:
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][2].setOccupant(self.player)
                chessboard[0][2].piece = self.ID
                self.row = 0
                self.column = 2
        self.moved = 1
    def castleQueenSide(self):
        if side == 0:
            if self.player == 1:
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][3].setOccupant(self.player)
                chessboard[7][3].piece = self.ID
                self.row = 7
                self.column = 3
            elif self.player == 2:
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][3].setOccupant(self.player)
                chessboard[0][3].piece = self.ID
                self.row = 0
                self.column = 3
        else:
            if self.player == 1:
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][4].setOccupant(self.player)
                chessboard[7][4].piece = self.ID
                self.row = 7
                self.column = 4
            elif self.player == 2:
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][4].setOccupant(self.player)
                chessboard[0][4].piece = self.ID
                self.row = 0
                self.column = 4
        self.moved = 1
    def hasMoved(self):
        if self.moved == 0:
            return False
        return True
    def tempMove(self, newRow, newColumn):
        self.tempMoved += 1
        self.oocc.append(chessboard[newRow][newColumn].returnOccupant())
        self.ppieces.append(chessboard[newRow][newColumn].piece)
        self.orow.append(self.row)
        self.ocol.append(self.column)
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
    def moveBack(self):
        self.tempMoved -= 1
        chessboard[self.row][self.column].setOccupant(self.oocc.pop())
        chessboard[self.row][self.column].piece = self.ppieces.pop()
        chessboard[self.orow[-1]][self.ocol[-1]].setOccupant(self.player)
        self.row = self.orow.pop()
        self.column = self.ocol.pop()
        chessboard[self.row][self.column].piece = self.ID
class Pawn:
    global chessboard
    def __init__(self, row, column, player, ID):
        self.row = row
        self.column = column
        self.player = player
        self.ID = ID
        self.orow = []
        self.ocol = []
        self.oocc = []
        self.ppieces = []
        self.urow = 0
        self.ucol = 0
        self.uocc = 0
        self.tempEnPassant = []
        self.movedTwo = False
        self.tempMovedTwo = False
        chessboard[row][column].setOccupant(player)
        chessboard[row][column].piece = ID
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def getPossibilities(self):
        possibilities = chessboard[self.row][self.column].PawnCanMove()
        return possibilities
    def AllPossibilities(self):
        possibilities = chessboard[self.row][self.column].PawnCanAttack()
        return possibilities
    def moveManually(self, newRow, newColumn):
        print("Pawn from " , chessboard[self.row][self.column], " to ", chessboard[newRow][newColumn])
        isCapture = False
        if chessboard[newRow][newColumn].returnOccupant()!=0:
            isCapture = True
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
        return isCapture
    def tempMove(self, newRow, newColumn):
        if abs(newRow - self.row) == 2:
            self.tempMovedTwo = True
        if abs(newRow - self.row) == 1 and abs(newColumn - self.column) == 1 and chessboard[newRow][newColumn].returnOccupant() == 0:
            self.tempEnPassant.append(True)
            self.ucol = newColumn
            self.urow = self.row
            self.uocc = chessboard[self.urow][self.ucol].returnOccupant()
            self.ppieces.append(chessboard[self.urow][self.ucol].piece)
            chessboard[self.urow][self.ucol].setOccupant(0)
            chessboard[self.urow][self.ucol].piece = 0
        else:
            self.tempEnPassant.append(False)
            self.ppieces.append(chessboard[newRow][newColumn].piece)
        self.oocc.append(chessboard[newRow][newColumn].returnOccupant())
        self.orow.append(self.row)
        self.ocol.append(self.column)
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
    def moveBack(self):
        self.tempMovedTwo = False
        if self.tempEnPassant.pop():
            chessboard[self.urow][self.ucol].setOccupant(self.uocc)
            chessboard[self.urow][self.ucol].piece = self.ppieces.pop()
            chessboard[self.row][self.column].piece = 0
        else:
            chessboard[self.row][self.column].piece = self.ppieces.pop()
        chessboard[self.row][self.column].setOccupant(self.oocc.pop())
        chessboard[self.orow[-1]][self.ocol[-1]].setOccupant(self.player)
        self.row = self.orow.pop()
        self.column = self.ocol.pop()
        chessboard[self.row][self.column].piece = self.ID
class playerKing:
    global chessboard
    global side
    def __init__(self, row, column, player, ID):
        self.row = row
        self.column = column
        self.player = player
        self.ID = ID
        self.moved = 0
        self.orow = []
        self.ocol = []
        self.oocc = []
        self.ppieces = []
        self.kingCastle = []
        self.queenCastle = []
        self.tempMoved = 0
        chessboard[row][column].setOccupant(player)
        chessboard[row][column].piece = ID
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def getPossibilities(self):
        possibilities = chessboard[self.row][self.column].KingCanMove()
        return possibilities
    def AllPossibilities(self):
        return chessboard[self.row][self.column].KingCanAttack()
    def isInCheck(self):
        if chessboard[self.row][self.column].isAttackedByOpponent():
            return True
        return False
    def moveManually(self, newRow, newColumn):
        print("King from " , chessboard[self.row][self.column], " to ", chessboard[newRow][newColumn])
        self.moved = 1
        isCapture = False
        if chessboard[newRow][newColumn].returnOccupant()!=0:
            isCapture = True
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
        return isCapture
    def castleKingSide(self):
        if side == 0:
            chessboard[self.row][self.column].setOccupant(0)
            chessboard[self.row][self.column].piece = 0
            chessboard[7][6].setOccupant(self.player)
            chessboard[7][6].piece = self.ID
            self.row = 7
            self.column = 6
            self.moved = 1
        else:
            chessboard[self.row][self.column].setOccupant(0)
            chessboard[self.row][self.column].piece = 0
            chessboard[7][1].setOccupant(self.player)
            chessboard[7][1].piece = self.ID
            self.row = 7
            self.column = 1
            self.moved = 1
    def castleQueenSide(self):
        if side == 0:
            chessboard[self.row][self.column].setOccupant(0)
            chessboard[self.row][self.column].piece = 0
            chessboard[7][2].setOccupant(self.player)
            chessboard[7][2].piece = self.ID
            self.row = 7
            self.column = 2
            self.moved = 1
        else:
            chessboard[self.row][self.column].setOccupant(0)
            chessboard[self.row][self.column].piece = 0
            chessboard[7][5].setOccupant(self.player)
            chessboard[7][5].piece = self.ID
            self.row = 7
            self.column = 5
            self.moved = 1
    def hasMoved(self):
        if self.moved == 0:
            return False
        return True
    def tempMove(self, newRow, newColumn):
        self.tempMoved += 1
        if side == 0:
            if newColumn - self.column == 2:
                self.kingCastle.append(True)
                self.queenCastle.append(False)
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][6].setOccupant(1)
                chessboard[7][6].piece = self.ID
                self.row = 7
                self.column = 6
                for piece in PPlayer.getAllPieces():
                    if piece.getRow() == 7 and piece.getColumn() == 7:
                        chessboard[7][7].setOccupant(0)
                        chessboard[7][5].piece = chessboard[7][7].piece
                        chessboard[7][5].setOccupant(1)
                        chessboard[7][7].piece = 0
                        piece.row = 7
                        piece.column = 5
                        return
            elif self.column - newColumn == 2:
                self.queenCastle.append(True)
                self.kingCastle.append(False)
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][2].setOccupant(1)
                chessboard[7][2].piece = self.ID
                self.row = 7
                self.column = 2
                for piece in PPlayer.getAllPieces():
                    if piece.getRow() == 7 and piece.getColumn() == 0:
                        chessboard[7][0].setOccupant(0)
                        chessboard[7][3].piece = chessboard[7][0].piece 
                        chessboard[7][3].setOccupant(1)
                        chessboard[7][0].piece = 0
                        piece.row = 7
                        piece.column = 3
                        return
        else:
            if self.column - newColumn == 2:
                self.kingCastle.append(True)
                self.queenCastle.append(False)
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][1].setOccupant(1)
                chessboard[7][1].piece = self.ID
                self.row = 7
                self.column = 1
                for piece in PPlayer.getAllPieces():
                    if piece.getRow() == 7 and piece.getColumn() == 0:
                        chessboard[7][0].setOccupant(0)
                        chessboard[7][2].piece = chessboard[7][0].piece
                        chessboard[7][2].setOccupant(1)
                        chessboard[7][0].piece = 0
                        piece.row = 7
                        piece.column = 2
                        return
            elif newColumn - self.column == 2:
                self.queenCastle.append(True)
                self.kingCastle.append(False)
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][5].setOccupant(1)
                chessboard[7][5].piece = self.ID
                self.row = 7
                self.column = 5
                for piece in PPlayer.getAllPieces():
                    if piece.getRow() == 7 and piece.getColumn() == 7:
                        chessboard[7][7].setOccupant(0)
                        chessboard[7][4].piece = chessboard[7][7].piece
                        chessboard[7][4].setOccupant(1)
                        chessboard[7][7].piece = 0
                        piece.row = 7
                        piece.column = 4
                        return
        self.queenCastle.append(False)
        self.kingCastle.append(False)
        self.oocc.append(chessboard[newRow][newColumn].returnOccupant())
        self.ppieces.append(chessboard[newRow][newColumn].piece)
        self.orow.append(self.row)
        self.ocol.append(self.column)
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
    def moveBack(self):
        self.tempMoved -= 1
        if side == 0:
            if self.kingCastle[-1]:
                self.kingCastle.pop()
                self.queenCastle.pop()
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][4].setOccupant(1)
                chessboard[7][4].piece = self.ID
                self.row = 7
                self.column = 4
                for piece in PPlayer.getAllPieces():
                    if piece.getRow() == 7 and piece.getColumn() == 5:
                        chessboard[7][5].setOccupant(0)
                        chessboard[7][7].piece = chessboard[7][5].piece
                        chessboard[7][7].setOccupant(1)
                        chessboard[7][5].piece = 0
                        piece.row = 7
                        piece.column = 7
                        return
            elif self.queenCastle[-1]:
                self.queenCastle.pop()
                self.kingCastle.pop()
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][4].setOccupant(1)
                chessboard[7][4].piece = self.ID
                self.row = 7
                self.column = 4
                for piece in PPlayer.getAllPieces():
                    if piece.getRow() == 7 and piece.getColumn() == 3:
                        chessboard[7][3].setOccupant(0)
                        chessboard[7][0].piece = chessboard[7][3].piece
                        chessboard[7][0].setOccupant(1)
                        chessboard[7][3].piece = 0
                        piece.row = 7
                        piece.column = 0
                        return
        else:
            if self.kingCastle[-1]:
                self.kingCastle.pop()
                self.queenCastle.pop()
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][3].setOccupant(1)
                chessboard[7][3].piece = self.ID
                self.row = 7
                self.column = 3
                for piece in PPlayer.getAllPieces():
                    if piece.getRow() == 7 and piece.getColumn() == 2:
                        chessboard[7][2].setOccupant(0)
                        chessboard[7][0].piece = chessboard[7][2].piece
                        chessboard[7][0].setOccupant(1)
                        chessboard[7][2].piece = 0
                        piece.row = 7
                        piece.column = 0
                        return
            elif self.queenCastle[-1]:
                self.queenCastle.pop()
                self.kingCastle.pop()
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[7][3].setOccupant(1)
                chessboard[7][3].piece = self.ID
                self.row = 7
                self.column = 3
                for piece in PPlayer.getAllPieces():
                    if piece.getRow() == 7 and piece.getColumn() == 4:
                        chessboard[7][4].setOccupant(0)
                        chessboard[7][7].piece = chessboard[7][4].piece
                        chessboard[7][7].setOccupant(1)
                        chessboard[7][4].piece = 0
                        piece.row = 7
                        piece.column = 7
                        return
        self.kingCastle.pop()
        self.queenCastle.pop()
        chessboard[self.row][self.column].setOccupant(self.oocc.pop())
        chessboard[self.row][self.column].piece = self.ppieces.pop()
        chessboard[self.orow[-1]][self.ocol[-1]].setOccupant(self.player)
        self.row = self.orow.pop()
        self.column = self.ocol.pop()
        chessboard[self.row][self.column].piece = self.ID
class opponentKing:
    global chessboard
    global side
    def __init__(self, row, column, player, ID):
        self.row = row
        self.column = column
        self.player = player
        self.ID = ID
        self.moved = 0
        self.orow = []
        self.ocol = []
        self.oocc = []
        self.ppieces = []
        self.kingCastle = []
        self.queenCastle = []
        self.tempMoved = 0
        chessboard[row][column].setOccupant(player)
        chessboard[row][column].piece = ID
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def getPossibilities(self):
        possibilities = chessboard[self.row][self.column].KingCanMove()
        return possibilities
    def AllPossibilities(self):
        return chessboard[self.row][self.column].KingCanAttack()
    def moveManually(self, newRow, newColumn):
        print("King from " , chessboard[self.row][self.column], " to ", chessboard[newRow][newColumn])
        self.moved = 1
        isCapture = False
        if chessboard[newRow][newColumn].returnOccupant()!=0:
            isCapture = True
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
        return isCapture
    def isInCheck(self):
        if chessboard[self.row][self.column].isAttackedByPlayer():
            return True
        return False
    def castleKingSide(self):
        if side == 0:
            chessboard[self.row][self.column].setOccupant(0)
            chessboard[self.row][self.column].piece = 0
            chessboard[0][6].setOccupant(self.player)
            chessboard[0][6].piece = self.ID
            self.row = 0
            self.column = 6
            self.moved = 1
        else:
            chessboard[self.row][self.column].setOccupant(0)
            chessboard[self.row][self.column].piece = 0
            chessboard[0][1].setOccupant(self.player)
            chessboard[0][1].piece = self.ID
            self.row = 0
            self.column = 1
            self.moved = 1
    def castleQueenSide(self): 
        if side == 0:
            chessboard[self.row][self.column].setOccupant(0)
            chessboard[self.row][self.column].piece = 0
            chessboard[0][2].setOccupant(self.player)
            chessboard[0][2].piece = self.ID
            self.row = 0
            self.column = 2
            self.moved = 1
        else:
            chessboard[self.row][self.column].setOccupant(0)
            chessboard[self.row][self.column].piece = 0
            chessboard[0][5].setOccupant(self.player)
            chessboard[0][5].piece = self.ID
            self.row = 0
            self.column = 5
            self.moved = 1
    def hasMoved(self):
        if self.moved == 0:
            return False
        return True
    def tempMove(self, newRow, newColumn):
        self.tempMoved += 1
        if side == 0:
            if newColumn - self.column == 2:
                self.kingCastle.append(True)
                self.queenCastle.append(False)
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][6].setOccupant(2)
                chessboard[0][6].piece = self.ID
                self.row = 0
                self.column = 6
                for piece in POpponent.getAllPieces():
                    if piece.getRow() == 0 and piece.getColumn() == 7:
                        chessboard[0][7].setOccupant(0)
                        chessboard[0][5].piece = chessboard[0][7].piece
                        chessboard[0][5].setOccupant(2)
                        chessboard[0][7].piece = 0
                        piece.row = 0
                        piece.column = 5
                        return
            elif self.column - newColumn == 2:
                self.queenCastle.append(True)
                self.kingCastle.append(False)
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][2].setOccupant(2)
                chessboard[0][2].piece = self.ID
                self.row = 0
                self.column = 2
                for piece in POpponent.getAllPieces():
                    if piece.getRow() == 0 and piece.getColumn() == 0:
                        chessboard[0][0].setOccupant(0)
                        chessboard[0][3].piece = chessboard[0][0].piece
                        chessboard[0][3].setOccupant(2)
                        chessboard[0][0].piece = 0
                        piece.row = 0
                        piece.column = 3
                        return
        else:
            if self.column - newColumn == 2:
                self.kingCastle.append(True)
                self.queenCastle.append(False)
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][1].setOccupant(2)
                chessboard[0][1].piece = self.ID
                self.row = 0
                self.column = 1
                for piece in POpponent.getAllPieces():
                    if piece.getRow() == 0 and piece.getColumn() == 0:
                        chessboard[0][0].setOccupant(0)
                        chessboard[0][2].piece = chessboard[0][0].piece
                        chessboard[0][2].setOccupant(2)
                        chessboard[0][0].piece = 0
                        piece.row = 0
                        piece.column = 2
                        return
            elif newColumn - self.column == 2:
                self.queenCastle.append(True)
                self.kingCastle.append(False)
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][5].setOccupant(2)
                chessboard[0][5].piece = self.ID
                self.row = 0
                self.column = 5
                for piece in POpponent.getAllPieces():
                    if piece.getRow() == 0 and piece.getColumn() == 7:
                        chessboard[0][7].setOccupant(0)
                        chessboard[0][4].piece = chessboard[0][7].piece
                        chessboard[0][4].setOccupant(2)
                        chessboard[0][7].piece = 0
                        piece.row = 0
                        piece.column = 4
                        return
        self.queenCastle.append(False)
        self.kingCastle.append(False)
        self.oocc.append(chessboard[newRow][newColumn].returnOccupant())
        self.ppieces.append(chessboard[newRow][newColumn].piece)
        self.orow.append(self.row)
        self.ocol.append(self.column)
        chessboard[self.row][self.column].setOccupant(0)
        chessboard[self.row][self.column].piece = 0
        chessboard[newRow][newColumn].setOccupant(self.player)
        chessboard[newRow][newColumn].piece = self.ID
        self.row = newRow
        self.column = newColumn
    def moveBack(self):
        self.tempMoved -= 1
        if side == 0:
            if self.kingCastle[-1]:
                self.kingCastle.pop()
                self.queenCastle.pop()
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][4].setOccupant(2)
                chessboard[0][4].piece = self.ID
                self.row = 0
                self.column = 4
                for piece in POpponent.getAllPieces():
                    if piece.getRow() == 0 and piece.getColumn() == 5:
                        chessboard[0][5].setOccupant(0)
                        chessboard[0][7].piece = chessboard[0][5].piece
                        chessboard[0][7].setOccupant(2)
                        chessboard[0][5].piece = 0
                        piece.row = 0
                        piece.column = 7
                        return
            elif self.queenCastle[-1]:
                self.queenCastle.pop()
                self.kingCastle.pop()
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][4].setOccupant(2)
                chessboard[0][4].piece = self.ID
                self.row = 0
                self.column = 4
                for piece in POpponent.getAllPieces():
                    if piece.getRow() == 0 and piece.getColumn() == 3:
                        chessboard[0][3].setOccupant(0)
                        chessboard[0][0].piece = chessboard[0][3].piece
                        chessboard[0][0].setOccupant(2)
                        chessboard[0][3].piece = 0
                        piece.row = 0
                        piece.column = 0
                        return
        else:
            if self.kingCastle[-1]:
                self.kingCastle.pop()
                self.queenCastle.pop()
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][3].setOccupant(2)
                chessboard[0][3].piece = self.ID
                self.row = 0
                self.column = 3
                for piece in POpponent.getAllPieces():
                    if piece.getRow() == 0 and piece.getColumn() == 2:
                        chessboard[0][2].setOccupant(0)
                        chessboard[0][0].piece = chessboard[0][2].piece
                        chessboard[0][0].setOccupant(2)
                        chessboard[0][2].piece = 0
                        piece.row = 0
                        piece.column = 0
                        return
            elif self.queenCastle[-1]:
                self.queenCastle.pop()
                self.kingCastle.pop()
                chessboard[self.row][self.column].setOccupant(0)
                chessboard[self.row][self.column].piece = 0
                chessboard[0][3].setOccupant(2)
                chessboard[0][3].piece = self.ID
                self.row = 0
                self.column = 3
                for piece in POpponent.getAllPieces():
                    if piece.getRow() == 0 and piece.getColumn() == 4:
                        chessboard[0][4].setOccupant(0)
                        chessboard[0][7].piece = chessboard[0][4].piece
                        chessboard[0][7].setOccupant(2)
                        chessboard[0][4].piece = 0
                        piece.row = 0
                        piece.column = 7
                        return
        self.kingCastle.pop()
        self.queenCastle.pop()
        chessboard[self.row][self.column].setOccupant(self.oocc.pop())
        chessboard[self.row][self.column].piece = self.ppieces.pop()
        chessboard[self.orow[-1]][self.ocol[-1]].setOccupant(self.player)
        self.row = self.orow.pop()
        self.column = self.ocol.pop()
        chessboard[self.row][self.column].piece = self.ID
