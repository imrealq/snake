from time import sleep
from pygame import time
from setting import *
from snake_terminal import Snake, Apple


class Snake(Snake):
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.default_snake_len = len(init_body)
        self.direction = init_direction

    def backward_direction(self, backward_direction):
        x, y = self.direction
        return True if backward_direction == (0 - x, 0 - y) else False


class App:
    def __init__(self) -> None:
        """
        Set status is running
        Set size of app is tuple
        """
        self._running = True
        self._display_surf = None
        self._clock = pygame.time.Clock()

    def on_init(self):
        """
            Start app by pygame init
            Create a window of board with size
        """
        pygame.init()
        self._running = True
        self._display_surf = pygame.display.set_mode(WINDOW_SIZE)
        self._point = 0
        self._game_over = False
        self._game_start = False
        self._snake = Snake(INIT_SNAKE_BODY, INIT_SNAKE_DIRECTION)
        self._apple_coordinates = Apple(
            MAX_X_AXIS, MAX_Y_AXIS, self._snake.body
        ).random()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            self._game_start = True
            if not self._game_over:
                if (
                    event.key == pygame.K_w or event.key == pygame.K_UP
                ) and not self._snake.backward_direction(HEAD_UP):
                    self._snake.take_direction(HEAD_UP)
                elif (
                    event.key == pygame.K_s or event.key == pygame.K_DOWN
                ) and not self._snake.backward_direction(HEAD_DOWN):
                    self._snake.take_direction(HEAD_DOWN)
                elif (
                    event.key == pygame.K_a or event.key == pygame.K_LEFT
                ) and not self._snake.backward_direction(HEAD_LEFT):
                    self._snake.take_direction(HEAD_LEFT)
                elif (
                    event.key == pygame.K_d or event.key == pygame.K_RIGHT
                ) and not self._snake.backward_direction(HEAD_RIGHT):
                    self._snake.take_direction(HEAD_RIGHT)
            else:
                self.on_init()

    def on_loop(self):
        def next_coordinates():
            """
            when the snake'head ends up wall, it will appear in other side.
            """
            x_step, y_step = self._snake.direction
            x, y = self._snake.head()
            x = (x + x_step) % MAX_X_AXIS
            y = (y + y_step) % MAX_Y_AXIS
            return (x, y)

        if self._snake.head() in self._snake.body[:-1]:
            """ the snake's head hits body """
            self._game_over = True
        else:
            """if game is not over, did the snake eat apple? and make a move"""
            if self._apple_coordinates == self._snake.head():
                self._apple_coordinates = Apple(
                    MAX_X_AXIS, MAX_Y_AXIS, self._snake.body
                ).random()
                self._snake.body.insert(0, self._snake.body[0])
                self._point += 1
            self._snake.take_step(next_coordinates())

    def on_render(self):
        coordinates_to_pixel = lambda coordinates: (
            CORNER.x + coordinates[0] * PIXEL_WIDTH,
            CORNER.y + coordinates[1] * PIXEL_HEIGHT,
        )

        def snake_and_apple():
            for body_coordinates in self._snake.body[:-1]:
                self._display_surf.blit(
                    SNAKE_BODY, coordinates_to_pixel(body_coordinates)
                )
            self._display_surf.blit(
                SNAKE_HEAD, coordinates_to_pixel(self._snake.head())
            )
            self._display_surf.blit(
                APPLE, coordinates_to_pixel(self._apple_coordinates)
            )

        def popup_game_over():
            pygame.draw.rect(self._display_surf, RED, POP_UP)
            self._display_surf.blit(
                GAME_OVER_FONT.render(" GAME OVER! ", 1, WHITE),
                (BOARD.centerx // 2, BOARD.centery // 2),
            )
            self._display_surf.blit(
                FONT.render("      Score: " + str(self._point), 1, WHITE),
                (BOARD.centerx // 2, BOARD.centery // 2 + 50),
            )

        def menu():
            pygame.draw.rect(self._display_surf, GREEN, POP_UP)
            self._display_surf.blit(
                MENU_FONT.render("  NEW GAME  ", 1, WHITE),
                (BOARD.centerx // 2, BOARD.centery // 2 + 10),
            )
            self._display_surf.blit(
                FONT.render("  Press any keys ", 1, WHITE),
                (BOARD.centerx // 2, BOARD.centery // 2 + 50),
            )

        self._display_surf.fill(BLACK)
        pygame.draw.rect(self._display_surf, WHITE, BOARD)
        self._display_surf.blit(
            FONT.render("SCORE: " + str(self._point), 1, GREEN), (0, 0)
        )

        (
            popup_game_over() if self._game_over else snake_and_apple()
        ) if self._game_start else menu()

        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while self._running:
            self._clock.tick(FPS)
            self.on_render()  # render menu
            if self._game_start:
                while not self._game_over and self._running:
                    for event in pygame.event.get():
                        self.on_event(event)
                    self.on_loop()
                    self.on_render()  # snake_and_apple
                    sleep(0.1)
                self.on_render()  # popup_game_over
            for event in pygame.event.get():
                self.on_event(event)
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
    print("Game over!")