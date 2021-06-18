import pygame
from pygame.locals import *
from time import sleep
from random import choice, randint
from snake_terminal import Snake as SnakeTerminal
from snake_terminal import Apple
from setting import *

class Snake(SnakeTerminal):
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.default_snake_len = len(init_body)
        self.direction = init_direction
    def backward_direction(self, backward_direction):
        x, y = self.direction
        return True if backward_direction == (0 - x, 0 - y) else False

class App():
    def __init__(self) -> None:
        '''
        Set status is running
        Set size of app is tuple
        '''
        self._running = True
        self._display_surf = None
        self._size = self.width, self.height = BOARD_SIZE
        self._clock = pygame.time.Clock()
        
    def on_init(self):
        '''
            Start app by pygame init
            Create a window of board with size
        '''
        pygame.init()
        self._running = True
        self._display_surf = pygame.display.set_mode(BOARD_SIZE)
        self._point = 0
        self._game_over = False
        self._snake = Snake(INIT_SNAKE_BODY, INIT_SNAKE_DIRECTION)
        self._apple_coordinates = Apple(MAX_X_AXIS, MAX_Y_AXIS, INIT_SNAKE_BODY).random()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if not self._game_over:
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and not self._snake.backward_direction(HEAD_UP):
                    self._snake.take_direction(HEAD_UP)
                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and not self._snake.backward_direction(HEAD_DOWN):
                    self._snake.take_direction(HEAD_DOWN)
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and not self._snake.backward_direction(HEAD_LEFT):
                    self._snake.take_direction(HEAD_LEFT)
                elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and not self._snake.backward_direction(HEAD_RIGHT):
                    self._snake.take_direction(HEAD_RIGHT)
            else:
                self.on_init()

    def on_loop(self):
        def next_coordinates():
            '''
            when the snake'head ends up wall, it will appear in other side.
            '''
            x_step, y_step = self._snake.direction
            x, y = self._snake.head()
            x = (x + x_step) % MAX_X_AXIS
            y = (y + y_step) % MAX_Y_AXIS
            return (x, y)
        if self._snake.head() in self._snake.body[:-1]:
            ''' the snake's head hits body '''
            self._game_over = True
        else:
            '''if game is not over, did the snake eat apple? and make a move'''
            if self._apple_coordinates == self._snake.head():
                self._apple_coordinates = Apple(MAX_X_AXIS, MAX_Y_AXIS, INIT_SNAKE_BODY).random()
                self._snake.body.insert(0, self._snake.body[0])
                self._point += 1
                print(self._point)
            self._snake.take_step(next_coordinates())

    def on_render(self, corner):
        self._display_surf.fill(WHITE)

        for body_coordinates in self._snake.body[:-1]:
            x, y = body_coordinates
            self._display_surf.blit(SNAKE_BODY, (corner.x + x * PIXEL_WIDTH, corner.y + y * PIXEL_HEIGHT))
        x, y = self._snake.head()
        self._display_surf.blit(SNAKE_HEAD, (corner.x + x * PIXEL_WIDTH, corner.y + y * PIXEL_HEIGHT))
        x, y = self._apple_coordinates
        self._display_surf.blit(APPLE, (corner.x + x * PIXEL_WIDTH, corner.y + y * PIXEL_HEIGHT))

        pygame.display.update()
        
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        corner = pygame.Rect(0, 0, PIXEL_WIDTH, PIXEL_HEIGHT)
        if self.on_init() == False:
            self._running = False
        while self._running:
            self._clock.tick(FPS)
            while not self._game_over and self._running:
                for event in pygame.event.get():
                    self.on_event(event)
                self.on_loop()
                self.on_render(corner)
                sleep(0.1)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render(corner)

        self.on_cleanup()

if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
    print('Game over!')