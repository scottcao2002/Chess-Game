#class for each square on the chessboard
class Square:
    global chessboard
    global POpponent
    global PPlayer
    global side
    def __init__(self, row, column, occupant, piece = 0):
        #Creates the row and column for each square. The occupant is 1 for the player and 2 for the opponent
        #The piece variable contains the piece that is on the square
        self.r = row
        self.c = column
        self.occ = occupant
        self.piece = piece
    def setOccupant(self, occ):
        self.occ = occ
    def returnOccupant(self):
        return self.occ
    #returns all squares a knight can move to
    def KnightCanMove(self):
        poss = []
        if self.r + 2 < 8 and self.c + 1 < 8 and chessboard[self.r + 2, self.c + 1].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[self.r + 2][self.c + 1].returnOccupant()
            chessboard[self.r + 2][self.c + 1].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([self.r+2, self.c + 1])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([self.r+2, self.c + 1])
            chessboard[self.r+2][self.c+1].setOccupant(temp2)
            self.occ = temp
        if self.r + 1 < 8 and self.c + 2 < 8 and chessboard[self.r + 1, self.c + 2].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[self.r + 1][self.c + 2].returnOccupant()
            chessboard[self.r + 1][self.c + 2].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([self.r+1, self.c + 2])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([self.r+1, self.c + 2])
            chessboard[self.r+1][self.c+2].setOccupant(temp2)
            self.occ = temp
        if self.r + 2 < 8 and self.c - 1 >= 0 and chessboard[self.r + 2, self.c - 1].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[self.r + 2][self.c - 1].returnOccupant()
            chessboard[self.r + 2][self.c - 1].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([self.r+2, self.c - 1])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([self.r+2, self.c - 1])
            chessboard[self.r+2][self.c-1].setOccupant(temp2)
            self.occ = temp
        if self.r + 1 < 8 and self.c - 2 >= 0 and chessboard[self.r + 1, self.c -2].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[self.r + 1][self.c -2].returnOccupant()
            chessboard[self.r + 1][self.c -2].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([self.r+1, self.c -2])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([self.r+1, self.c -2])
            chessboard[self.r+1][self.c-2].setOccupant(temp2)
            self.occ = temp
        if self.r - 2 >=0 and self.c + 1 < 8 and chessboard[self.r - 2, self.c + 1].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[self.r -2][self.c + 1].returnOccupant()
            chessboard[self.r -2][self.c + 1].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([self.r-2, self.c + 1])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([self.r-2, self.c + 1])
            chessboard[self.r-2][self.c+1].setOccupant(temp2)
            self.occ = temp
        if self.r - 1 >=0 and self.c + 2 < 8 and chessboard[self.r -1, self.c + 2].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[self.r -1][self.c + 2].returnOccupant()
            chessboard[self.r -1][self.c + 2].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([self.r-1, self.c + 2])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([self.r-1, self.c + 2])
            chessboard[self.r-1][self.c+2].setOccupant(temp2)
            self.occ = temp
        if self.r - 2 >=0 and self.c - 1 >=0 and chessboard[self.r - 2, self.c - 1].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[self.r -2][self.c -1].returnOccupant()
            chessboard[self.r - 2][self.c - 1].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([self.r-2, self.c -1])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([self.r-2, self.c - 1])
            chessboard[self.r-2][self.c-1].setOccupant(temp2)
            self.occ = temp
        if self.r - 1 >=0 and self.c - 2 >=0 and chessboard[self.r -1, self.c -2].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[self.r - 1][self.c -2].returnOccupant()
            chessboard[self.r -1][self.c -2].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([self.r-1, self.c -2])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([self.r-1, self.c -2])
            chessboard[self.r-1][self.c-2].setOccupant(temp2)
            self.occ = temp
        return poss
    #returns all squares a knight can attack
    def KnightCanAttack(self):
        poss = []
        if self.r + 2 < 8 and self.c + 1 < 8:
            poss.append([self.r+2, self.c + 1])
        if self.r + 1 < 8 and self.c + 2 < 8:
            poss.append([self.r+1, self.c + 2])
        if self.r + 2 < 8 and self.c - 1 >= 0:
            poss.append([self.r+2, self.c - 1])
        if self.r + 1 < 8 and self.c - 2 >= 0:
            poss.append([self.r+1, self.c -2])
        if self.r - 2 >=0 and self.c + 1 < 8:
            poss.append([self.r-2, self.c + 1])
        if self.r - 1 >=0 and self.c + 2 < 8:
            poss.append([self.r-1, self.c + 2])
        if self.r - 2 >=0 and self.c - 1 >=0:
            poss.append([self.r-2, self.c - 1])
        if self.r - 1 >=0 and self.c - 2 >=0:
            poss.append([self.r-1, self.c -2])
        return poss
    #returns all squares a bishop can move to
    def BishopCanMove(self):
        poss = []
        possRow = self.r + 1
        possColumn = self.c + 1
        while possRow < 8 and possColumn < 8 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
            possColumn += 1
        possRow = self.r + 1
        possColumn = self.c - 1
        while possRow < 8 and possColumn >= 0 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
            possColumn -= 1
        possRow = self.r - 1
        possColumn = self.c - 1
        while possRow >= 0 and possColumn >= 0 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
            possColumn -= 1
        possRow = self.r - 1
        possColumn = self.c + 1
        while possRow >= 0 and possColumn < 8 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
            possColumn += 1
        return poss
    #returns all squares a bishop can attack
    def BishopCanAttack(self):
        poss = []
        possRow = self.r + 1
        possColumn = self.c + 1
        while possRow < 8 and possColumn < 8:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
            possColumn += 1
        possRow = self.r + 1
        possColumn = self.c - 1
        while possRow < 8 and possColumn >= 0:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
            possColumn -= 1
        possRow = self.r - 1
        possColumn = self.c - 1
        while possRow >= 0 and possColumn >= 0:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
            possColumn -= 1
        possRow = self.r - 1
        possColumn = self.c + 1
        while possRow >= 0 and possColumn < 8:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
            possColumn += 1
        return poss
    #returns all squares a rook can move to
    def RookCanMove(self):
        poss = []
        possRow = self.r + 1
        possColumn = self.c
        while possRow < 8 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
        possRow = self.r - 1
        possColumn = self.c
        while possRow >= 0 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
        possRow = self.r
        possColumn = self.c + 1
        while possColumn < 8 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possColumn += 1
        possRow = self.r
        possColumn = self.c - 1
        while possColumn >= 0 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possColumn -= 1
            
        return poss
    #returns all squares a rook can attack
    def RookCanAttack(self):
        poss = []
        possRow = self.r + 1
        possColumn = self.c
        while possRow < 8:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
        possRow = self.r - 1
        possColumn = self.c
        while possRow >= 0:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
        possRow = self.r
        possColumn = self.c + 1
        while possColumn < 8:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possColumn += 1
        possRow = self.r
        possColumn = self.c - 1
        while possColumn >= 0:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possColumn -= 1
            
        return poss
    #returns all squares a queen can move to
    def QueenCanMove(self):
        poss = []
        possRow = self.r + 1
        possColumn = self.c + 1
        while possRow < 8 and possColumn < 8 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
            possColumn += 1
        possRow = self.r + 1
        possColumn = self.c - 1
        while possRow < 8 and possColumn >= 0 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
            possColumn -= 1
        possRow = self.r - 1
        possColumn = self.c - 1
        while possRow >= 0 and possColumn >= 0 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
            possColumn -= 1
        possRow = self.r - 1
        possColumn = self.c + 1
        while possRow >= 0 and possColumn < 8 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
            possColumn += 1
        possRow = self.r + 1
        possColumn = self.c
        while possRow < 8 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
        possRow = self.r - 1
        possColumn = self.c
        while possRow >= 0 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
        possRow = self.r
        possColumn = self.c + 1
        while possColumn < 8 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possColumn += 1
        possRow = self.r
        possColumn = self.c - 1
        while possColumn >= 0 and chessboard[possRow][possColumn].returnOccupant() != self.occ:
            temp = self.occ
            temp2 = chessboard[possRow][possColumn].returnOccupant()
            chessboard[possRow][possColumn].setOccupant(temp)
            self.occ = 0
            if temp == 1 and not PPlayer.getKing().isInCheck():
                poss.append([possRow, possColumn])
            elif temp == 2 and not POpponent.getKing().isInCheck():
                poss.append([possRow, possColumn])
            chessboard[possRow][possColumn].setOccupant(temp2)
            self.occ = temp
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possColumn -= 1
            
        return poss
    #returns all squares a queen can attack
    def QueenCanAttack(self):
        poss = []
        possRow = self.r + 1
        possColumn = self.c
        while possRow < 8:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
        possRow = self.r - 1
        possColumn = self.c
        while possRow >= 0:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
        possRow = self.r
        possColumn = self.c + 1
        while possColumn < 8:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possColumn += 1
        possRow = self.r
        possColumn = self.c - 1
        while possColumn >= 0:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possColumn -= 1
        possRow = self.r + 1
        possColumn = self.c + 1
        while possRow < 8 and possColumn < 8:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
            possColumn += 1
        possRow = self.r + 1
        possColumn = self.c - 1
        while possRow < 8 and possColumn >= 0:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow += 1
            possColumn -= 1
        possRow = self.r - 1
        possColumn = self.c - 1
        while possRow >= 0 and possColumn >= 0:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
            possColumn -= 1
        possRow = self.r - 1
        possColumn = self.c + 1
        while possRow >= 0 and possColumn < 8:
            poss.append([possRow, possColumn])
            if chessboard[possRow][possColumn].returnOccupant() != 0:
                break
            possRow -= 1
            possColumn += 1
        return poss
    #returns all squares a pawn can move to
    def PawnCanMove(self):
        poss = []
        if self.occ == 2:
            possColumn = self.c
            possRow = self.r + 1
            if possRow < 8 and chessboard[possRow][possColumn].returnOccupant() == 0:
                temp = self.occ
                temp2 = chessboard[possRow][possColumn].returnOccupant()
                chessboard[possRow][possColumn].setOccupant(temp)
                self.occ = 0
                if temp == 1 and not PPlayer.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                elif temp == 2 and not POpponent.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                chessboard[possRow][possColumn].setOccupant(temp2)
                self.occ = temp
            possColumn = self.c -1
            possRow = self.r + 1
            if possRow < 8 and possColumn >= 0 and chessboard[possRow][possColumn].returnOccupant() == 1:
                temp = self.occ
                temp2 = chessboard[possRow][possColumn].returnOccupant()
                chessboard[possRow][possColumn].setOccupant(temp)
                self.occ = 0
                if temp == 1 and not PPlayer.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                elif temp == 2 and not POpponent.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                chessboard[possRow][possColumn].setOccupant(temp2)
                self.occ = temp
            possColumn = self.c +1
            possRow = self.r + 1
            if possRow <8 and possColumn < 8 and chessboard[possRow][possColumn].returnOccupant() == 1:
                temp = self.occ
                temp2 = chessboard[possRow][possColumn].returnOccupant()
                chessboard[possRow][possColumn].setOccupant(temp)
                self.occ = 0
                if temp == 1 and not PPlayer.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                elif temp == 2 and not POpponent.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                chessboard[possRow][possColumn].setOccupant(temp2)
                self.occ = temp
            possColumn = self.c
            possRow = self.r + 2
            if self.r == 1 and chessboard[possRow][possColumn].returnOccupant() == 0 and chessboard[possRow-1][possColumn].returnOccupant() == 0:
                temp = self.occ
                temp2 = chessboard[possRow][possColumn].returnOccupant()
                chessboard[possRow][possColumn].setOccupant(temp)
                self.occ = 0
                if temp == 1 and not PPlayer.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                elif temp == 2 and not POpponent.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                chessboard[possRow][possColumn].setOccupant(temp2)
                self.occ = temp
            for piece in PPlayer.getAllPieces():
                if type(piece) is Pawn:
                    if piece.movedTwo or piece.tempMovedTwo:
                        if self.r == 4 and abs(piece.getColumn() - self.c) == 1:
                            poss.append([5, piece.getColumn()])
            return poss
        if self.occ == 1:
            possColumn = self.c
            possRow = self.r - 1
            if possRow >= 0 and chessboard[possRow][possColumn].returnOccupant() == 0:
                temp = self.occ
                temp2 = chessboard[possRow][possColumn].returnOccupant()
                chessboard[possRow][possColumn].setOccupant(temp)
                self.occ = 0
                if temp == 1 and not PPlayer.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                elif temp == 2 and not POpponent.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                chessboard[possRow][possColumn].setOccupant(temp2)
                self.occ = temp
            possColumn = self.c -1
            possRow = self.r - 1
            if possRow >= 0 and possColumn >= 0 and chessboard[possRow][possColumn].returnOccupant() == 2:
                temp = self.occ
                temp2 = chessboard[possRow][possColumn].returnOccupant()
                chessboard[possRow][possColumn].setOccupant(temp)
                self.occ = 0
                if temp == 1 and not PPlayer.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                elif temp == 2 and not POpponent.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                chessboard[possRow][possColumn].setOccupant(temp2)
                self.occ = temp
            possColumn = self.c +1
            possRow = self.r - 1
            if possRow >= 0 and possColumn < 8 and chessboard[possRow][possColumn].returnOccupant() == 2:
                temp = self.occ
                temp2 = chessboard[possRow][possColumn].returnOccupant()
                chessboard[possRow][possColumn].setOccupant(temp)
                self.occ = 0
                if temp == 1 and not PPlayer.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                elif temp == 2 and not POpponent.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                chessboard[possRow][possColumn].setOccupant(temp2)
                self.occ = temp
            possColumn = self.c
            possRow = self.r - 2
            if self.r == 6 and chessboard[possRow][possColumn].returnOccupant() == 0 and chessboard[possRow+1][possColumn].returnOccupant() == 0:
                temp = self.occ
                temp2 = chessboard[possRow][possColumn].returnOccupant()
                chessboard[possRow][possColumn].setOccupant(temp)
                self.occ = 0
                if temp == 1 and not PPlayer.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                elif temp == 2 and not POpponent.getKing().isInCheck():
                    poss.append([possRow, possColumn])
                chessboard[possRow][possColumn].setOccupant(temp2)
                self.occ = temp
            for piece in POpponent.getAllPieces():
                if type(piece) is Pawn:
                    if piece.movedTwo or piece.tempMovedTwo:
                        if self.r == 3 and abs(piece.getColumn() - self.c) == 1:
                            poss.append([2, piece.getColumn()])
            return poss
        return poss
    #returns all squares a pawn can attack
    def PawnCanAttack(self):
        poss = []
        if self.occ == 2:
            possRow = self.r + 1
            possColumn = self.c +1
            if possRow < 8 and possColumn < 8:
                poss.append([possRow, possColumn])
            possRow = self.r + 1
            possColumn = self.c - 1
            if possRow < 8 and possColumn >= 0:
                poss.append([possRow, possColumn])
        if self.occ == 1:
            possRow = self.r - 1
            possColumn = self.c + 1
            if possRow >= 0 and possColumn < 8:
                poss.append([possRow, possColumn])
            possRow = self.r - 1
            possColumn = self.c - 1
            if possRow >= 0 and possColumn >= 0:
                poss.append([possRow, possColumn])
        return poss
            
    #returns all squares a king can move to
    def KingCanMove(self):
        poss = []
        if self.occ == 1:    
            if self.r + 1 < 8 and self.c + 1 < 8 and chessboard[self.r + 1, self.c + 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r+1][self.c+1].isAttackedByOpponent():
                    poss.append([self.r+1, self.c + 1])
                chessboard[self.r][self.c].setOccupant(1)
            if self.c + 1 < 8 and chessboard[self.r, self.c + 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r][self.c+1].isAttackedByOpponent():
                    poss.append([self.r, self.c + 1])
                chessboard[self.r][self.c].setOccupant(1)
            if self.r - 1 >= 0 and self.c + 1 < 8 and chessboard[self.r - 1, self.c + 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r-1][self.c+1].isAttackedByOpponent():
                    poss.append([self.r-1, self.c + 1])
                chessboard[self.r][self.c].setOccupant(1)
            if self.r -1 >= 0 and chessboard[self.r - 1, self.c].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r-1][self.c].isAttackedByOpponent():
                    poss.append([self.r-1, self.c])
                chessboard[self.r][self.c].setOccupant(1)
            if self.r -1 >=0 and self.c -1 >=0 and chessboard[self.r - 1, self.c - 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r-1][self.c-1].isAttackedByOpponent():
                    poss.append([self.r-1, self.c - 1])
                chessboard[self.r][self.c].setOccupant(1)
            if self.c -1 >= 0 and chessboard[self.r, self.c - 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r][self.c-1].isAttackedByOpponent():
                    poss.append([self.r, self.c - 1])
                chessboard[self.r][self.c].setOccupant(1)
            if self.r + 1 < 8 and self.c - 1 >= 0 and chessboard[self.r + 1, self.c - 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r+1][self.c-1].isAttackedByOpponent():
                    poss.append([self.r+1, self.c - 1])
                chessboard[self.r][self.c].setOccupant(1)
            if self.r + 1 < 8 and chessboard[self.r + 1, self.c].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r+1][self.c].isAttackedByOpponent():
                    poss.append([self.r+1, self.c])
                chessboard[self.r][self.c].setOccupant(1)
            if PPlayer.canCastleKingSide():
                if side == 0:
                    poss.append([7, 6])
                else:
                    poss.append([7, 1])
            if PPlayer.canCastleQueenSide():
                if side == 0:
                    poss.append([7, 2])
                else:
                    poss.append([7, 5])
        if self.occ == 2:
            if self.r + 1 < 8 and self.c + 1 < 8 and chessboard[self.r + 1, self.c + 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r+1][self.c+1].isAttackedByPlayer():
                    poss.append([self.r+1, self.c + 1])
                chessboard[self.r][self.c].setOccupant(2)
            if self.c + 1 < 8 and chessboard[self.r, self.c + 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r][self.c+1].isAttackedByPlayer():
                    poss.append([self.r, self.c + 1])
                chessboard[self.r][self.c].setOccupant(2)
            if self.r - 1 >= 0 and self.c + 1 < 8 and chessboard[self.r - 1, self.c + 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r-1][self.c+1].isAttackedByPlayer():
                    poss.append([self.r-1, self.c + 1])
                chessboard[self.r][self.c].setOccupant(2)
            if self.r -1 >= 0 and chessboard[self.r - 1, self.c].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r-1][self.c].isAttackedByPlayer():
                    poss.append([self.r-1, self.c])
                chessboard[self.r][self.c].setOccupant(2)
            if self.r -1 >=0 and self.c -1 >=0 and chessboard[self.r - 1, self.c - 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r-1][self.c-1].isAttackedByPlayer():
                    poss.append([self.r-1, self.c - 1])
                chessboard[self.r][self.c].setOccupant(2)
            if self.c -1 >= 0 and chessboard[self.r, self.c - 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r][self.c-1].isAttackedByPlayer():
                    poss.append([self.r, self.c - 1])
                chessboard[self.r][self.c].setOccupant(2)
            if self.r + 1 < 8 and self.c - 1 >= 0 and chessboard[self.r + 1, self.c - 1].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r+1][self.c-1].isAttackedByPlayer():
                    poss.append([self.r+1, self.c - 1])
                chessboard[self.r][self.c].setOccupant(2)
            if self.r + 1 < 8 and chessboard[self.r + 1, self.c].returnOccupant() != self.occ:
                chessboard[self.r][self.c].setOccupant(0)
                if not chessboard[self.r+1][self.c].isAttackedByPlayer():
                    poss.append([self.r+1, self.c])
                chessboard[self.r][self.c].setOccupant(2)
            if POpponent.canCastleKingSide():
                if side == 0:
                    poss.append([0, 6])
                else:
                    poss.append([0, 1])
            if POpponent.canCastleQueenSide():
                if side == 0:
                    poss.append([0, 2])
                else:
                    poss.append([0, 5])
        return poss
    #returns all squares a king can attack
    def KingCanAttack(self):
        poss = []
        if self.r + 1 < 8 and self.c + 1 < 8:
            poss.append([self.r+1, self.c + 1])
        if self.c + 1 < 8:
            poss.append([self.r, self.c + 1])
        if self.r -1 >= 0 and self.c + 1 < 8:
            poss.append([self.r-1, self.c + 1])
        if self.r - 1 >= 0:
            poss.append([self.r-1, self.c])
        if self.r - 1 >=0 and self.c - 1 >=0:
            poss.append([self.r-1, self.c - 1])
        if self.c -1 >=0:
            poss.append([self.r, self.c -1])
        if self.r +1 <8 and self.c - 1 >=0:
            poss.append([self.r+1, self.c - 1])
        if self.r + 1 < 8:
            poss.append([self.r+1, self.c])
        return poss
    #returns whether or not the square is attacked by one of the player's pieces
    def isAttackedByPlayer(self):
        for piece in PPlayer.getAllPieces():
            for possibility in piece.AllPossibilities():
                if possibility[0]== self.r and possibility[1] == self.c and chessboard[piece.getRow()][piece.getColumn()].returnOccupant() == 1:
                    return True
        return False
    #returns whether or not the square is attacked by one of the opponent's pieces
    def isAttackedByOpponent(self):
        for piece in POpponent.getAllPieces():
            for possibility in piece.AllPossibilities():
                if possibility[0]== self.r and possibility[1] == self.c and chessboard[piece.getRow()][piece.getColumn()].returnOccupant() == 2:
                    return True
        return False
    
    #prints the name of each square
    def __str__(self):
        if side == 0:
            last = str(8 - self.r)
            if self.c == 0:
                return "a" + last
            elif self.c == 1:
                return "b" + last
            elif self.c == 2:
                return "c" + last
            elif self.c == 3:
                return "d" + last
            elif self.c == 4:
                return "e" + last
            elif self.c == 5:
                return "f" + last
            elif self.c == 6:
                return "g" + last
            elif self.c == 7:
                return "h" + last
        else:
            last = str(self.r + 1)
            if self.c == 0:
                return "h" + last
            elif self.c == 1:
                return "g" + last
            elif self.c == 2:
                return "f" + last
            elif self.c == 3:
                return "e" + last
            elif self.c == 4:
                return "d" + last
            elif self.c == 5:
                return "c" + last
            elif self.c == 6:
                return "b" + last
            elif self.c == 7:
                return "a" + last
