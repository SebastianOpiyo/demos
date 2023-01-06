# Version4 : Bird movement

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
bird_move_y_cord = 0  # Moves horizontally

# Pipe Images
PIPE_SURFACE = pygame.image.load(os.path.join("assets", "pipe.png"))
PIPE_SURFACE = pygame.transform.scale2x(PIPE_SURFACE)

# Obstacles
OBSTACLE_WIDTH = 70
obstacle_height = random.randint(50, 500)
OBSTACLE_COLOR = GREEN
obstacle_x_pos = 300
obstacle_x_change_pos = -4


def display_bird(x=bird_x_position, y=bird_y_position):
    SCREEN.blit(BIRD_IMAGE, (x, y))


def display_obstacle(height):
    top_obstacle = pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x_pos, 0, OBSTACLE_WIDTH, height))
    bottom_obstacle_height = 500 - height - 50
    bottom_obstacle = pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x_pos, 500,
                                                                OBSTACLE_WIDTH, bottom_obstacle_height))
    return top_obstacle, bottom_obstacle


def move_bird(bird_y, bird_move_y):
    # Moves the bird along the y-axis
    bird_y += bird_move_y

    # set movement boundaries for the bird
    if bird_y <= 0:
        bird_y = 0
    elif bird_y >= 500:
        bird_y = 500
    return bird_y


def move_obstacle(obstacle_x_change):
    obstacle_x_change += obstacle_x_change_pos
    return obstacle_x_change


def collision_detector(obstacle):
    pass


def create_screen():
    SCREEN.fill(BLACK)
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
    pygame.display.set_caption("Flappy Bird by Patto!")
    CLOCK.tick(FPS)


def start_game(): pass


def game_over(): pass


def main():
    """Runs the game"""
    game_state = "running"  # controls which state the games is in
    bird_move_y = bird_move_y_cord
    bird_y = bird_y_position
    obstacle_x_change = obstacle_x_change_pos

    while game_state != "exit":
        create_screen()
        # display_bird(bird_x_position, bird_y_position)
        for event in pygame.event.get():  # get user interaction events
            # if user clicks X (close) on the window, close the game
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                game_state = "exit"  # causes exit of game loop
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_move_y = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bird_move_y = 3

        # Move the bird along the y-axis
        bird_y = move_bird(bird_y, bird_move_y)
        # Move the obstacle along the x-axis
        obstacle_x_change = move_obstacle(obstacle_x_change)
        display_bird(bird_x_position, bird_y)
        display_obstacle(obstacle_height)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    pygame.init()  # Initializing pygame modules
    main()