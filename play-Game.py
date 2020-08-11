pygame.init()
screen_width = 600
screen_height = 650
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chess Game")


onePlayerButton = screenButton((255, 100, 180), 175, 225, 250, 100, "1 Player")
twoPlayerButton = screenButton((255, 100, 180), 175, 425, 250, 100, "2 Player")
side = 0
choosePlayer = True
while choosePlayer:
    redrawPlayerWindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            choosePlayer = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if onePlayerButton.isOver(pos):
                print("You chose 1 player mode!")
                onePlayer = True
                choosePlayer = False
            if twoPlayerButton.isOver(pos):
                print("You chose 2 player mode!")
                onePlayer = False
                choosePlayer = False

buttonWhite = screenButton((255, 100, 180), 20, 300, 200, 100, "White")
buttonBlack = screenButton((255, 100, 180), 350, 300, 200, 100, "Black")
begin = True
while begin:
    redrawBeginningWindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            begin = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonWhite.isOver(pos):
                begin = False
                print("You chose the white pieces!")
                side = 0
            if buttonBlack.isOver(pos):
                begin = False
                print("You chose the black pieces!")
                side = 1
        

run = True

PPlayer = HumanPlayer()
POpponent = Opponent()
playBackground()
a = 1
moves = 0
if side == 0:
    playerTurn = True
    opponentTurn = False
else:
    playerTurn = False
    opponentTurn = True
while run:
    if playerTurn:
        redrawWindow()
        if PPlayer.canMove() == 1:
            if PPlayer.getKing().isInCheck():
                font = pygame.font.SysFont('comicsans', 60, True)
                check = font.render("Check", 1, (0, 0, 0))
                win.blit(check, (225, 600))
                pygame.display.update()
            playerMoves()
            if PPlayer.canPromote():
                PPlayer.promote(promotePiece())
        elif PPlayer.canMove() == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            font = pygame.font.SysFont('comicsans', 60, True)
            stalemate = font.render("Stalemate! It's a draw!", 1, (0, 0, 0))
            win.blit(stalemate, (10, 600))
            if a == 1:
                print("Stalemate! It's a draw!")
                a = 2
            pygame.display.update()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            font = pygame.font.SysFont('comicsans', 60, True)
            if side == 0:
                checkmate = font.render("Checkmate! Black won!", 1, (0, 0, 0))
            else:
                checkmate = font.render("Checkmate! White won!", 1, (0, 0, 0))
            win.blit(checkmate, (10, 600))
            if a == 1:
                if side == 0:
                    print("Checkmate! Black won")
                else:
                    print("Checkmate! White won")
                a = 2
            pygame.display.update()

    elif opponentTurn:
        redrawWindow()
        if POpponent.canMove() == 1:
            if POpponent.getKing().isInCheck():
                font = pygame.font.SysFont('comicsans', 60, True)
                check = font.render("Check", 1, (0, 0, 0))
                win.blit(check, (225, 600))
                pygame.display.update()
            opponentMoves()
            if POpponent.canPromote() and not onePlayer:
                POpponent.promote(promotePiece())
        elif POpponent.canMove() == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            font = pygame.font.SysFont('comicsans', 60, True)
            stalemate = font.render("Stalemate! It's a draw!", 1, (0, 0, 0))
            win.blit(stalemate, (10, 600))
            if a == 1:
                print("Stalemate! It's a draw!")
                a = 2
            pygame.display.update()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            font = pygame.font.SysFont('comicsans', 60, True)
            if side == 0:
                checkmate = font.render("Checkmate! White won!", 1, (0, 0, 0))
            else:
                checkmate = font.render("Checkmate! Black won!", 1, (0, 0, 0))
            win.blit(checkmate, (10, 600))
            if a == 1:
                if side == 0:
                    print("Checkmate! White won!")
                    
                else:
                    print("Checkmate! Black won!")
                a = 2
            pygame.display.update()


    pygame.display.update()



pygame.quit()
