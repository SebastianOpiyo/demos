
import pygame  # accesses pygame files
import sys  # to communicate with windows, i.e sys.exit to quit the game
import os  # to communicate with OS
import random  # To generate random objects
from pygame.locals import *  # Basic pygame imports

# game setup ################ only runs once

# global variables
FPS = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 800, 600  # sets size of screen/window
screen = pygame.display.set_mode(SCREENSIZE)  # creates window and game screen
clock = pygame.time.Clock()  # creates clock to limit frames per second


# set variables for colors RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

# background image
backgroundimage = pygame.image.load(os.path.join("assets", "background.png")).convert_alpha()
backgroundimage = pygame.transform.scale(backgroundimage, (SCREENWIDTH,SCREENHEIGHT))

# player images
player1Image1 = pygame.image.load(os.path.join("assets", "1.png")).convert_alpha()
player1Image2 = pygame.image.load(os.path.join("assets", "2.png")).convert_alpha()
player1Image3 = pygame.image.load(os.path.join("assets", "3.png")).convert_alpha()
player1Image4 = pygame.image.load(os.path.join("assets", "4.png")).convert_alpha()
player1Image5 = pygame.image.load(os.path.join("assets", "5.png")).convert_alpha()
player1Image6 = pygame.image.load(os.path.join("assets", "6.png")).convert_alpha()
flappybird = player1Image1
pipe_surface = pygame.image.load(os.path.join("assets", "pipe.png"))
pipe_surface = pygame.transform.scale2x(pipe_surface)

# resize images
player1ImageWidthHeight = [75, 100]  # set size for player sprite
player1Image1 = pygame.transform.scale(player1Image1, player1ImageWidthHeight)  # modifies size of image
player1pos = [SCREENWIDTH//2, SCREENHEIGHT//2]    #X,Y for centre
animate1 = [player1Image1, player1Image2, player1Image3, player1Image4, player1Image5, player1Image6]

# sound effects
die_sound = os.path.join("assets","sfx_die.ogg")
Flip_sound = os.path.join("assets", "Laser_Cannon.ogg")

pipe_list = []
pipe_height = [400, 450, 500]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 200)


# animateclock = 1
# animatepos = 3
# animateclock = animateclock + 1
# if animateclock >=20:
#     animateclock = 0
#     animatepos = animatepos + 1
#     if animatepos == 3:
#         animatepos = 0


def draw_screen():
    screen.fill(black)
    screen.blit(backgroundimage, (0, 0))
    pygame.display.set_caption("Flappy Bird by Patto!")
    pygame.display.update()
    clock.tick(FPS)


def display_bird(bird_image, x, y):
    screen.blit(bird_image, (x, y))


def main():
    startTime = pygame.time.get_ticks()  # stores current time
    gameState = "running"  # controls which state the games is in
    # game loop #################### runs 60 times a second!
    while gameState != "exit":  # game loop - note:  everything in the mainloop is indented one tab
        draw_screen()
        for event in pygame.event.get():  # get user interaction events
            # if user clicks X (close) on the window, close the game
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                gameState = "exit"  # causes exit of game loop
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                # draw the screen
                # draw_screen()
                pass


        # draw the player
        screen.blit(player1Image1, (player1pos[0], player1pos[1]))
        # draw obstacles

        # out of game loop ###############
        # your code ends here ###############################
        pygame.display.flip()  # transfers build screen to human visible screen
        clock.tick(FPS)  # limits game to frame per second, FPS value
        print("The game has closed")  # notifies user the game has ended
        pygame.quit()  # stops the game engine
        sys.exit()  # close operating system window


def check_collision(pipes):
    for pipe in pipes:

        if flappybird.colliderect(pipe):
            pygame.mixer.init()
            pygame.mixer.music.load(die_sound)
            pygame.mixer.music.play()
            pygame.event.wait()
            return False
    if flappybird.top <= -100 or flappybird.bottom >=900:
        return False
    return True


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    top_pipe = pipe_surface.get_rect(midbottom =(700, random_pipe_pos-300))
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5

    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe, pipe)
            pygame.init()
            clock()


def move_player(player):
    player[1]+=5
    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if not player[1] > 0:
            player[1] -= 10
    elif keys[pygame.K_DOWN]:
        if not player[1] < SCREENHEIGHT-100:
            player[1] += 10


if __name__ == "__main__":
    pygame.init()  # starts the game engine
    main()
