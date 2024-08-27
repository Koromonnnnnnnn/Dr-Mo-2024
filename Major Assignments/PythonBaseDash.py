import pygame

#pygame boilerplate setup
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Base Dash Clone")

#game variables
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FPS = 60

#player variables
pw, ph = 10, 20
px, py = 50, 50
vx, vy = 5, 0
g = 0.5
jmp = -10
double_jmp = -5
jumping = False
double_jump = False
jump_pressed = False

#game loop
while True:
    clock.tick(FPS)

    #event handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    keys = pygame.key.get_pressed()

    #physics

    #player movement
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

    #apply gravity
    vy += g
    py += vy

    #check if on ground
    if py >= 600 - ph:
        py = 600 - ph
        jumping =  False
        double_jump = False
        vy = 0

    #render section
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (px, py, pw, ph)) #player
    pygame.display.flip() #update display