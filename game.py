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

# Define color
BLACK = (0, 0, 0)
screen.fill(BLACK)
pygame.display.update() # This makes sure that the screen updates before moving on

# Define Box properties
box_color = (255, 255, 255) # This is white
box_size = 400 # Box size
box_line_width = 5 # Line thickness
box_x = (max_width - box_size) // 2
box_y = (max_height - box_size) // 2

# Define Grid properties
grid_color = (255, 255, 255) # This is white
grid_size = 3 # This is the size of the grid on screen
grid_line_width = 5 # Line thickness
cell_size = box_size // grid_size # How big each cell is in the grid inside the box

# Keep the window open until closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # This allows the game to exit when the player quits
            running = False
    
    # Draw box for grid to fit inside of

    # For now set up the grid here for tic-tac-toe
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
    
    # Update the display to view the new grid
    pygame.display.update()


pygame.quit()