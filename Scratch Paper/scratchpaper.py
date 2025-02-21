import pygame

# Colors
RED = (250, 0, 0)
ORANGE = (200, 100, 0)
GREEN = (0, 150, 0)

# Define Flower class
class Flower:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        # Draw the stem
        pygame.draw.rect(screen, GREEN, (self.x - 10, self.y, 20, 100))

        # Draw the petals
        pygame.draw.circle(screen, RED, (self.x - 20, self.y), 20)  # top-left petal
        pygame.draw.circle(screen, RED, (self.x - 20, self.y - 40), 20)  # bottom-left petal
        pygame.draw.circle(screen, RED, (self.x + 20, self.y), 20)  # top-right petal
        pygame.draw.circle(screen, RED, (self.x + 20, self.y - 40), 20)  # bottom-right petal

        # Draw the center of the flower
        pygame.draw.circle(screen, ORANGE, (self.x, self.y - 20), 20)  # flower center

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Flower")

# Create a Flower object
flower = Flower(300, 220)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    screen.fill((255, 255, 255))  # white background

    # Draw the flower
    flower.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
