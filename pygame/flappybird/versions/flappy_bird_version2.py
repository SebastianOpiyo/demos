# Add bird


import pygame  # accesses pygame files
import sys  # to communicate with windows, i.e sys.exit to quit the game
import os  # to communicate with OS
import random  # To generate random objects
from pygame.locals import *  # Basic pygame imports


# Setting Global Variables
FPS = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 800, 600  # sets size of screen/window
SCREEN = pygame.display.set_mode(SCREENSIZE)  # creates window and game screen
CLOCK = pygame.time.Clock()  # creates clock to limit frames per second

# set variables for colors RGB (0-255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Background Image
BACKGROUND_IMAGE = pygame.image.load(os.path.join("assets", "background.png")).convert_alpha()
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SCREENWIDTH, SCREENHEIGHT))

# Bird
BIRD_IMAGE = pygame.image.load(os.path.join("assets", "1.png")).convert_alpha()
bird_width_height = [75, 100]  # set size for player sprite
BIRD_IMAGE = pygame.transform.scale(BIRD_IMAGE, bird_width_height)  # modifies size of image
bird_x_position, bird_y_position = SCREENWIDTH//2, SCREENHEIGHT//2    # bird x,y position at start of the game


def display_bird(x=bird_x_position, y=bird_y_position):
    """Creates the bird image and adds to the screen"""
    SCREEN.blit(BIRD_IMAGE, (x, y))


def create_screen():
    """Creates the screen surface for the game"""
    SCREEN.fill(BLACK)
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
    pygame.display.set_caption("Flappy Bird by Patto!")
    display_bird(50, 100)  # Call the create bird function, with or without parameters
    pygame.display.update()
    CLOCK.tick(FPS)


def main():
    """Runs the game"""
    game_state = "running"  # controls which state the games is in

    while game_state != "exit":
        create_screen()
        # display_bird(bird_x_position, bird_y_position)
        for event in pygame.event.get():  # get user interaction events
            # if user clicks X (close) on the window, close the game
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                game_state = "exit"  # causes exit of game loop
                pygame.quit()
                sys.exit()

            else:
                pass


if __name__ == "__main__":
    pygame.init()  # Initializing pygame modules
    main()