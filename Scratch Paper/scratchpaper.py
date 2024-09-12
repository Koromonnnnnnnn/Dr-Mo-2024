import pygame
import random
import math

pygame.init()
gamescreen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Particle Accelerator with Rainbow Path and Particles")
clock = pygame.time.Clock()

gameOver = False

# Particle attributes
xpos = []  # position
ypos = []
xVel = []  # velocity
yVel = []
sizes = []
colors = []  # Colors for particles
speed = 3

angle = 0
hue = 0  # Start hue for the rainbow effect

def hue_to_rgb(hue):
    """ Convert hue to an RGB color. """
    h = hue / 60.0
    c = 255
    x = c * (1 - abs((h % 2) - 1))
    r = g = b = 0

    if 0 <= h < 1:
        r, g, b = c, x, 0
    elif 1 <= h < 2:
        r, g, b = x, c, 0
    elif 2 <= h < 3:
        r, g, b = 0, c, x
    elif 3 <= h < 4:
        r, g, b = 0, x, c
    elif 4 <= h < 5:
        r, g, b = x, 0, c
    elif 5 <= h < 6:
        r, g, b = c, 0, x

    return (int(r), int(g), int(b))

while not gameOver:
    clock.tick(60)  # Cap the frame rate to 60 FPS

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # Update angle for path calculation
    angle += 1
    if angle > 360:
        angle = 0

    radians = math.radians(angle)

    # Update particles
    for i in range(1):
        if len(xpos) < 1000:
            velX = random.uniform(-1, 1)
            velY = random.uniform(-1, 1)
            magnitude = math.sqrt(velX**2 + velY**2)
            if magnitude != 0:
                normalizedVelX = speed * velX / magnitude
                normalizedVelY = speed * velY / magnitude
            else:
                normalizedVelX = 0
                normalizedVelY = 0

            xpos.append(400)
            ypos.append(400)
            sizes.append(1)
            colors.append(hue_to_rgb(hue))  # Initialize particle color
            xVel.append(normalizedVelX)
            yVel.append(normalizedVelY)

    # Update particle positions and velocities
    for i in range(len(xpos)):
        xpos[i] += xVel[i]
        ypos[i] += yVel[i]
        sizes[i] += 0.03

        # Boundary check
        if xpos[i] < 0 or xpos[i] > 800 or ypos[i] < 0 or ypos[i] > 800:
            xpos[i] = 400
            ypos[i] = 400
            sizes[i] = 1
            velX = random.uniform(-1, 1)
            velY = random.uniform(-1, 1)
            magnitude = math.sqrt(velX**2 + velY**2)
            if magnitude != 0:
                xVel[i] = speed * velX / magnitude
                yVel[i] = speed * velY / magnitude
            else:
                xVel[i] = 0
                yVel[i] = 0
            # Update particle color when resetting
            colors[i] = hue_to_rgb(hue)

    # Update position for graphical path
    xpos_path = int(50 * math.cos(radians * 5) + 400)
    ypos_path = int(50 * math.sin(radians * 5) + 400)

    # Update hue for rainbow effect
    hue += 1
    if hue >= 360:
        hue = 0

    # Convert hue to RGB for the path
    path_color = hue_to_rgb(hue)

    # Render
    gamescreen.fill((0, 0, 0))  # Clear the screen

    # Draw the particles
    for i in range(len(xpos)):
        pygame.draw.circle(gamescreen, colors[i], (int(xpos[i]), int(ypos[i])), int(sizes[i]))

    # Draw the rainbow path
    pygame.draw.circle(gamescreen, path_color, (xpos_path, ypos_path), 2)

    pygame.display.flip()

pygame.quit()
