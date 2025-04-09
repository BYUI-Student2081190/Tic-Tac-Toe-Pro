# This is a test of pygame change later to reflect actual game
import pygame
from x_object import XObject

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

# Create the X Object
x_obj = XObject(max_width // 2, (max_height // 2) + 230, font, obj_color) # Pass in these to handle functions being called

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
        
        # Handle the events of the X Object
        x_obj.handle_event(event, box_x, box_y, box_size, cell_size)

    # Display the x on screen
    x_obj.draw(screen) # Pass in the screen object

    # Display the box and grid
    draw_box_and_grid()
    
    # Update the display to view the new grid
    pygame.display.update()

pygame.quit()