import pygame
import random

GREEN = (0, 100, 0)
BLUE = (0, 50, 150)


class Platform:
    def __init__(self):
        self.width = random.randint(20, 30)
        self.height = 30
        self.x = 800
        self.y = random.randint(400, 550)
        self.speed = random.uniform(5, 7)
        self.type = random.randint(0, 2)
