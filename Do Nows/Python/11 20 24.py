import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Pattern Generator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 90, 167)

current_color = RED
current_shape = "triangle"
SHAPE_SIZE = 40

shapeList = []

font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_shape = "ellipse"
            elif event.key == pygame.K_2:
                current_shape = "hexagon"
            elif event.key == pygame.K_3:
                current_shape = "triangle"
            elif event.key == pygame.K_4:
                current_shape = "star"
            elif event.key == pygame.K_5:
                current_shape = "rectangle"
            if event.key == pygame.K_w:
                current_color = WHITE
            elif event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_b:
                current_color = BLUE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            new_shape = [mouse_x, mouse_y, SHAPE_SIZE, current_color, current_shape]
            shapeList.append(new_shape)

    screen.fill(WHITE)

    for shape in shapeList:
        x, y, size, color, kind = shape

        if kind == "ellipse":
            pygame.draw.ellipse(screen, color, (x - size, y - size // 2, size * 2, size))
        elif kind == "hexagon":
            points = [
                (x, y - size),
                (x + size, y - size // 2),
                (x + size, y + size // 2),
                (x, y + size),
                (x - size, y + size // 2),
                (x - size, y - size // 2),
            ]
            pygame.draw.polygon(screen, color, points)
        elif kind == "triangle":
            points = [
                (x, y - size),
                (x - size, y + size),
                (x + size, y + size),
            ]
            pygame.draw.polygon(screen, color, points)
        elif kind == "rectangle":
            points = [
                (x - size, y - size),
                (x + size, y - size),
                (x + size, y + size),
                (x - size, y + size),
            ]
            pygame.draw.polygon(screen, color, points)
        elif kind == "star":
            points = [
                (x, y - size),
                (x + size * 0.2, y - size * 0.2),
                (x + size * 0.5, y - size * 0.5),
                (x + size * 0.3, y + size * 0.1),
                (x + size * 0.6, y + size * 0.5),
                (x, y + size * 0.2),
                (x - size * 0.6, y + size * 0.5),
                (x - size * 0.3, y + size * 0.1),
                (x - size * 0.5, y - size * 0.5),
                (x - size * 0.2, y - size * 0.2),
            ]
            pygame.draw.polygon(screen, color, points)

    instructions = font.render(
        "1: Ellipse  2: Hexagon  3: Triangle  4: Star  5: Rectangle |  W: White  R: Red  B: Blue",
        True,
        BLACK,
    )
    screen.blit(instructions, (10, 10))

    pygame.display.flip()

pygame.quit()
