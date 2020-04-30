import random
import pygame as pg

class Player:    
    # Create the snake. Make sure it's position is a multiple of 25, since our snake size is 25.
    def __init__(self):
        self.x = random.randint(4, 24) * 25
        self.y = random.randint(4, 24) * 25
        self.snakeHead = [self.x, self.y]
        self.snakePositions = [[self.x, self.y], [self.x - 25, self.y], [self.x - 50, self.y]]


    # Depending on the arrows pushes, we make it move left/right/up/down.
    def handle_keys(self, input):
        if input == "LEFT":
            self.snakeHead[0] -= 25
        if input == "RIGHT":
            self.snakeHead[0] += 25
        if input == "UP":
            self.snakeHead[1] -= 25
        if input == "DOWN":
            self.snakeHead[1] += 25


    # If they go off screen, wrap around to the other side.
    def wrapAround(self):
        if self.snakeHead[0] < 0:
            self.snakeHead[0] = 700
        elif self.snakeHead[0] > 700:
            self.snakeHead[0] = -25

        if self.snakeHead[1] < 0:
            self.snakeHead[1] = 700
        elif self.snakeHead[1] > 700:
            self.snakeHead[1] = -25

    # Check to see if the snake has "eaten" the pellet. (If the position of the pellet and the head of the snake are the same)
    def didSnakeEatPellet(self, pellet):
        return ( (self.snakeHead[0], self.snakeHead[1]) == (pellet.x, pellet.y) )

    def foodSpawnInSnake(self, pellet):
        for snakePos in self.snakePositions:
            if (snakePos[0], snakePos[1]) == (pellet.x, pellet.y):
                return True
        
    # Grow the snake so we can "move"
    def growSnake(self):
        self.snakePositions.insert(0, list(self.snakeHead))

    # Shrink the snake
    def shrinkSnake(self):
        self.snakePositions.pop()

    # Check to see if the snake collides with itself.
    def collideWithSelf(self):
        for body in self.snakePositions[1:]:
            if (self.snakeHead[0], self.snakeHead[1]) == (body[0], body[1]):
                return True


    # Draw the snake
    def draw(self, surface):
        for position in self.snakePositions:
            pg.draw.rect(surface, (90, 255, 90, .3), pg.Rect(position[0], position[1], 25, 25))
 