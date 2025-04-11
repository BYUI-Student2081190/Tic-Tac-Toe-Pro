# Import PyGame for use in this object
import pygame

# Create the class
class XObject:
    def __init__(self, x, y, font, color):
        self.image = font.render("X", True, color)
        self.rect = self.image.get_rect(center=(x, y))
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.locked_in = False
    
    # Add a function to condense the object
    def to_dict(self):
        return {
            "x": self.rect.centerx,
            "y": self.rect.centery,
            "locked_in": self.locked_in
        }
    
    # Add a function to restore the object after being a dict
    def from_dict(cls, data, font, color):
        
        # Recreate the object to load
        obj = cls(
            x = data.get("x"),
            y = data.get("y"),
            font = font,
            color = color
        )

        obj.locked_in = data.get("locked_in", False) # Restore state

        # Return the object
        return obj

    def draw(self, screen): # Display self to screen.
        screen.blit(self.image, self.rect.topleft)
    
    def handle_event(self, event, box_x, box_y, box_size, cell_size):
        # Drag and Drop handling for game
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and self.locked_in != True:
            self.dragging = True # If the mouse is clicked on the object, then it can move
            self.offset_x, self.offset_y = event.pos[0] - self.rect.x, event.pos[1] - self.rect.y # Match the position of the mouse with the object

        if event.type == pygame.MOUSEBUTTONUP and self.locked_in != True:
            self.dragging = False # The mouse is no longer being clicked so stop dragging the object
            # Make the x snap to a square in the grid
            if box_x <= event.pos[0] <= box_x + box_size and box_y <= event.pos[1] <= box_y + box_size:
                grid_x = (event.pos[0] - box_x) // cell_size # Get the posistion for the grid box
                grid_y = (event.pos[1] - box_y) // cell_size # Get the posistion for the grid box
                self.rect.center = (box_x + grid_x * cell_size + cell_size // 2, box_y + grid_y * cell_size + cell_size // 2 + 10) # Snap the object into the grid box in the center of the box
                # Set locked in to true so it can't move anymore after it has been placed.
                self.locked_in = True

        if event.type == pygame.MOUSEMOTION and self.dragging and self.locked_in != True:
            self.rect.x = event.pos[0] - self.offset_x # Set the object's location
            self.rect.y = event.pos[1] - self.offset_y # Set the object's location