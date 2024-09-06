import pygame
import math

pygame.init()
pygame.display.set_caption("Graphical for loops")
screen = pygame.display.set_mode((800, 800))


gameover = False  # variable to run our game loop
angle = 0


while (
    not gameover
):  # Game loop----------------------------------------------------------------

    angle += 1
    if angle > 360:
        angle = 0

    radians = angle * 180 / 3.14

    xpos = 20 * math.cos(radians) + 200
    ypos = 20 * math.sin(radians) + 200

    # multiplying front of the trig functions by a constant makes the circle bigger
    # adding something to the end changes the position of the circle

    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 2)

    pygame.display.flip()

pygame.quit()
