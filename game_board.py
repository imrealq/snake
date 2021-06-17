import pygame
from pygame.locals import *
import os

BOARD_SIZE = (400, 400)
FPS = 60
WHITE = (255, 255, 255)
GREEN_DOT_IMG = pygame.image.load(os.path.join('assets', 'green_dot.png'))
RED_DOT_IMG = pygame.image.load(os.path.join('assets', 'red_dot.png'))
BLACK_DOT_IMG = pygame.image.load(os.path.join('assets', 'blue_dot.png'))
PIXEL_WIDTH, PIXEL_HEIGHT = 15, 15
SNAKE_BODY = pygame.transform.scale(GREEN_DOT_IMG, (PIXEL_WIDTH, PIXEL_HEIGHT))
SNAKE_HEAD = pygame.transform.scale(BLACK_DOT_IMG, (PIXEL_WIDTH, PIXEL_HEIGHT))
APPLE = pygame.transform.scale(RED_DOT_IMG, (PIXEL_WIDTH, PIXEL_HEIGHT))

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

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self, pos):
        self._display_surf.fill(WHITE)
        self._display_surf.blit(SNAKE_BODY, (pos.x, pos.y))
        self._display_surf.blit(SNAKE_HEAD, (pos.x + PIXEL_WIDTH, pos.y))
        self._display_surf.blit(APPLE, (pos.x + 200, pos.y + 200))

        pygame.display.update()
        
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        pos = pygame.Rect(0, 0, PIXEL_WIDTH, PIXEL_HEIGHT)
        if self.on_init() == False:
            self._running = False
        while self._running:
            self._clock.tick(FPS)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render(pos)
        self.on_cleanup()

if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
    print('Game over!')