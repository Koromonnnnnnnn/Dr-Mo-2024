import pygame

pygame.init()
pygame.display.set_caption("Python For Loops")
screen = pygame.display.set_mode((800, 800))

gameover = False
while not gameover:

    screen.fill((0,0,0))

    for i in range(20):
        pygame.draw.rect(screen, (200,0,0), (50*i, 50, 20, 20)) #red
        pygame.draw.rect(screen, (0,0,200), (50*i, 100, 20, 20))
        pygame.draw.rect(screen, (200,200,0), (50*i, 150, 20, 20))
        pygame.draw.rect(screen, (0,200,200), (50*i, 200, 20, 20))

    pygame.display.update()

pygame.quit()