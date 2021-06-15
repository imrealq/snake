import pygame
from pygame.locals import *

class App():
    def on_event(self, event):
        pass
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit
    def on_execute(self):
        self.on_event(None)
        self.on_loop()
        self.on_render()
        self.on_cleanup()

if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
    print('Game on!')