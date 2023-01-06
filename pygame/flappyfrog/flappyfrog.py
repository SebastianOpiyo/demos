# either Frogger or Flappy Bird style game
# IMPORTS
import pygame  # accesses pygame files
import pygame.locals import *  # has basic functionalities we will use
import sys  # to communicate with windows
import os



# CONSTANTS
FPS = 60  # sets max speed of main loop
SCREENWIDTH, SCREENHEIGHT = 800 , 600
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT  # sets size of screen/window
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)



def main():
    # game setup ################ only runs once
    pygame.init()  # starts the game engine
    clock = pygame.time.Clock()  # creates clock to limit frames per second


    screen = pygame.display.set_mode(SCREENSIZE)  # creates window and game screen

    # Background Image
    backgroundImage = pygame.image.load(os.path.join('Assets', 'background.png')).convert_alpha()
    backgroundImage = pygame.transform.scale(backgroundImage, (SCREENWIDTH, SCREENHEIGHT))

    player1Image1 = pygame.image.load(os.path.join('Assets', '1.png')).convert_alpha()
    player1Image2 = pygame.image.load(os.path.join('Assets', '2.png')).convert_alpha()
    player1Image3 = pygame.image.load(os.path.join('Assets', '3.png')).convert_alpha()
    player1Image4 = pygame.image.load(os.path.join('Assets', '4.png')).convert_alpha()
    player1Image5 = pygame.image.load(os.path.join('Assets', '5.png')).convert_alpha()
    player1Image6 = pygame.image.load(os.path.join('Assets', '6.png')).convert_alpha()
    # resize images
    player1ImageWidthHeight = [300, 400]  # set size for player sprite
    player1Image1 = pygame.transform.scale(player1Image1, player1ImageWidthHeight)  # modifies size of image
    player1pos = [SCREENWIDTH//2, SCREENHEIGHT//2]    #X,Y for centre
    animate1 = [player1Image1,player1Image2,player1Image3,player1Image4,player1Image5,player1Image6]
    animateclock = 0
    animatepos = 0
    startTime = pygame.time.get_ticks()  # stores current time

    gameState = "running"  # controls which state the games is in
    i = 0
    # game loop #################### runs 60 times a second!
    while gameState != "exit":  # game loop - note:  everything in the mainloop is indented one tab

        for event in pygame.event.get():  # get user interaction events
            if event.type == pygame.QUIT:  # tests if window's X (close) has been clicked
                gameState = "exit"  # causes exit of game loop
        # your code starts here ##############################
        
        # Screen
        screen.fill(BLACK)
        screen.blit(backgroundImage, (i,0))


        # draw the player


        screen.blit(player1Image1, (player1pos[0], player1pos[1]))
        animateclock = animateclock + 1
        if animateclock >=20:
            animateclock = 0
            animatepos = animatepos + 1
            if animatepos == 3:
                animatepos = 0

        # draw the obstacles


        # move the obstacles


        # move the player
        player1pos[1]+=5
        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if not player1pos[1] < 0:
                player1pos[1] -= 10
        elif keys[pygame.K_DOWN]:
            if not player1pos[1] > SCREENHEIGHT-100:
                player1pos[1] += 10




        # detect a collision
        #if <nameofobstacle>.colliderect(player1Image):
            # game over!
            #print("Time alive: ", pygame.time.get_ticks() - startTime)

        # your code ends here ###############################
        pygame.display.flip()  # transfers build screen to human visible screen
        clock.tick(FPS)  # limits game to frame per second, FPS value

    # out of game loop ###############
    print("The game has closed")  # notifies user the game has ended
    pygame.quit()   # stops the game engine
    sys.exit()  # close operating system window
    



if __name__ == "__main__":
    main()