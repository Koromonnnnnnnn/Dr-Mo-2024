import pygame
import random
from Platforms import Platform

# pygame boilerplate setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Base Dash Clone")

# game variables
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 60

# load player animation frames
try:
    walk1 = pygame.image.load("walk1.png")
    walk2 = pygame.image.load("walk2.png")
except pygame.error as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    exit()

# animation variables
current_frame = 0
animation_speed = 0.1
frame_timer = 0

# player variables
pw, ph = 10, 20
px, py = 50, 50
vx, vy = 5, 0
g = 0.5
jmp = -12  # changed this because it's not jumping high enough
double_jmp = -10
jumping = False
double_jump = False
jump_pressed = False

platforms = []

platform_add_timer = 0
platform_add_interval = 50


def get_player_rect(px, py, pw, ph):
    return pygame.Rect(px, py, pw, ph)


# game loop
while True:
    clock.tick(FPS)

    # event handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    # platform spawning logic
    platform_add_timer += 1
    if platform_add_timer >= platform_add_interval:
        platforms.append(Platform())
        platform_add_timer = 0
        print("Appending platform")

    # update and remove off-screen platforms
    for platform in platforms:
        platform.update()
        if platform.x + platform.width < 0:
            platforms.remove(platform)

    # animation logic
    frame_timer += animation_speed
    if frame_timer >= 1:
        frame_timer = 0
        current_frame = (current_frame + 1) % 2  # switch between frames

    # choose the correct frames
    if current_frame == 0:
        current_image = walk1
    else:
        current_image = walk2

    # player movement
    if keys[pygame.K_LEFT]:
        px -= vx
    if keys[pygame.K_RIGHT]:
        px += vx

    if keys[pygame.K_UP]:
        if not jump_pressed:
            if not jumping:
                vy = jmp
                jumping = True
            elif not double_jump:
                vy = double_jmp
                double_jump = True
            jump_pressed = True
    else:
        jump_pressed = False

    # apply gravity
    vy += g
    py += vy

    # define the player's rectangle
    player_rect = get_player_rect(px, py, pw, ph)

    # check if on ground and handle collisions with platforms
    on_ground = False
    for platform in platforms:
        platform_rect = pygame.Rect(
            platform.x, platform.y, platform.width, platform.height
        )

        if player_rect.colliderect(platform_rect):
            if vy > 0:
                py = platform.y - ph
                vy = 0
                jumping = False
                double_jump = False
                on_ground = True
            elif vy < 0:
                py = platform.y + platform.height
                vy = 0

    # check if on ground (if no collision)
    if not on_ground and py >= 600 - ph:
        py = 600 - ph
        vy = 0
        jumping = False
        double_jump = False

    # render section
    screen.fill(BLACK)

    # draw platforms
    for platform in platforms:
        platform.draw(screen)

    # draw player
    try:
        pygame.draw.rect(screen, BLUE, (px, py, pw, ph))
    except pygame.error as e:
        print(f"Error drawing player image: {e}")

    pygame.display.update()  # update display
