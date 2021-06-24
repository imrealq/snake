from time import sleep
from pygame import time
from setting import *
from snake_terminal import Snake, Apple
import sql


class Snake(Snake):
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.default_snake_len = len(init_body)
        self.direction = init_direction


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
        self._screen = "intro"
        self._player = ""
        self._snake = Snake(INIT_SNAKE_BODY, INIT_SNAKE_DIRECTION)
        self._apple_coordinates = Apple(
            MAX_X_AXIS, MAX_Y_AXIS, self._snake.body
        ).random()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if self._screen == "intro":
                self._screen = "input name"
            elif self._screen == "input name":
                if event.key == pygame.K_BACKSPACE:
                    self._player = self._player[:-1]
                elif event.key in LIST_ALLOW_INPUT_KEY and len(self._player) < 12:
                    self._player += event.unicode
                elif event.key == pygame.K_RETURN and self._player:
                    self._player = self._player[:12]
                    self._screen = "playing"
            elif self._screen == "playing":
                if event.key in MOVE_UP and self._snake.direction != HEAD_DOWN:
                    self._snake.take_direction(HEAD_UP)
                elif event.key in MOVE_DOWN and self._snake.direction != HEAD_UP:
                    self._snake.take_direction(HEAD_DOWN)
                elif event.key in MOVE_LEFT and self._snake.direction != HEAD_RIGHT:
                    self._snake.take_direction(HEAD_LEFT)
                elif event.key in MOVE_RIGHT and self._snake.direction != HEAD_LEFT:
                    self._snake.take_direction(HEAD_RIGHT)
            elif self._screen == "game over":
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

        if self._screen == "playing":
            if self._snake.head() in self._snake.body[:-1]:
                """ the snake's head hits body """
                player_id = sql.get_player_id(self._player)
                sql.insert_game_score(self._point, player_id)
                self._screen = "game over"
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
        self._display_surf.fill(BLACK)
        board = pygame.draw.rect(self._display_surf, WHITE, BOARD)
        information = " ".join(
            ["POINTS:", str(self._point), "   ", "PLAYER:", self._player]
        )
        self._display_surf.blit(FONT.render(information, 1, GREEN), (RIGHT, 3))

        def snake_and_apple():
            coordinates_to_pixel = lambda coordinates: (
                CORNER.x + coordinates[0] * PIXEL_WIDTH,
                CORNER.y + coordinates[1] * PIXEL_HEIGHT,
            )
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
            pop_up = pygame.draw.rect(self._display_surf, RED, POP_UP)
            self._display_surf.blit(
                GAME_OVER_FONT.render("GAME OVER!", 1, WHITE),
                (pop_up.x + 20, pop_up.y + 15),
            )
            self._display_surf.blit(
                GAME_OVER_FONT.render("Points: " + str(self._point), 1, WHITE),
                (pop_up.x + 40, pop_up.x + 65),
            )

        def menu():
            pop_up = pygame.draw.rect(self._display_surf, GREEN, POP_UP)
            self._display_surf.blit(
                MENU_FONT.render("NEW GAME", 1, WHITE), (pop_up.x + 25, pop_up.y + 15)
            )
            self._display_surf.blit(
                MENU_FONT.render("Press any keys", 1, WHITE),
                (pop_up.x + 4, pop_up.y + 50),
            )

        def input_player_name():
            input_field = pygame.draw.rect(self._display_surf, GRAY, INPUT_FIELD_NAME)
            self._display_surf.blit(
                FONT.render("Input your name", 1, GREEN),
                (input_field.x + 18, input_field.y + 10),
            )
            self._display_surf.blit(
                FONT.render(self._player, 1, GREEN),
                (input_field.x + 18, input_field.y + 40),
            )

        if self._screen == "intro":
            menu()
        if self._screen == "input name":
            input_player_name()
        elif self._screen == "playing":
            snake_and_apple()
            sleep(0.075)
        elif self._screen == "game over":
            popup_game_over()
            sleep(0.75)

        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while self._running:
            self._clock.tick(FPS)
            self.on_render()
            self.on_loop()
            for event in pygame.event.get():
                self.on_event(event)
        self.on_cleanup()


if __name__ == "__main__":
    sql.init_db()
    theApp = App()
    theApp.on_execute()
    print("Game over!")
