import random
import pygame as pg

class Food:
    def __init__(self):
        self.x = random.randint(2, 27) * 25
        self.y = random.randint(2, 27) * 25
        self.pellet = pg.Rect(self.x, self.y, 25, 25)

    # If the pellet is eaten, randomize a new location.
    def eaten(self):
        self.x = random.randint(2, 27) * 25
        self.y = random.randint(2, 27) * 25
        self.pellet = pg.Rect(self.x, self.y, 25, 25)

    # Return the food as a Rectangle so we can check if the snake has eaten the food.
    def selfAsRec(self):
        return self.pellet

    # Draw the pellet
    def draw(self, surface):
        pg.draw.rect(surface, (204, 102, 0), self.pellet)

