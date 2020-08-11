class screenButton:
    def __init__(self, color, x, y, width, height, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.SysFont("comicsans", 30)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False



class Button:
    def __init__(self, color, row, col, x, y, width, height):
        self.color = color
        self.originalColor = color
        self.x = x
        self.y = y
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.state = 0
    def setColor(self, newColor):
        self.color = newColor
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.height:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


class Board:
    def __init__(self):
        global win
        global chessboard
        global PPlayer
        global POpponent
        global side
        self.state = 0
        self.board = []
        x = 20
        y = 20
        width = 70
        height = 70
        row = 0
        col = 0
        for i in range(0, 4):
            thisRow = []
            for k in range(0, 4):
                thisRow.append(Button((255, 255, 255), row, col, x, y, width, height))
                col += 1
                x += width
                thisRow.append(Button((100, 40, 0), row, col, x, y, width, height))
                col += 1
                x += width
            x = 20
            y += height
            col = 0
            row += 1
            self.board.append(thisRow)
            thisRow = []
            for r in range(0, 4):
                thisRow.append(Button((100, 40, 0), row, col, x, y, width, height))
                col += 1
                x += width
                thisRow.append(Button((255, 255, 255), row, col, x, y, width, height))
                col += 1
                x += width
            x = 20
            y += height
            col = 0
            row += 1
            self.board.append(thisRow)
    def getSquare(self, row, column):
        return self.board[row][column]
    def drawPiece(self, win, r, c, locx, locy):
        if side == 0:
            if chessboard[r][c].returnOccupant() == 1:
                for piece in PPlayer.getAllPieces():
                    if piece.getRow() == r and piece.getColumn() == c:
                        if type(piece) is Pawn:
                            win.blit(pygame.image.load("WPawn.png"), (locx + 7, locy + 10))
                        if type(piece) is Bishop:
                            win.blit(pygame.image.load("WBishop.png"), (locx +5, locy + 5))
                        if type(piece) is playerKing:
                            win.blit(pygame.image.load("WKing.png"), (locx +5, locy+10))
                        if type(piece) is Rook:
                            win.blit(pygame.image.load("WRook.png"), (locx, locy+5))
                        if type(piece) is Knight:
                            win.blit(pygame.image.load("WKnight.png"), (locx, locy))
                        if type(piece) is Queen:
                            win.blit(pygame.image.load("WQueen.png"), (locx, locy))
                        break
            if chessboard[r][c].returnOccupant() == 2:
                for piece in POpponent.getAllPieces():
                    if piece.getRow() == r and piece.getColumn() == c:
                        if type(piece) is Pawn:
                            win.blit(pygame.image.load("BPawn.png"), (locx + 7, locy + 10))
                        if type(piece) is Bishop:
                            win.blit(pygame.image.load("BBishop.png"), (locx+1, locy + 3))
                        if type(piece) is opponentKing:
                            win.blit(pygame.image.load("BKing.png"), (locx+3, locy + 10))
                        if type(piece) is Rook:
                            win.blit(pygame.image.load("BRook.png"), (locx, locy+5))
                        if type(piece) is Knight:
                            win.blit(pygame.image.load("BKnight.png"), (locx + 6, locy+3))
                        if type(piece) is Queen:
                            win.blit(pygame.image.load("BQueen.png"), (locx, locy))
                        break
        else:
            if chessboard[r][c].returnOccupant() == 1:
                for piece in PPlayer.getAllPieces():
                    if piece.getRow() == r and piece.getColumn() == c:
                        if type(piece) is Pawn:
                            win.blit(pygame.image.load("BPawn.png"), (locx + 7, locy + 10))
                        if type(piece) is Bishop:
                            win.blit(pygame.image.load("BBishop.png"), (locx+1, locy + 3))
                        if type(piece) is playerKing:
                            win.blit(pygame.image.load("BKing.png"), (locx+3, locy + 10))
                        if type(piece) is Rook:
                            win.blit(pygame.image.load("BRook.png"), (locx, locy+5))
                        if type(piece) is Knight:
                            win.blit(pygame.image.load("BKnight.png"), (locx + 6, locy+3))
                        if type(piece) is Queen:
                            win.blit(pygame.image.load("BQueen.png"), (locx, locy))
                        break
            if chessboard[r][c].returnOccupant() == 2:
                for piece in POpponent.getAllPieces():
                    if piece.getRow() == r and piece.getColumn() == c:
                        if type(piece) is Pawn:
                            win.blit(pygame.image.load("WPawn.png"), (locx + 7, locy + 10))
                        if type(piece) is Bishop:
                            win.blit(pygame.image.load("WBishop.png"), (locx +5, locy + 5))
                        if type(piece) is opponentKing:
                            win.blit(pygame.image.load("WKing.png"), (locx +5, locy+10))
                        if type(piece) is Rook:
                            win.blit(pygame.image.load("WRook.png"), (locx, locy+5))
                        if type(piece) is Knight:
                            win.blit(pygame.image.load("WKnight.png"), (locx, locy))
                        if type(piece) is Queen:
                            win.blit(pygame.image.load("WQueen.png"), (locx, locy))
                        break
        return
    def draw(self):
        if PPlayer.getKing().isInCheck():
            board.board[PPlayer.getKing().getRow()][PPlayer.getKing().getColumn()].setColor((255, 0, 0))
        if POpponent.getKing().isInCheck():
            board.board[POpponent.getKing().getRow()][POpponent.getKing().getColumn()].setColor((255, 0, 0))
        for i in range(0, len(self.board)):
            for k in range(0, len(self.board[i])):
                self.board[i][k].draw(win)
                self.drawPiece(win, i, k, self.board[i][k].getX(), self.board[i][k].getY())
    def clear(self):
        for i in range(0, len(self.board)):
            for k in range(0, len(self.board[i])):
                if self.board[i][k].state == 1 or self.board[i][k].state == 2:
                    self.board[i][k].setColor(self.board[i][k].originalColor)
                    self.board[i][k].state = 0
    def completelyClear(self):
        for i in range(0, len(self.board)):
            for k in range(0, len(self.board[i])):
                self.board[i][k].setColor(self.board[i][k].originalColor)
                self.board[i][k].state = 0


    
board = Board()
def playBackground():
    background = ["Background1.wav",
                  "Background2.wav",
                  "Background3.wav",
                  "Background4.wav"]
    infiles = []
    for i in range(0, 10):
        num = int(random.random()*len(background))
        infiles.append(background[num])
    outfile = "Background.wav"
    data= []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()
    pygame.mixer.music.load("Background.wav")
    pygame.mixer.music.play(-1)
def playSound():
    songs = [pygame.mixer.Sound('Fail.wav'), 
             pygame.mixer.Sound('FBI.wav'), 
             pygame.mixer.Sound('Fine.wav'), 
             pygame.mixer.Sound('GTA.wav'), 
             pygame.mixer.Sound('Meme.wav'), 
             pygame.mixer.Sound('Nani.wav'), 
             pygame.mixer.Sound('SadViolin.wav'), 
             pygame.mixer.Sound('What.wav'), 
             pygame.mixer.Sound('Bruh.wav'),
             pygame.mixer.Sound('Distortion.wav'),
             pygame.mixer.Sound('JohnCena.wav'),
             pygame.mixer.Sound('Omg.wav'),
             pygame.mixer.Sound('SnoopDog.wav'),
             pygame.mixer.Sound('Thud.wav'),
             pygame.mixer.Sound('Wow.wav'),
             pygame.mixer.Sound('YouWhat.wav'),
             pygame.mixer.Sound('Illuminati.wav'),
             pygame.mixer.Sound('Nuts.wav'),
             pygame.mixer.Sound('ShotsFired.wav'),
             pygame.mixer.Sound('Sparta.wav'),
             pygame.mixer.Sound('Triple.wav'),
             pygame.mixer.Sound('Airhorn.wav'),
             pygame.mixer.Sound('Look.wav'),
             pygame.mixer.Sound('RickRoll.wav'),
             pygame.mixer.Sound('Sax.wav'),
             pygame.mixer.Sound('Whoa.wav'),
             pygame.mixer.Sound('TacticalNuke.wav')]
    num = int(random.random()*len(songs))
    songs[num].play()

def playerMoves():
    global board
    global chessboard
    global PPlayer
    global run
    global playerTurn
    global opponentTurn
    global side
    global moves

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i in range(0, len(board.board)):
                for k in range(0, len(board.board[i])):
                    if board.board[i][k].isOver(pos):                  
                        if board.state == 1:
                            if board.board[i][k].state == 2:
                                for r in range(0, len(board.board)):
                                    for c in range(0, len(board.board[i])):
                                        if board.board[r][c].state == 1:
                                            if side == 0:
                                                moves += 1
                                                print(str(moves)+ ".")
                                            PPlayer.makesMove(r,c,i,k)
                                            board.state = 0
                                            board.completelyClear()
                                            playSound()
                                            playerTurn = False
                                            opponentTurn = True
                            elif chessboard[i][k].returnOccupant() == 1:
                                board.clear()
                                for piece in PPlayer.getAllPieces():
                                    if piece.getRow() == i and piece.getColumn() == k:
                                        board.board[i][k].state = 1
                                        board.board[i][k].setColor((255, 255, 0))
                                        for possibility in piece.getPossibilities():
                                            board.board[possibility[0]][possibility[1]].setColor((0, 0, 255))
                                            board.board[possibility[0]][possibility[1]].state = 2
                                            board.state = 1
                                        break
                            else:
                                board.clear()
                                board.state = 0
                        elif board.state == 0:
                            board.clear()
                            if chessboard[i][k].returnOccupant() == 1:
                                for piece in PPlayer.getAllPieces():
                                    if piece.getRow() == i and piece.getColumn() == k:
                                        board.board[i][k].state = 1
                                        board.board[i][k].setColor((255, 255, 0))
                                        for possibility in piece.getPossibilities():
                                            board.board[possibility[0]][possibility[1]].setColor((0, 0, 255))
                                            board.board[possibility[0]][possibility[1]].state = 2
                                            board.state = 1
                                        break
def opponentMoves():
    global board
    global chessboard
    global PPlayer
    global run
    global playerTurn
    global opponentTurn
    global side
    global moves
    if onePlayer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        board.completelyClear()
        if side != 0:
            moves += 1
            print(str(moves)+ ".")
        POpponent.makesMove()
        playerTurn = True
        opponentTurn = False
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for i in range(0, len(board.board)):
                    for k in range(0, len(board.board[i])):
                        if board.board[i][k].isOver(pos):                  
                            if board.state == 1:
                                if board.board[i][k].state == 2:
                                    for r in range(0, len(board.board)):
                                        for c in range(0, len(board.board[i])):
                                            if board.board[r][c].state == 1:
                                                if side != 0:
                                                    moves += 1
                                                    print(str(moves)+ ".")
                                                POpponent.makesMove(r,c,i,k)
                                                board.state = 0
                                                board.completelyClear()
                                                playSound()
                                                playerTurn = True
                                                opponentTurn = False
                                elif chessboard[i][k].returnOccupant() == 2:
                                    board.clear()
                                    for piece in POpponent.getAllPieces():
                                        if piece.getRow() == i and piece.getColumn() == k:
                                            board.board[i][k].state = 1
                                            board.board[i][k].setColor((255, 255, 0))
                                            for possibility in piece.getPossibilities():
                                                board.board[possibility[0]][possibility[1]].setColor((0, 0, 255))
                                                board.board[possibility[0]][possibility[1]].state = 2
                                                board.state = 1
                                            break
                                else:
                                    board.clear()
                                    board.state = 0
                            elif board.state == 0:
                                board.clear()
                                if chessboard[i][k].returnOccupant() == 2:
                                    for piece in POpponent.getAllPieces():
                                        if piece.getRow() == i and piece.getColumn() == k:
                                            board.board[i][k].state = 1
                                            board.board[i][k].setColor((255, 255, 0))
                                            for possibility in piece.getPossibilities():
                                                board.board[possibility[0]][possibility[1]].setColor((0, 0, 255))
                                                board.board[possibility[0]][possibility[1]].state = 2
                                                board.state = 1
                                            break
def promotePiece():
    global PPlayer
    global POpponent
    global win
    global board
    global pos
    global run
    board.state = 10
    font = pygame.font.SysFont('comicsans', 30, True)
    text = font.render("Click piece to promote to:", 1, (0, 0, 0))
    queenButton = screenButton((255, 255, 255), 20, 620, 100, 25, "Queen")
    bishopButton = screenButton((255, 255, 255), 140, 620, 100, 25, "Bishop")
    knightButton = screenButton((255, 255, 255),260, 620, 100, 25, "Knight")
    rookButton = screenButton((255, 255, 255), 380, 620, 100, 25, "Rook")
    a = 0
    press= True
    while press:
        win.fill((0, 160, 0))
        board.draw()
        queenButton.draw(win)
        bishopButton.draw(win)
        knightButton.draw(win)
        rookButton.draw(win)
        win.blit(text, (120, 590))
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                press = False
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if queenButton.isOver(pos):
                    press = False
                    a = 1
                elif knightButton.isOver(pos):
                    press = False
                    a= 2
                elif bishopButton.isOver(pos):
                    press = False
                    a = 3
                elif rookButton.isOver(pos):
                    press = False
                    a = 4
        pygame.display.update()
    board.state = 0
    return a

def redrawWindow():
    global win
    global board
    win.fill((0, 160, 0))
    board.draw()
    pygame.display.update()
def redrawBeginningWindow():
    global onePlayer
    win.fill((64, 224, 208))
    if onePlayer:
        font = pygame.font.SysFont('comicsans', 40, True)
        firstLine = font.render("Choose which color piece you want:", 1, (0, 0, 0))
    else:
        font = pygame.font.SysFont('comicsans', 35, True)
        firstLine = font.render("Choose which color piece faces upward:", 1, (0, 0, 0))
    win.blit(firstLine, (20, 100))
    buttonWhite.draw(win)
    buttonBlack.draw(win)
def redrawPlayerWindow():
    win.fill((64, 224, 208))
    onePlayerButton.draw(win)
    twoPlayerButton.draw(win)
