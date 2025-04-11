# This is a test of pygame change later to reflect actual game
import pygame
import json
from x_object import XObject # Import the XObject from the file for use
from o_object import OObject # Import the OObject from the file for use
from state_machine import StateMachine # Import the StateMachine for use in the program, used to easily handle state changes
from game_state import GameState # Import the Enum for use in the program, used to update the currentt_state

# Initialize Pygame
pygame.init()

# Create varibles for screen size
max_width = 600
max_height = 600

# Set up display
screen = pygame.display.set_mode((max_width, max_height))
pygame.display.set_caption("Tic-Tac-Toe Pro") # This sets the caption above the window

# Create StateMachine Object for game states
current_state = StateMachine()

# Font set up - This is used to create an X character and O character on screen.
font = pygame.font.Font(None, 150) # This is saying we will use the default font because we do not have a font file. Change the size as needed.
obj_color = (255, 255, 255) # This is white, this holds the color of the X and O objects
obj_start_x = max_width // 2 # Hold the x starting position of the object
obj_start_y = (max_height // 2) + 230 # Hold the y starting position of the object

# Define color
BLACK = (0, 0, 0)
screen.fill(BLACK)
pygame.display.update() # This makes sure that the screen updates before moving on

# Create a board 3x3 matrix to store and track player moves
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Define Box properties
box_color = (255, 255, 255) # This is white
box_size = 400 # Box size
box_line_width = 5 # Line thickness
box_x = (max_width - box_size) // 2
box_y = ((max_height - box_size) // 2) - 50 # Added this 50 to off center the box up

# Define Grid properties
grid_color = (255, 255, 255) # This is white
grid_size = 3 # This is the size of the grid on screen
grid_line_width = 5 # Line thickness
cell_size = box_size // grid_size # How big each cell is in the grid inside the box

# Create a set to track occupied cells while the game runs
occupied_cells = set() # Stores vales of (x, y) of each object in a cell

# Create the X Objects
x_objects = [XObject(obj_start_x, obj_start_y, font, obj_color)] # Start the game with only one
current_x_index = 0 # This will be the starting index or turn of the game. Each time an X is placed succesfully it will go up

# Create the O Objects
o_objects = [] # Start with this blank for right now, this will have stuff added as the game goes on
current_o_index = 0 # This will be the starting index or turn of O in the game. Each time an O is placed succesfully it will go up

# Variable to hold the winning line data
winning_line_data = [] # It is an empty list

# Draw Box and Grid function
def draw_box_and_grid():
    # Set up the grid and box for tic-tac-toe
    # Draw the box
    pygame.draw.rect(screen, box_color, (box_x, box_y, box_size, box_size), box_line_width)
    # Draw the vertical grid lines
    for i in range(1, grid_size):
        x = box_x + i * cell_size
        pygame.draw.line(screen, grid_color, (x, box_y), (x, box_y + box_size), grid_line_width)
    # Draw the horizontal grid lines
    for i in range(1, grid_size):
        y = box_y + i * cell_size
        pygame.draw.line(screen, grid_color, (box_x, y), (box_x + box_size, y), grid_line_width)

# Draw the winning line when the player wins
def draw_winning_line(winner, line_type, index):
    # Set the line_color
    line_color = (255, 0, 0) # This is red, default to this for X

    # Check to see if the winner is O to make the line blue
    if winner == "O":
        line_color = (0, 0, 255) # This is blue

    # Set the line thickness
    line_thickness = 10

    # If the line is a row win
    if line_type == "row":
        # Figure inside the box where the line must go
        y = box_y + index * cell_size + cell_size // 2
        # Draw the line on that y spot
        pygame.draw.line(screen, line_color, (box_x, y), (box_x + box_size, y), line_thickness)
    # If the line is a col win
    elif line_type == "col":
        # Figure inside the box where the line will go
        x = box_x + index * cell_size + cell_size // 2
        # Draw the line on that x spot
        pygame.draw.line(screen, line_color, (x, box_y), (x, box_y + box_size), line_thickness)
    # If the line is a diagonal win
    elif line_type == "diag":
        if index == 0: # This means that the line needs to go left-to-right
            pygame.draw.line(screen, line_color, (box_x, box_y), (box_x + box_size, box_y + box_size), line_thickness)
        else: # This means that the line needs to go right-to-left
            pygame.draw.line(screen, line_color, (box_x + box_size, box_y), (box_x, box_y + box_size), line_thickness)

# This function is run when a player makes a move
def update_board(cell, player):
    # Get the row and column of the cell
    (col, row) = cell
    # Check to see if the spot we are adding to is none
    if board[row][col] is None:
        board[row][col] = player # Add the X or the O to the board

# This function checks for a winner of the game
def check_winner():
    # Create a variable to hold the row index for the draw line function
    row_index = 0
    # Check the rows of the board
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            # There is a winner so set the game state to a win
            current_state.change_state(GameState.GAME_WIN)
            # Draw the winning line
            winning_line_data.append(row[0])
            winning_line_data.append("row")
            winning_line_data.append(row_index)
        # If this row does not have the winner add one to the row_index
        row_index += 1
    # Check the colums of the board
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            # There is a winner here as well so set the game state to a win
            current_state.change_state(GameState.GAME_WIN)
            # Draw the winning line
            winning_line_data.append(board[0][col])
            winning_line_data.append("col")
            winning_line_data.append(col)
    # Check the diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        # There is a winner here, set the game state to a win
        current_state.change_state(GameState.GAME_WIN)
        # Draw the winning line
        winning_line_data.append(board[0][0])
        winning_line_data.append("diag")
        winning_line_data.append(0) # This does diagonal left-to-right
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        # There is another winner here, set the game state to a win
        current_state.change_state(GameState.GAME_WIN)
        # Draw the winning line
        winning_line_data.append(board[0][2])
        winning_line_data.append("diag")
        winning_line_data.append(1) # This does diagonal right-to-left
    # Note: If there is not a winner yet, do nothing because we have the game state
    # taking care of if a winner appears

# This function saves the data to the json file
def save_data():
    # Create data structure to go into the json file
    data = {
        "gameState": current_state.state.value,
        "xIndex": current_x_index,
        "oIndex": current_o_index,
        "xObjects": [obj.to_dict() for obj in x_objects],
        "oObjects": [obj.to_dict() for obj in o_objects],
        "occupiedCells": list(occupied_cells),
        "winningLineData": winning_line_data,
        "board": board
    }

    # Write to the json file
    with open("save_data.json", "w") as file:
        json.dump(data, file, indent=4) # Indent allows it to be readable

# This function loads in the save data for a continued game
def load_data():
    # Set up a try catch block to handle if data is not there
    try:
        with open("save_data.json", "r") as file:
            # Load in the data
            data = json.load(file)
            # Make all the variables global
            global current_state
            global current_x_index
            global current_o_index
            global x_objects
            global o_objects
            global occupied_cells
            global winning_line_data
            global board
            # Extract the game properties
            current_state.change_state(GameState(data["gameState"]))
            current_x_index = data.get("xIndex")
            current_o_index = data.get("oIndex")
            x_objects = [XObject.from_dict(XObject, obj_data, font, obj_color) for obj_data in data.get("xObjects", [])]
            o_objects = [OObject.from_dict(OObject, obj_data, font, obj_color) for obj_data in data.get("oObjects", [])]
            occupied_cells = set(map(tuple, data.get("occupiedCells", [])))
            winning_line_data = data.get("winningLineData")
            board = data.get("board")
    
    except FileNotFoundError:
        print("No save data found") # This keeps the program from blowing up


# Keep the window open until closed
running = True
while running:
    screen.fill(BLACK) # Clear the screen while running so you don't create graphic bugs

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # This allows the game to exit when the player quits
            running = False
        
        # Check to see if the state of the game is X's turn
        if current_state.state == GameState.X_TURN:
            # Check to see if there are moves still
            if current_x_index < len(x_objects):
                # Get our x object by index
                x_obj = x_objects[current_x_index]

                # Handle the events of the X Object
                x_obj.handle_event(event, box_x, box_y, box_size, cell_size)

                # Check to see if that space is occupied before placing an X or O
                if event.type == pygame.MOUSEBUTTONUP and x_obj.dragging == False:
                    grid_x = (x_obj.rect.centerx - box_x) // cell_size
                    grid_y = (x_obj.rect.centery - box_y) // cell_size

                    # Make sure this is inside the bounds
                    if 0 <= grid_x < grid_size and 0 <= grid_y < grid_size:
                        if (grid_x, grid_y) not in occupied_cells: # Only snap if it is ok to go in here
                            x_obj.rect.center = (box_x + grid_x * cell_size + cell_size // 2,
                                                box_y + grid_y * cell_size + cell_size // 2 + 10)
                            occupied_cells.add((grid_x, grid_y)) # These points to the set
                            # Add the cell to the board and who occupies it
                            update_board((grid_x, grid_y), "X")
                            # Also add 1 to the current index because this one was solved
                            current_x_index = current_x_index + 1
                            # Check a winner after every playable turn
                            check_winner()
                            # Add a new X to the list
                            if current_x_index < 5 and current_state.state != GameState.GAME_WIN: # Create a new O object if the X's can still make more
                                o_objects.append(OObject(obj_start_x, obj_start_y, font, obj_color))
                                # Set the current_state to O's turn
                                current_state.change_state(GameState.O_TURN)
                            # Create a way to end the game in a draw if the game has not been won, and X's turns equal 5
                            elif current_x_index == 5 and current_state.state != GameState.GAME_WIN:
                                # Set the game to a draw
                                current_state.change_state(GameState.GAME_OVER)

                        else: # This does not snap and goes back to the starting position
                            x_obj.rect.center = (obj_start_x, obj_start_y)
                            # Make sure locked_in does not trigger so you can place it again
                            x_obj.locked_in = False

        # Check to see if the state of the game is O's turn
        if current_state.state == GameState.O_TURN:
            # Check to see if there are moves still
            if current_o_index < len(o_objects):
                # Get our x object by index
                o_obj = o_objects[current_o_index]

                # Handle the events of the X Object
                o_obj.handle_event(event, box_x, box_y, box_size, cell_size)

                # Check to see if that space is occupied before placing an X or O
                if event.type == pygame.MOUSEBUTTONUP and o_obj.dragging == False:
                    grid_x = (o_obj.rect.centerx - box_x) // cell_size
                    grid_y = (o_obj.rect.centery - box_y) // cell_size

                    # Make sure this is inside the bounds
                    if 0 <= grid_x < grid_size and 0 <= grid_y < grid_size:
                        if (grid_x, grid_y) not in occupied_cells: # Only snap if it is ok to go in here
                            o_obj.rect.center = (box_x + grid_x * cell_size + cell_size // 2,
                                                box_y + grid_y * cell_size + cell_size // 2 + 10)
                            occupied_cells.add((grid_x, grid_y)) # These points to the set
                            # Add the cell to the board and who occupies it
                            update_board((grid_x, grid_y), "O")
                            # Also add 1 to the current index because this O was placed
                            current_o_index = current_o_index + 1
                            # Check a winner after every playable turn
                            check_winner()
                            # Add a new X to the list
                            if current_o_index <= 4 and current_state.state != GameState.GAME_WIN: # Create a new X object if the O's can still make more
                                x_objects.append(XObject(obj_start_x, obj_start_y, font, obj_color))
                                # Set the current_state to X's turn
                                current_state.change_state(GameState.X_TURN)

                        else: # This does not snap and goes back to the starting position
                            o_obj.rect.center = (obj_start_x, obj_start_y)
                            # Make sure locked_in does not trigger so you can place it again
                            o_obj.locked_in = False
    
        # Handle key presses the player can do
        if event.type == pygame.KEYDOWN:
            # Space resets the game
            if event.key == pygame.K_SPACE:
                # Do this by clearing out the object lists
                x_objects.clear()
                o_objects.clear()
                # Now clear the occupied cells set
                occupied_cells.clear()
                # Now clear the board as well and reset it
                board.clear()
                board = [[None, None, None],
                         [None, None, None],
                         [None, None, None]]
                # Also clear the winning line
                winning_line_data.clear()
                # Then reset the current_indexes
                current_x_index = 0
                current_o_index = 0
                # Now create a new x for the x_object
                x_objects.append(XObject(obj_start_x, obj_start_y, font, obj_color))
                # Now set the game state to X's turn
                current_state.change_state(GameState.X_TURN)
            # 'S' saves the game
            elif event.key == pygame.K_s:
                # Call the save function
                save_data()
            # 'L' loads the game
            elif event.key == pygame.K_l:
                # Call the load function
                load_data()

    # Display the x's on screen
    for x_obj in x_objects:
        x_obj.draw(screen)

    # Display the o's on screen
    for o_obj in o_objects:
        o_obj.draw(screen)

    # Display the box and grid
    draw_box_and_grid()

    # Draw the winner line if the game has been won
    if current_state.state == GameState.GAME_WIN:
        # Split up the data into variables
        winner = winning_line_data[0]
        line_type = winning_line_data[1]
        index = winning_line_data[2]

        # Now send them to draw the line
        draw_winning_line(winner, line_type, index)

    # Update the display to view the new grid
    pygame.display.update()

pygame.quit()