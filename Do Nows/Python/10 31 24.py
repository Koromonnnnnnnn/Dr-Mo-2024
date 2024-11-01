import pygame

# Initialize Pygame
pygame.init()

# Create game screen
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Skull Drawing")

diaimage = pygame.image.load("DiaDeLosMuertos.png")
diaimage = pygame.transform.scale(
    diaimage, (800, 500)
) 

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.draw.ellipse(screen, WHITE, (250, 200, 300, 300))
    pygame.draw.ellipse(screen, WHITE, (285, 400, 225, 200))

    pygame.draw.circle(screen, BLACK, (350, 300), 50)
    pygame.draw.circle(screen, BLACK, (450, 300), 50)

    pygame.draw.polygon(screen, BLACK, [(400, 350), (375, 400), (425, 400)])

    for i in range(5):
        pygame.draw.rect(screen, BLACK, (340 + i * (20 + 5), 480, 20, 30))
        pygame.draw.rect(screen, BLACK, (340 + i * (20 + 5), 515, 20, 30))

    screen.blit(diaimage, (0, 450))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
