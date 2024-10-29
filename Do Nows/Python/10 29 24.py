import pygame
import random

pygame.init()
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    event = pygame.event.get()

    for event in pygame.event.get():
        break

    pygame.time.wait(200)

    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()
