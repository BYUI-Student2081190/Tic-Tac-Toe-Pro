# Imports
from enum import Enum # Use the enum to set up a state machine for the game

# Create the Enum to be used in the program
class GameState(Enum):
    X_TURN = 0 # This is active on X's turn
    O_TURN = 1 # This is active on O's turn
    GAME_OVER = 2 # This triggers when the game is over
    GAME_WIN = 3 # This triggers when the game is won