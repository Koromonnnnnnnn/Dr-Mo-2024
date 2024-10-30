# Takes about 2 seconds to load

import pygame

WIDTH = 800
HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0, 0, 0))


def mandelbrot(c):
    z = 0
    counter = 0

    while abs(z) < 2 and counter < 80:
        z = z * z + c
        counter += 1

    return counter


for x in range(800):
    for y in range(800):
        t = (x / 800) * 4 - 2
        m = (y / 800) * 4 - 2
        c = complex(t, m)

        num = mandelbrot(c)
        if num < 20:
            color = (0, 0, 0)
        elif num < 40:
            color = (255, 0, 0)
        elif num < 60:
            color = (0, 255, 0)
        elif num < 80:
            color = (0, 0, 255)
        else:
            color = (0, 0, 0)

        screen.set_at((x, y), color)

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
