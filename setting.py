import os
import pygame
from pygame.locals import *
import string

pygame.font.init()

# general setting of window and board
BOARD_SIZE = BOARD_SIZE_WIDTH, BOARD_SIZE_HEIGHT = (405, 405)
MARGIN = TOP, RIGHT, BOTTOM, LEFT = 30, 5, 5, 5
WINDOW_SIZE = WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT = (
    BOARD_SIZE_WIDTH + RIGHT + LEFT,
    BOARD_SIZE_HEIGHT + TOP + BOTTOM,
)
PIXEL = PIXEL_WIDTH, PIXEL_HEIGHT = 15, 15
FPS = 60

MAX_X_AXIS, MAX_Y_AXIS = (
    BOARD_SIZE_WIDTH // PIXEL_WIDTH,
    BOARD_SIZE_HEIGHT // PIXEL_HEIGHT,
)
BOARD = pygame.Rect(RIGHT, TOP, BOARD_SIZE_WIDTH, BOARD_SIZE_HEIGHT)
CORNER = pygame.Rect(RIGHT, TOP, PIXEL_WIDTH, PIXEL_HEIGHT)
POP_UP = pygame.Rect(BOARD.centerx // 2, BOARD.centery // 2, BOARD_SIZE_WIDTH // 2, 100)
INPUT_FIELD_NAME = pygame.Rect(
    BOARD.centerx // 2, BOARD.centery // 2, BOARD_SIZE_WIDTH // 2, 80
)

# RGB color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
GRAY = (211, 211, 211)
RED = (255, 0, 0)
# load image and font
GREEN_DOT_IMG = pygame.image.load(os.path.join("assets", "green_dot.png"))
RED_DOT_IMG = pygame.image.load(os.path.join("assets", "red_dot.png"))
BLACK_DOT_IMG = pygame.image.load(os.path.join("assets", "blue_dot.png"))
FONT_SIZE = 20
FONT = pygame.font.Font(os.path.join("fonts", "DejaVuSans.ttf"), FONT_SIZE)
MENU_FONT_SIZE = 26
MENU_FONT = GAME_OVER_FONT = pygame.font.Font(
    os.path.join("fonts", "DejaVuSans.ttf"), MENU_FONT_SIZE
)

# init snake infor
SNAKE_BODY = pygame.transform.scale(GREEN_DOT_IMG, (PIXEL_WIDTH, PIXEL_HEIGHT))
SNAKE_HEAD = pygame.transform.scale(BLACK_DOT_IMG, (PIXEL_WIDTH, PIXEL_HEIGHT))
INIT_SNAKE_BODY = [(0, 0), (1, 0), (2, 0), (3, 0)]
INIT_SNAKE_DIRECTION = (1, 0)
APPLE = pygame.transform.scale(RED_DOT_IMG, (PIXEL_WIDTH, PIXEL_HEIGHT))

# control the snake's head
HEAD_UP = (0, -1)
HEAD_DOWN = (0, 1)
HEAD_RIGHT = (1, 0)
HEAD_LEFT = (-1, 0)

# allow key input
LIST_ALLOW_INPUT_KEY = [
    pygame.key.key_code(char)
    for char in "".join([string.ascii_lowercase, string.digits, "+", "-", "_"])
]
