import pygame

pygame.init()
pygame.display.set_caption("graphical for loops")
screen = pygame.display.set_mode((500, 500))

while 1:

    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen, (200, 0, 100), (i * 50, j * 50, 50, 50), 1)

    pygame.display.flip()

pygame.quit()
