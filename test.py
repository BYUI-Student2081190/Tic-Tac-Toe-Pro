# This is a test of pygame. Change later.
import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 300))
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