import player
import food
import score
import pygame as pg


pg.init()

screen = pg.display.set_mode((700, 700))

background = pg.Surface(screen.get_size())  # Create empty pygame surface
background.fill((0,0,0))     # Fill the background white color (red,green,blue)
background = background.convert()  # Convert Surface to make blitting faster

screen.blit(background, (0, 0))

clock = pg.time.Clock()

mainloop = True

FPS = 25 # faster = more difficult

playtime = 0.0

snakeyBoi = player.Player()
pellet = food.Food()
score = score.Score()

font = score.returnFont()

movement = "NULL"

# Loop the game
while mainloop:
    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0

    text = font.render(score.returnScore(), True, (255, 255, 255))

    textArea = text.get_rect()

    textArea.centerx = 40
    textArea.centery = 25

    # Get the event. If "ESC" is hit, quit the game. If the user closes the window, end the game
    # Or else, check if they push left, right, up, or down.
    lastDir = movement
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            mainloop = False # pygame window closed by user
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                mainloop = False # user pressed ESC
            if event.key == pg.K_LEFT and lastDir != "RIGHT":
                movement = "LEFT"
            if event.key == pg.K_RIGHT and lastDir != "LEFT":
                movement = "RIGHT"
            if event.key == pg.K_UP and lastDir != "DOWN":
                movement = "UP"
            if event.key == pg.K_DOWN and lastDir != "UP":
                movement = "DOWN"

    # Wrap the player if they go out of bounds.
    snakeyBoi.wrapAround()

    # Depending on the last pushed key, keep moving in that direction.
    if movement == "LEFT":
        snakeyBoi.handle_keys("LEFT")
    elif movement == "RIGHT":
        snakeyBoi.handle_keys("RIGHT")
    elif movement == "UP":
        snakeyBoi.handle_keys("UP")
    elif movement == "DOWN":
        snakeyBoi.handle_keys("DOWN")

    if snakeyBoi.foodSpawnInSnake(pellet):
        pellet.eaten()

    snakeyBoi.growSnake()
    if snakeyBoi.didSnakeEatPellet(pellet.selfAsRec()):
        pellet.eaten()
        score.updateScore()
    else:
        snakeyBoi.shrinkSnake()

    if not movement == "NULL":
        if snakeyBoi.collideWithSelf():
            mainloop = False

    # Empty the screen and redraw the new position.
    screen.fill((0, 0, 0))
    pellet.draw(screen)
    snakeyBoi.draw(screen)

    screen.blit(text, textArea)

    pg.display.update()

    # Print framerate and playtime in titlebar.
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    pg.display.set_caption(text)

    #Update Pygame display.
    pg.display.flip()


# Finish Pygame.  
pg.quit()

# At the very last:
print("This game was played for {0:.2f} seconds".format(playtime))
