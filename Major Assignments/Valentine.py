import pygame

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Valentine's Day Card")
screen = pygame.display.set_mode((800, 800))
font = pygame.font.Font("freesansbold.ttf", 32)
img = pygame.image.load("dog.jpg")

RED = (250, 0, 0)
ORANGE = (200, 100, 0)
GREEN = (0, 150, 0)



class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        left_circle_center = (self.x - 20, self.y)
        right_circle_center = (self.x + 20, self.y)
        triangle_points = [
            (self.x - 40, self.y + 5),
            (self.x + 40, self.y + 5),
            (self.x, self.y + 50),
        ]

        pygame.draw.circle(surface, self.color, left_circle_center, 20)
        pygame.draw.circle(surface, self.color, right_circle_center, 20)
        pygame.draw.polygon(surface, self.color, triangle_points)

    def draw2(self, screen):
        # Draw the stem
        pygame.draw.rect(screen, GREEN, (self.x - 10, self.y, 20, 100))

        # Draw the petals
        pygame.draw.circle(screen, RED, (self.x - 20, self.y), 20)  # top-left petal
        pygame.draw.circle(
            screen, RED, (self.x - 20, self.y - 40), 20
        )  # bottom-left petal
        pygame.draw.circle(screen, RED, (self.x + 20, self.y), 20)  # top-right petal
        pygame.draw.circle(
            screen, RED, (self.x + 20, self.y - 40), 20
        )  # bottom-right petal

        # Draw the center of the flower
        pygame.draw.circle(screen, ORANGE, (self.x, self.y - 20), 20)  # flower center

class Heart(Shape):
  def __init__(self, x, y, color):
    super().__init__(x, y, color)


class Flower(Shape):
  def __init__(self, x, y, color):
    super().__init__(x, y, color)


# Create instances of Heart
heart1 = Heart(50, 100, (250, 0, 0))
heart2 = Heart(
    250, 100, (250, 0, 0)
)  # You can ask students to change positions and colors
heart3 = Heart(450, 100, (250, 0, 0))
heart4 = Heart(650, 100, (250, 0, 0))

flower1 = Flower(50, 220, (250, 0, 0))
flower2 = Flower(250, 220, (250, 0, 0))
flower3 = Flower(450, 220, (250, 0, 0))
flower4 = Flower(650, 220, (250, 0, 0))

# Draw everything
heart1.draw(screen)
heart2.draw(screen)
heart3.draw(screen)
heart4.draw(screen)

flower1.draw2(screen)
flower2.draw2(screen)
flower3.draw2(screen)
flower4.draw2(screen)

text1 = font.render("I Love You!", True, (255, 255, 255))
text2 = font.render("Happy Valentines Day", True, (250, 0, 0), (200, 150, 150))
screen.blit(text1, (200, 100))
screen.blit(text2, (400, 300))
screen.blit(img, (0, 400))

pygame.display.flip()
pygame.time.wait(60000)
