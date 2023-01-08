# either Frogger or Flappy Bird style game
import pygame  # accesses pygame files
import sys  # to communicate with windowsimport os  # to communicate with OS
import os
import random  # To generate random objects
from pygame.locals import *  # Basic pygame imports


# game setup ################ only runs once
pygame.init()  # starts the game engine
clock = pygame.time.Clock()  # creates clock to limit frames per second
FPS = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 800, 600  # sets size of screen/window
screen = pygame.display.set_mode(SCREENSIZE)  # creates window and game screen

# set variables for colors RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

# Fonts
START_GAME_FONT = pygame.font.SysFont('comicsansms', 50)
END_GAME_FONT = pygame.font.SysFont('comicsansms', 50)

# Sound Effects
FLAP_SOUND = pygame.mixer.Sound(os.path.join("assets", "flap.wav"))
CRASH_SOUND = pygame.mixer.Sound(os.path.join("assets", "sfx_die.ogg"))
SCORE_SOUND = pygame.mixer.Sound(os.path.join("assets", "score.wav"))

# Background Image
BACKGROUND_IMAGE = pygame.image.load(os.path.join("assets", "background.png")).convert_alpha()
BASE = pygame.image.load(os.path.join("assets", "base.png")).convert_alpha()

# Image Sprites
# player1Image = pygame.image.load(os.path.join("assets", "1.png")).convert_alpha()

# Load the sprite images for animation
image_sprite = [
    pygame.image.load(os.path.join("assets", "1.png")).convert_alpha(),
    pygame.image.load(os.path.join("assets", "2.png")).convert_alpha(),
    pygame.image.load(os.path.join("assets", "3.png")).convert_alpha(),
    pygame.image.load(os.path.join("assets", "4.png")).convert_alpha(),
    pygame.image.load(os.path.join("assets", "5.png")).convert_alpha(),
    pygame.image.load(os.path.join("assets", "6.png")).convert_alpha()
]


# We use the frame variable to iterate through the image_sprite list.
frame_value = 0
# base scroll variables
base_scroll = 0
scroll_speed = 4

# Obstacle Image
OBSTACLE_SURFACE = pygame.image.load(os.path.join("assets", "pipe.png"))


# resize images
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SCREENWIDTH, SCREENHEIGHT))
BASE = pygame.transform.scale(BASE, (SCREENWIDTH, SCREENHEIGHT))
OBSTACLE_SURFACE = pygame.transform.scale2x(OBSTACLE_SURFACE)
player1ImageWidthHeight = [70, 90]  # set size for player sprite
player1pos = [SCREENWIDTH//2, SCREENHEIGHT//2]    #X,Y for centre

# Obstacle settings
OBSTACLE_GAP = 150
OBSTACLE_FREQUENCY = 1450  # Milliseconds
LAST_OBSTACLE = pygame.time.get_ticks() - OBSTACLE_FREQUENCY
OBSTACLE_WIDTH = 50
obstacle_height = random.randint((SCREENWIDTH//4), (SCREENHEIGHT-10))
OBSTACLE_COLOR = green
obstacle_x_pos = 700
obstacle_x_change_pos = -5
startTime = pygame.time.get_ticks()  # stores current time

moving = False  # check if the bord is moving
gameState = "running"  # controls which state the games is in
# game loop #################### runs 60 times a second!
while gameState != "exit":  # game loop - note:  everything in the mainloop is indented one tab

    # your code starts here ##############################
    clock.tick(FPS)  # setting game fps
    screen.fill(black)
    # Add the background
    screen.blit(BACKGROUND_IMAGE, (0, 0))

    for event in pygame.event.get():  # get user interaction events
        if event.type == pygame.QUIT:  # tests if window's X (close) has been clicked
            gameState = "exit"  # causes exit of game loop
            sys.exit()

    # Storing keys pressed in a new variable using key.get_pressed() method
    keys = pygame.key.get_pressed()

    # Changing the y-coordinate of the player and setting moving variable to true
    if keys[K_UP] or keys[K_SPACE]:
        if not player1pos[1] < 0:
            player1pos[1] -= 10
            moving = True
            FLAP_SOUND.play()

    if keys[KEYDOWN]:
        player1pos[1] += 10
        moving = True

    if moving:
        frame_value += 1
        # screen.blit(player1Image, (player1pos[0], player1pos[1]))

    # reset the frame to zero if its value is greater than
    # the list length.
    if frame_value > len(image_sprite):
        frame_value = 0

    # Add scrolling effect to the base
    # screen.blit(BASE, (base_scroll, 768))
    # base_scroll -= scroll_speed
    # if abs(base_scroll) > 70:
    #     base_scroll = 0

    # draw the player
    player1Image = image_sprite[frame_value]  # load player1 image into a variable
    player1Image = pygame.transform.scale(player1Image, player1ImageWidthHeight)  # modifies size/scale of the image
    screen.blit(player1Image, (player1pos[0], player1pos[1]))
    pygame.display.update()  # Update the surface

    # draw the obstacles
    pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x_pos, 0, OBSTACLE_WIDTH, obstacle_height))
    bottom_obstacle_height = 535 - obstacle_height - 150//2
    pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x_pos, 535, OBSTACLE_WIDTH, bottom_obstacle_height))

    # move the obstacles
    obstacle_x_pos += obstacle_x_change_pos

    # generate new obstacle
    if obstacle_x_pos <= -10:
        obstacle_x_pos = 200
        obstacle_height = random.randint(150, 550)

    pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x_pos, 0, OBSTACLE_WIDTH, obstacle_height))
    bottom_obstacle_height = 535 - obstacle_height - 150//2
    pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x_pos, 535, OBSTACLE_WIDTH, bottom_obstacle_height))

    # move the player
    # player1pos[1] += 5

    # detect a collision
    if 50 <= obstacle_x_pos <= (100 + 70):
        if player1pos[1] <= obstacle_height or player1pos[1] >= (bottom_obstacle_height - 70):
            display_content = END_GAME_FONT.render("GAME OVER!", True, red)
            screen.blit(display_content, (250, 150))
            CRASH_SOUND.play()
            # pygame.quit()

    # your code ends here ###############################
    pygame.display.flip()  # transfers build screen to human visible screen
    # clock.tick(FPS)  # limits game to frame per second, FPS value
    

# out of game loop ###############

print("The game has closed")  # notifies user the game has ended
pygame.quit()   # stops the game engine
sys.exit()  # close operating system window
