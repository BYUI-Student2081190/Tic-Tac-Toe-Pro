# This is a test of pygame change later to reflect actual game
import pygame

# Initialize Pygame
pygame.init()

# Create varibles for screen size
max_width = 400
max_height = 300

# Set up display
screen = pygame.display.set_mode((max_width, max_height))
pygame.display.set_caption("Pygame Test")

# Define color
RED = (255, 0, 0)
screen.fill(RED)
pygame.display.update() # This makes sure that the screen updates before moving on.

# Keep the window open until closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()