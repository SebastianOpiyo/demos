
# import pygame
# from pygame.locals import * #Basic Pygame Imports
import os


NAME = "patrick"
FPS = 32



SCREENWIDTH = 289
SCREENHEIGHT = 511
# SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'resources\SPRITES\\bird.png'
BACKGROUND = 'resources\SPRITES\\bg.jpeg'
PIPE = 'resources\SPRITES\pipe.png '

# loading images

print(os.path.join('Assets', '1.png'))



def main(name):
    print(name)


def dance(a, b):
    print(a + b)

main(NAME)
dance(3, 4)

# if __name__ == "__main__":
#     main()
#     dance()
 