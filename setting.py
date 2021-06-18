import os
import pygame
from pygame.locals import *

BOARD_SIZE = BOARD_SIZE_WIDTH, BOARD_SIZE_HEIGHT = (405, 405)
FPS = 60
WHITE = (255, 255, 255)
GREEN_DOT_IMG = pygame.image.load(os.path.join('assets', 'green_dot.png'))
RED_DOT_IMG = pygame.image.load(os.path.join('assets', 'red_dot.png'))
BLACK_DOT_IMG = pygame.image.load(os.path.join('assets', 'blue_dot.png'))
PIXEL_WIDTH, PIXEL_HEIGHT = 15, 15
MAX_X_AXIS, MAX_Y_AXIS = BOARD_SIZE_WIDTH // PIXEL_WIDTH, BOARD_SIZE_HEIGHT // PIXEL_HEIGHT
SNAKE_BODY = pygame.transform.scale(GREEN_DOT_IMG, (PIXEL_WIDTH, PIXEL_HEIGHT))
SNAKE_HEAD = pygame.transform.scale(BLACK_DOT_IMG, (PIXEL_WIDTH, PIXEL_HEIGHT))
APPLE = pygame.transform.scale(RED_DOT_IMG, (PIXEL_WIDTH, PIXEL_HEIGHT))
INIT_SNAKE_BODY = [(0,0), (1, 0), (2, 0), (3, 0)]
INIT_SNAKE_DIRECTION = (1, 0)
HEAD_UP = (0, -1)
HEAD_DOWN = (0, 1)
HEAD_RIGHT = (1, 0)
HEAD_LEFT = (-1, 0)