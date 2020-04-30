import pygame as pg

class Score:
    def __init__(self):
        self.score = 0
        self.font = pg.font.SysFont("arialunicodettf", 12)

    # Update the score when the snake has eaten the pellet.
    def updateScore(self):
        self.score += 100

    def returnScore(self):
        return "Score: " + str(self.score)

    def returnFont(self):
        return self.font

    