from time import sleep
from random import choice
class Snake():
    '''
    +---------------------------------> x 
    |(0, 0)
    |                UP
    |              (0, -1)
    |             +------+    RIGHT
    |     (-1, 0) | HEAD |    (1, 0) 
    |      LEFT   +------+
    |              (0, 1)
    |               DOWN
    |
    + y                    
    '''
    def __init__(self, initBody, initDirection):
        # body is a list [(x1, y1), (x2, y2), (x3, y3),...] body of snake
        # direction is a tuple (x, y) where snake heads to 
        self.body = initBody
        self.direction = initDirection
    def take_step(self, position):
        # position should be a point with (x, y)
        self.body = self.body[1:] + [position]
    def take_direction(self, direction):
        self.direction = direction
    def head(self):
        return self.body[-1]
    def set_new_head(self, width, height):
        x_step, y_step = self.direction
        x, y = self.head()
        x = (x + x_step) % width
        y = (y + y_step) % height
        return((x, y))   

class Apple():
    pass
class Game():
    def __init__(self, width, height, body, direction):
        self.width = width
        self.height = height
        self.snake = Snake(body, direction)

    def board_matrix(self):
        matrix = [[' ' for y in range(self.height)] for x in range(self.width)]
        for y, row in enumerate(matrix):
            for x in range(self.width):
                if (x, y) == self.snake.head():
                    matrix[y][x] = 'x'
                elif (x, y) in self.snake.body:
                    matrix[y][x] = 'o'
        return matrix

    def render(self):
        # print(f'Board size width x height is {self.width} x {self.height}')
        print('Game on!')

        matrix = self.board_matrix()
        border_top_bottom = ''.join(['+', '-' * self.width, '+'])
        print(border_top_bottom)
        for row in matrix:
            row = ['|'] + row + ['|']
            print(''.join(row))
        print(border_top_bottom)
        


def main():
    width = 20
    height = 20
    body = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
    directions_mapping = {(1, 0): 'right', (0, 1): 'down', (-1, 0): 'left', (0, -1): 'up'}
    direction = (1, 0)

    game = Game(width, height, body, direction)

    def n_step(number_steps):
        for step in range(int(number_steps)):
            game.render()
            sleep(0.1)
            new_head = game.snake.set_new_head(game.width, game.height)
            game.snake.take_step(new_head)
        

    while True:
        game.snake.take_direction(direction)
        n_step(5)        
        x, y = direction
        opposite_direction = (0 - x, 0 - y)
        turns = list(directions_mapping.keys()).copy()
        turns.remove(opposite_direction)
        direction = choice(turns)
        print('turn', directions_mapping.get(direction))
        
if __name__ == '__main__':
    main()