import pygame

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Valentine's Day Card")
screen = pygame.display.set_mode((800, 800))
font = pygame.font.Font('freesansbold.ttf', 32)
img = pygame.image.load("dog.jpg")

class Heart:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self, surface):
        left_circle_center = (self.x - 20, self.y)
        right_circle_center = (self.x + 20, self.y)
        triangle_points = [(self.x - 40, self.y + 5),
                           (self.x + 40, self.y + 5),
                           (self.x, self.y + 50)]
        
        pygame.draw.circle(surface, self.color, left_circle_center, 20)
        pygame.draw.circle(surface, self.color, right_circle_center, 20)
        pygame.draw.polygon(surface, self.color, triangle_points)

class Flower:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self, surface):
        left_circle_center = (self.x - 20, self.y)
        right_circle_center = (self.x + 20, self.y)
        triangle_points = [(self.x - 40, self.y + 5),
                           (self.x + 40, self.y + 5),
                           (self.x, self.y + 50)]
        
    pygame.draw.circle(surface, (250,0,0), (180, 200), 20) #top left circle
    pygame.draw.circle(surface, (250,0,0), (220, 200), 20) #top right circle
    pygame.draw.polygon(surface, (250,0,0), ((160, 205),(239, 205), (200, 250))) #triangle to form base

# Create instances of Heart
heart1 = Heart(50, 200, (250, 0, 0))
heart2 = Heart(250, 200, (250, 0, 0))  # You can ask students to change positions and colors
heart3 = Heart(450, 200, (250, 0, 0))
heart4 = Heart(650, 200, (250, 0, 0)) 

# Draw everything
heart1.draw(screen)
heart2.draw(screen)
heart3.draw(screen)
heart4.draw(screen)

flower1.draw(screen)
flower2.draw(screen)
flower3.draw(screen)
flower4.draw(screen)

text1 = font.render('I Love You!', True, (250, 100, 100))
text2 = font.render('Happy Valentines Day', True, (250, 0, 0), (200, 150, 150))
screen.blit(text1, (200, 100))
screen.blit(text2, (400, 300))
screen.blit(img, (0, 400))

pygame.display.flip()
pygame.time.wait(5000)
