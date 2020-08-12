# Chess Game
Chess is a two player game played between a player with the black pieces and the player with the white pieces. The objective of the game is to capture the opposing side's king (called checkmate).
The game is played on an 8x8 square, with each side having 16 pieces. The game ends decisively if someone's king is attacked and cannot escape. The game may also end in stalemate.


# How to run the project
All of the files must be run in order for the game to work (with the exception of the opponent class. You may choose whether you want the opponent AI to play the King's Indian Defense or no premade opening). This chess game uses the pygame library. The music and picture files must be in the same folder as the files containing the code.

The following files should be run:

initialization.py

square.py

chessboard.py

pieces.py

minimax.py

player.py

opponent-King's-Indian-Opening.py OR opponent-No-Openings.py

game-screen.py

play-Game.py


# Playing the game
This game includes classical background music, along with meme sounds on every move (just to keep things entertaining). It opens with a choice of 1 or 2 player. The next screen
asks if you want the white or black pieces. For the one player game, the AI uses a minimax algorithm, with a default depth of 2. The algorithm includes alpha-beta pruning. Clicking
on any of your pieces on your turn will highlight the piece, and the spaces where that piece can move is also highlighted in blue. In 1 player mode, the opponent's previous move is
highlighted in purple. If a king is in check, it is highlighted in red. Each move (with the move number) is printed as the output in case you want to go back and check your previous
moves and/or mistakes.



# Background music
Unfortunately, the Background1 and Background4 files were too big to include on Github. However, if you wanted to add your own music, you just have to add their names to the array
titled "background" under the function playBackground(). To eliminate the sounds, you can delete the playSound() function executed in the functions playerMoves() and opponentMoves() of the file game-Screen.py and you can delete the playBackground() function that is created in the file game-Screen.py and executed in the file play-Game.py
