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

# Define Grid properties
grid_color = (255, 255, 255) # This is white
grid_size = 100 # This is the size of the grid on screen

# Grid Positions
grid_line_width = 5 # Line thickness
grid_positions = [
    ((max_width / 3, 0), (max_width / 3, max_height)),
    ((2 * max_width / 3, 0), (2 * max_width / 3, max_height)),
    ((0, max_height / 3), (max_width, max_height / 3)),
    ((0, 2 * max_height / 3), (max_width, 2 * max_height / 3)),
]

# Keep the window open until closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # This allows the game to exit when the player quits
            running = False
    
    # For now set up the grid here for tic-tac-toe
    # Draw the grid lines
    for grid_start_pos, grid_end_pos in grid_positions:
        pygame.draw.line(screen, grid_color, grid_start_pos, grid_end_pos, grid_line_width)
    
    # Update the display to view the new grid
    pygame.display.update()


pygame.quit()