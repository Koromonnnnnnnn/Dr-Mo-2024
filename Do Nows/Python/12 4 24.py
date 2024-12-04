import pygame
pygame.init()
pygame.joystick.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("controller input!")
clock = pygame.time.Clock()

# Check if a joystick is connected
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
    joystick.init()
    print("Joystick connected:", joystick.get_name())
else:
    print("No joystick detected!")
    joystick = None

#player variables
px = 300
py = 300

# Game loop
running = True
while running:
    #input section--------------------------------------------
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #NOTE: you will want to comment out the print statements here to make code less laggy (that's why the continue statements are there)

        # Handle joystick button presses
        if event.type == pygame.JOYBUTTONDOWN:
            print("Button pressed:", event.button) 
            continue
        if event.type == pygame.JOYBUTTONUP:
            print("Button released!")
            continue
        # Handle joystick axis motion
        if event.type == pygame.JOYAXISMOTION:
            print("Axis", event.axis, "moved to", event.value)
            continue

        # Handle joystick hat (D-pad) motion
        if event.type == pygame.JOYHATMOTION:
            print("Hat moved to", event.value)
            continue
        
    #update section-----------------------------------------------
    stick1 = joystick.get_axis(0)
    if abs(stick1) > .01:
        px += stick1*10 #number multiplied here is speed

    #TODO: add y movement here (y axis is 1)
        
    #TODO: can you add color changes when buttons are pressed?

    #render section-----------------------------------------------
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (40, 40, 150), (px, py, 50, 50))  # Draw the player

    pygame.display.flip()


pygame.quit()
