import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Procedural Cityscape")

offset = 0


# Function to draw a building with random features
def draw_building():
    xpos = random.randrange(-100, 800)
    ypos = random.randrange(0, 800)
    width = random.randrange(100, 200)
    color = random.randrange(50, 200)
    pygame.draw.rect(screen, (color, color, color), (xpos, ypos, width, 800))
    pygame.draw.rect(screen, (0, 0, 0), (xpos, ypos, width, 800), 2)
    for i in range(xpos + 10, xpos + width - 20, 30):
        for j in range(ypos + 10, ypos + 600, 60):
            pygame.draw.rect(screen, (200, 200, 50), (i, j, 20, 40))


def draw_tree():
    for x in range(75, 375, 675):
        for i in range(3):
            pygame.draw.rect(screen, (165, 42, 42), (x + offset, 300, 50, 300))
            pygame.draw.rect(screen, (165, 42, 42), (x + 300 + offset, 300, 50, 300))
            pygame.draw.rect(screen, (165, 42, 42), (x + 600 + offset, 300, 50, 300))
    for x in range(100, 800, 300):
        for i in range(3):
            pygame.draw.circle(screen, (42, 126, 25), (x + offset, 300), 40)
            pygame.draw.circle(screen, (42, 126, 25), (x - 50 + offset, 300), 40)
            pygame.draw.circle(screen, (42, 126, 25), (x + 50 + offset, 300), 40)


def draw_clouds():
    for x in range(100, 800, 300):
        for i in range(3):
            pygame.draw.circle(screen, (255, 255, 255), (x + offset, 100), 40)
            pygame.draw.circle(screen, (255, 255, 255), (x - 50 + offset, 125), 40)
            pygame.draw.circle(screen, (255, 255, 255), (x + 50 + offset, 125), 40)
        pygame.draw.rect(screen, (255, 255, 255), (x - 50 + offset, 100, 100, 65))


screen.fill((20, 20, 100))
for i in range(20):
    draw_building()
for i in range(20):
    draw_tree()
for i in range(20):
    draw_clouds()

pygame.display.update()
pygame.time.wait(50000)
pygame.quit()
