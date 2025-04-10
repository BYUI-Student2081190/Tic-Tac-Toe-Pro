# Imports
from game_state import GameState

# Create the class
class StateMachine:
    def __init__(self):
        # Create the object and set self to X_TURN at the start of the game
        self.state = GameState.X_TURN

    def change_state(self, new_state): # Change the current state of the game
        # Check to see if the new_state is part of the Enum
        if isinstance(new_state, GameState):
            self.state = new_state # Change the state to the desired state