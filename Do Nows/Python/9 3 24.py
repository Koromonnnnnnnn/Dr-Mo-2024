import pygame

pygame.init()
pygame.display.set_caption("graphical for loops")
screen = pygame.display.set_mode((800, 800))

while 1:

    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen, (200, 0, 100), (i * 50, j * 50, 50, 50), 1)

    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen, (244, 244, 244), (i * 25, j * 25, 50, 50), 1)

    for i in range(20):
        for j in range(20):
            pygame.draw.rect(screen, (50, 200, 170), (i * 30, j * 30, 50, 50), 1)

    for i in range(20):
        for j in range(20):
            pygame.draw.rect(screen, (199, 234, 154), (i * 80, j * 80, 50, 50), 1)

    pygame.display.flip()

pygame.quit()
