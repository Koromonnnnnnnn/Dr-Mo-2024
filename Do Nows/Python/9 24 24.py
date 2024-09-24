import pygame
import math

pygame.init()
pygame.display.set_caption("Spiral Pumpkins!")
screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 0))

PUMPKIN_ORANGE = (255, 165, 0)
GREEN = (0, 150, 0)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

def draw_pumpkin_spiral(x, y, width, height, depth, angle):
    if depth == 0:
        return
   
    pygame.draw.ellipse(screen, PUMPKIN_ORANGE, (x, y, width, height))
    pygame.draw.ellipse(screen, BLACK, (x, y, width, height), 2)
    
    stem_width = width // 5
    stem_height = height // 5
    pygame.draw.rect(screen, GREEN, (x + (width // 2 - stem_width // 2), y - stem_height, stem_width, stem_height))
    pygame.draw.rect(screen, BLACK, (x + (width // 2 - stem_width // 2), y - stem_height, stem_width, stem_height), 2)

    pygame.draw.ellipse(screen, BLACK, (x + width * 0.1, y, width * 0.8, height), 2)
    pygame.draw.ellipse(screen, BLACK, (x + width * 0.25, y, width * 0.5, height), 2)
    pygame.draw.ellipse(screen, BLACK, (x + width * 0.35, y, width * 0.3, height), 2)
    pygame.draw.ellipse(screen, BLACK, (x + width * 0.45, y, width * 0.1, height), 2)

    new_width = width * 1.15
    new_height = height * 1.15
    radius = width * 0.6
    new_x = x + radius * math.cos(angle)
    new_y = y + radius * math.sin(angle)
    new_angle = angle - math.pi / 6

    draw_pumpkin_spiral(new_x, new_y, new_width, new_height, depth - 1, new_angle)

initial_x = 250
initial_y = 500
initial_width = 30
initial_height = 20
recursion_depth = 20
initial_angle = 0

draw_pumpkin_spiral(initial_x, initial_y, initial_width, initial_height, recursion_depth, initial_angle)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
