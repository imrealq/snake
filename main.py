'''
+---------------------------------> x 
|(0, 0)
|              (W) UP
|             (0, -1)
|             +------+  (D) RIGHT
|     (-1, 0) | HEAD |   (1, 0) 
|    (A) LEFT +------+
|              (0, 1)
|             (S) DOWN
|
+ y                    
'''
from time import sleep
from random import choice, randint
class Snake():
    def __init__(self, init_body, init_direction, init_speed):
        # body is a list [(x1, y1), (x2, y2), (x3, y3),...] body of snake
        # direction is a tuple (x, y) where snake heads to 
        self.body = init_body
        self.default_snake_len = len(init_body)
        self.direction = init_direction
        self.speed = init_speed
    def take_step(self, position):
        # position should be a point with (x, y)
        self.body = self.body[1:] + [position]
    def take_direction(self, direction):
        self.direction = direction
    def head(self):
        return self.body[-1]

class Apple():
    def __init__(self, width, height, snake_body):
        self.width = width
        self.height = height
        self.snake_body = snake_body
    def random(self):
        self.x = randint(0, self.width - 1)
        self.y = randint(0, self.height - 1)
        if (self.x, self.y) not in self.snake_body:
            return (self.x, self.y)
        else:
            return self.random()
class Game():
    def __init__(self, width, height, body, direction, speed=1):
        self.width = width
        self.height = height
        self.snake = Snake(body, direction, speed)
        self.random_position = Apple(self.width, self.height, self.snake.body).random()
        self.x_apple, self.y_apple = self.random_position
        self.points = 0
        self.directions_mapping = {(1, 0): 'right', (0, 1): 'down', (-1, 0): 'left', (0, -1): 'up'}

    def snake_eats_apple(self):
        if (self.x_apple, self.y_apple) == self.snake.head():
            self.x_apple, self.y_apple = self.random_position
            self.snake.body.insert(0, self.snake.body[0])
            self.points = len(self.snake.body) - self.snake.default_snake_len

    def is_game_over(self):
        if self.snake.head() in self.snake.body[:-1]:
            return True
        else:
            return False
    def board_matrix(self):
        matrix = [[' ' for y in range(self.height)] for x in range(self.width)]
        
        self.snake_eats_apple()
        matrix[self.y_apple][self.x_apple] = '*'            
        for y, row in enumerate(matrix):
            for x in range(self.width):
                if (x, y) == self.snake.head():
                    matrix[y][x] = 'x'
                elif (x, y) in self.snake.body:
                    matrix[y][x] = 'o'
        return matrix

    def render(self):
        # print(f'Board size width x height is {self.width} x {self.height}')
        print(f"Game on! Current snake'head directions is {self.directions_mapping.get(self.snake.direction)}")
        print(f"position of apple is {self.x_apple, self.y_apple}")
        matrix = self.board_matrix()
        border_top_bottom = ''.join(['+', '-' * self.width, '+'])
        print(border_top_bottom)
        for row in matrix:
            row = ['|'] + row + ['|']
            print(''.join(row))
        print(border_top_bottom)
    
    # when the snake'head ends up wall, it will appear in other side.
    def render_one_step(self):
        x_step, y_step = self.snake.direction
        x, y = self.snake.head()
        x = (x + x_step) % self.width
        y = (y + y_step) % self.height
        return((x, y))       
    
    def render_continuos_steps(self):
        self.render()
        new_head = self.render_one_step()
        self.snake.take_step(new_head)
        sleep(self.snake.speed)

    # return three directions are not oppiste snake's head one
    def possible_directions(self):
        x, y = self.snake.direction
        opposite_direction = (0 - x, 0 - y)
        directions = list(self.directions_mapping.keys())
        directions.remove(opposite_direction)
        return directions

def main():
    # table_size = input(
    #     '''
    #     Pick table size
    #     1) 8 x 8
    #     2) 12 x 12
    #     3) 15 x 15
    #     '''
    # )
    # if table_size == 1:
    #     width_x_height = (8, 8)
    # elif table_size == 2:
    #     width_x_height = (12, 12)
    # else:
    #     width_x_height = (15, 15)
    width_x_height = (3, 3)
    width, height = width_x_height
    body = [(0, 0), (1, 0), (2, 0)]
    direction = (1, 0)
    speed = 0.2

    game = Game(width, height, body, direction, speed=speed)
    
    try:
        while True:
            if not game.is_game_over():
                for i in range(randint(1,20)):
                    print(f'Points: {game.points}')
                    if not game.is_game_over():
                        game.render_continuos_steps()
                    else:
                        break
                direction = choice(game.possible_directions())
                game.snake.take_direction(direction)
            else:
                print('Game over!')
                break
    except KeyboardInterrupt:
        print('Game over!') 

        
if __name__ == '__main__':
    main()