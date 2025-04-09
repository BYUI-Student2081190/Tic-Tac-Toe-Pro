# This is a test of pygame change later to reflect actual game
import pygame
from x_object import XObject # Import the XObject from the file for use

# Initialize Pygame
pygame.init()

# Create varibles for screen size
max_width = 600
max_height = 600

# Set up display
screen = pygame.display.set_mode((max_width, max_height))
pygame.display.set_caption("Tic-Tac-Toe Pro") # This sets the caption above the window

# Font set up - This is used to create an X character and O character on screen.
font = pygame.font.Font(None, 150) # This is saying we will use the default font because we do not have a font file. Change the size as needed.
obj_color = (255, 255, 255) # This is white, this holds the color of the X and O objects
obj_start_x = max_width // 2 # Hold the x starting position of the object
obj_start_y = (max_height // 2) + 230 # Hold the y starting position of the object

# Define color
BLACK = (0, 0, 0)
screen.fill(BLACK)
pygame.display.update() # This makes sure that the screen updates before moving on

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
x_objects = [XObject(obj_start_x, obj_start_y, font, obj_color)] # Start with only two for now
current_x_index = 0 # This will be the starting index or turn of the game. Each time an X is placed succesfully it will go up

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

# Keep the window open until closed
running = True
while running:
    # Clear the screen while running so you don't create graphic bugs
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # This allows the game to exit when the player quits
            running = False
        
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
                        # Also add 1 to the current index because this one was solved
                        current_x_index = current_x_index + 1
                        # Add a new X to the list
                        if current_x_index < 9: # Create a new object if the X's can still make more
                            x_objects.append(XObject(obj_start_x, obj_start_y, font, obj_color))

                    else: # This does not snap and goes back to the starting position
                        x_obj.rect.center = (obj_start_x, obj_start_y)
                        # Make sure locked_in does not trigger so you can place it again
                        x_obj.locked_in = False

    # Display the x's on screen
    for x_obj in x_objects:
        if current_x_index <= len(x_objects): # If we are still in the game
            x_obj.draw(screen)
        if x_obj.locked_in == True: # Check to see if it is on screen already
            x_obj.draw(screen) # Pass in the screen object

    # Display the box and grid
    draw_box_and_grid()
    
    # Update the display to view the new grid
    pygame.display.update()

pygame.quit()