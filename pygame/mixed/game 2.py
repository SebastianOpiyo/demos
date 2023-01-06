# pygame template - Bourne Grammar 2016
import random
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
circlex = 0
circley = 0
speed = 5
gameState = "running"  # controls which state the games is in
# game loop #################### runs 60 times a second!
while gameState != "exit":  # game loop - note:  everything in the mainloop is indented one tab
    screen.fill(black)
    mousePosition = pygame.mouse.get_pos()
    random_height = random.randint(1,25)
    for event in pygame.event.get():  # get user interaction events
        if event.type == pygame.QUIT:  # tests if window's X (close) has been clicked
            gameState = "exit"  # causes exit of game loop
    # your code starts here ##############################
    pygame.draw.circle(screen, red, (circlex, circley), 150)
    pygame.draw.circle(screen, yellow, (circlex, circley), 100)
    pygame.draw.circle(screen, green, (circlex, circley), 50)
    circlex = circlex+speed
    if circlex > 745:
        speed = -speed
    if circlex < 0:
        speed = -speed
    mouseposition = pygame.mouse.get_pos()
    if circlex-35 <mouseposition[0] <circlex+35 and pygame.mouse.get_pressed()[0] == 0:

        circley = random =random.randint(400, 700)
        circlex = random =random.randint(400, 700)
        score = score+1

    speed = 10


    # your code ends here ###############################
    pygame.display.flip()  # transfers build screen to human visable screen
    clock.tick(FPS)  # limits game to frame per second, FPS value
# out of game loop ###############
print("The game has closed")  # notifies user the game has ended
pygame.quit()   # stops the game engine
sys.exit()  # close operating system window
