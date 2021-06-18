import pygame
from pygame.locals import *
from time import sleep
from snake_terminal import Snake as SnakeTerminal
from setting import *

class Snake(SnakeTerminal):
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.default_snake_len = len(init_body)
        self.direction = init_direction

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
        self.snake = Snake(INIT_SNAKE_BODY, INIT_SNAKE_DIRECTION)

    def on_init(self):
        '''
            Start app by pygame init
            Create a window of board with size
        '''
        pygame.init()
        self._running = True
        self._display_surf = pygame.display.set_mode(BOARD_SIZE)

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        def next_coordinates():
            '''
            when the snake'head ends up wall, it will appear in other side.
            '''
            x_step, y_step = self.snake.direction
            x, y = self.snake.head()
            x = (x + x_step) % MAX_X_AXIS
            y = (y + y_step) % MAX_Y_AXIS
            return (x, y)
        self.snake.take_step(next_coordinates())

    def on_render(self, corner):
        self._display_surf.fill(WHITE)

        for body_coordinates in self.snake.body[:-1]:
            x, y = body_coordinates
            self._display_surf.blit(SNAKE_BODY, (corner.x + x * PIXEL_WIDTH, corner.y + y * PIXEL_HEIGHT))
        x, y = self.snake.head()
        self._display_surf.blit(SNAKE_HEAD, (corner.x + x * PIXEL_WIDTH, corner.y + y * PIXEL_HEIGHT))
        
        self._display_surf.blit(APPLE, (corner.x + 200, corner.y + 200))

        pygame.display.update()
        
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        corner = pygame.Rect(0, 0, PIXEL_WIDTH, PIXEL_HEIGHT)
        if self.on_init() == False:
            self._running = False
        while self._running:
            self._clock.tick(FPS)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render(corner)
            sleep(0.5)
        self.on_cleanup()

if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
    print('Game over!')