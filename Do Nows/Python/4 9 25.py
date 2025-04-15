import pygame
import math

pygame.init()
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Concentric Arc Circles")

# Define colors

BLACK = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
chartreuse = (127, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (160, 32, 240)
magenta = (255, 0, 255)
rose = (255, 105, 180)
maroon = (128, 0, 0)
teal = (0, 128, 128)

# Fill background with black

screen.fill(BLACK)

# Inner Circle

pygame.draw.arc(screen, orange, (200, 150, 400, 400), math.pi / 2, math.pi, 12)
pygame.draw.arc(screen, red, (200, 150, 400, 400), 0, math.pi / 2, 12)
pygame.draw.arc(screen, yellow, (200, 150, 400, 400), math.pi, 3 * math.pi / 12, 12)
pygame.draw.arc(screen, orange, (200, 150, 400, 400), math.pi / 2, math.pi, 12)

# Middle Circle

pygame.draw.arc(
    screen, purple, (180, 130, 440, 440), 7 * math.pi / 4, 9 * math.pi / 4, 12
)
pygame.draw.arc(screen, green, (180, 130, 440, 440), math.pi / 4, 3 * math.pi / 4, 12)
pygame.draw.arc(
    screen, purple, (180, 130, 440, 440), 7 * math.pi / 4, 9 * math.pi / 4, 12
)
pygame.draw.arc(
    screen, purple, (180, 130, 440, 440), 7 * math.pi / 4, 9 * math.pi / 4, 12
)


# Outer Circle

pygame.draw.arc(screen, red, (160, 110, 480, 480), 0, math.pi / 6, 12)


pygame.draw.arc(
    screen, magenta, (160, 110, 480, 480), 4 * math.pi / 3, 3 * math.pi / 2, 12
)


pygame.display.flip()

# Main loop to keep window open

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
