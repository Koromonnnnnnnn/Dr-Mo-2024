import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)
RED = (150, 0, 0)
HOVER_GRAY = (100, 100, 100)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Judgement - Main Menu")
clock = pygame.time.Clock()

try:
    title_font = pygame.font.Font('freesansbold.ttf', 72)
    menu_font = pygame.font.Font('freesansbold.ttf', 48)
except pygame.error:
    print("Default font not found, using system font.")
    title_font = pygame.font.SysFont(None, 80)
    menu_font = pygame.font.SysFont(None, 55)

try:
    background_image = pygame.image.load('cockpit.png').convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error:
    print("Background image not found. Using solid color.")
    background_image = None

try:
    pygame.mixer.music.load('horrormusic.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
except pygame.error:
    print("Background music not found or mixer issue.")

def draw_text(text, font, color, surface, x, y, center=True):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    if center:
        textrect.center = (x, y)
    else:
        textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect

def start_game():
    print("Starting game...")


def options_menu():
    print("Opening options...")


def main_menu():
    running = True
    while running:
        screen.fill(DARK_GRAY)

        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(DARK_GRAY)

        mx, my = pygame.mouse.get_pos()

        draw_text("Judgement", title_font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

        button_y_start = SCREEN_HEIGHT // 2
        button_spacing = 70

        button_start = draw_text("Start Game", menu_font, WHITE, screen, SCREEN_WIDTH // 2, button_y_start)
        button_options = draw_text("Options", menu_font, WHITE, screen, SCREEN_WIDTH // 2, button_y_start + button_spacing)
        button_exit = draw_text("Exit", menu_font, WHITE, screen, SCREEN_WIDTH // 2, button_y_start + 2 * button_spacing)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_start.collidepoint((mx, my)):
            draw_text("Start Game", menu_font, HOVER_GRAY, screen, SCREEN_WIDTH // 2, button_y_start)
            if click:
                start_game()


        if button_options.collidepoint((mx, my)):
            draw_text("Options", menu_font, HOVER_GRAY, screen, SCREEN_WIDTH // 2, button_y_start + button_spacing)
            if click:
                options_menu()

        if button_exit.collidepoint((mx, my)):
            draw_text("Exit", menu_font, HOVER_GRAY, screen, SCREEN_WIDTH // 2, button_y_start + 2 * button_spacing)
            if click:
                pygame.quit()

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main_menu()
