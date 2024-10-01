import pygame
import math
import cmath

WIDTH = 800
HEIGHT = 800

pygame.init()
pygame.display.set_caption("mandelbrot")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0, 0, 0))


def mandelbrot(c):
    z = 0
    counter = 0

    while abs(z) < 2 and counter < 80:
        z = z * z + c
        counter += 1

    return counter


for x in range(WIDTH):
    for y in range(HEIGHT):
        t = -2
        m = -2

        while t<2:
            t+=1

        while m<2:
            m+=1

        c = complex(t, m)

        num = mandelbrot(c)
        if num < 20:
            screen.set_at((int(t), int(m)), (255, 255, 255))
            pygame.display.flip()


pygame.time.wait(10009)
pygame.quit()
