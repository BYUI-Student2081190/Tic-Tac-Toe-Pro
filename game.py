# This is a test of pygame change later to reflect actual game
import pygame

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

# Create the X object on screen
x_obj = font.render("X", True, obj_color) # Render the x object
x_rect = x_obj.get_rect(center = (max_width // 2, (max_height // 2) + 230)) # This gives the object a hit box, it can only be moved is the mouse is touching said hitbox

dragging = False # Default to false so it can be dragging only when a condition is met
offset_x, offset_y = 0, 0 # Movement on screen

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
    
        # Drag and Drop handling for game
        if event.type == pygame.MOUSEBUTTONDOWN and x_rect.collidepoint(event.pos):
            dragging = True # If the mouse is clicked on the object, then it can move
            offset_x, offset_y = event.pos[0] - x_rect.x, event.pos[1] - x_rect.y # Match the position of the mouse with the object

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False # The mouse is no longer being clicked so stop dragging the object

        if event.type == pygame.MOUSEMOTION and dragging:
            x_rect.x = event.pos[0] - offset_x # Set the object's location
            x_rect.y = event.pos[1] - offset_y # Set the object's location

    # Display the x on screen
    screen.blit(x_obj, x_rect)

    # Display the box and grid
    draw_box_and_grid()
    
    # Update the display to view the new grid
    pygame.display.update()

pygame.quit()