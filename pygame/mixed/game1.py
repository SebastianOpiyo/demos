# pygame template - Bourne Grammar 2016

import pygame  # accesses pygame files
import sys  # to communicate with windows
# game setup ################ only runs once
pygame.init()  # starts the game engine
clock = pygame.time.Clock()  # creates clock to limit frames per second
FPS = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 800   , 600  # sets size of screen/window
screen = pygame.display.set_mode(SCREENSIZE)  # creates window and game screen
# set variables for colors RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
orange = (240, 129, 19)
rectx = 0
speed = 1
gameState = "running"  # controls which state the games is in
# game loop #################### runs 60 times a second!
player1Image = pygame.image.load("MicrosoftTeams-image.png")

player1XY = [100, 100]
while gameState != "exit":  # game loop - note:  everything in the mainloop is indented one tab
    screen.fill(green)
    for event in pygame.event.get():  # get user interaction events
        if event.type == pygame.QUIT:  # tests if window's X (close) has been clicked
            gameState = "exit"  # causes exit of game loop
    # your code starts here ##############################
    player1 = screen.blit(player1Image, player1XY)

    pygame.draw.rect(screen,red,(rectx,200,50,50))
    rectx = rectx+speed
    if rectx > SCREENWIDTH:
        speed = -speed
    mousePosition = pygame.mouse.get_pos()
    player1XY[0] = mousePosition[0]-25
    player1XY[1] = mousePosition[1]-25
    if mousePosition[0] > rectx-20 and pygame.mouse.get_pressed()[0] == True:
        print("Winnnnnnnn!!!!")
    if rectx < SCREENWIDTH:
        speed = speed + 1

    # your code ends here ###############################
    pygame.display.flip()  # transfers build screen to human visable screen
    clock.tick(FPS)  # limits game to frame per second, FPS value

# out of game loop ###############
print("The game has closed")  #
