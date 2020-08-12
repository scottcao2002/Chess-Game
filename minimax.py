#minimax algorithm used for the AI
def minimax(depth, alpha, beta, isComputer):
    global PPlayer
    global POpponent
    global chessboard
    global tempOpponentTurn
    global tempPlayerTurn
    if depth == 0 or abs(POpponent.getScore()) == maxsize or POpponent.canMove() == 0 or PPlayer.canMove() == 0:
        return POpponent.getScore()
    if isComputer:
        for piece in POpponent.getAllPieces():
            if type(piece) is Pawn:
                piece.tempMovedTwo = False
        bestScore = -maxsize - 1
        for piece in POpponent.getAllPieces():
            if chessboard[piece.getRow()][piece.getColumn()].piece == piece.ID:
                if len(piece.getPossibilities()) > 0:
                    for possibility in piece.getPossibilities():
                        piece.tempMove(possibility[0], possibility[1])
                        tempPlayerTurn = True
                        tempOpponentTurn = False
                        score = minimax(depth-1, alpha, beta, False)
                        piece.moveBack()
                        tempPlayerTurn = False
                        tempOpponentTurn = True
                        bestScore = max(score, bestScore)
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
                    
        return bestScore
    else:
        for piece in PPlayer.getAllPieces():
            if type(piece) is Pawn:
                piece.tempMovedTwo = False
        bestScore = maxsize + 1
        for piece in PPlayer.getAllPieces():
            if chessboard[piece.getRow()][piece.getColumn()].piece == piece.ID:
                if len(piece.getPossibilities()) > 0:
                    for possibility in piece.getPossibilities():
                        piece.tempMove(possibility[0], possibility[1])
                        score = minimax(depth - 1, alpha, beta, True)
                        piece.moveBack()
                        bestScore = min(score, bestScore)
                        beta = min(score, beta)
                        if beta <= alpha:
                            break
        return bestScore
                
