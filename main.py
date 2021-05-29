class Snake():
    '''
     y
    ^                UP
    |              (0, 1)
    |             +------+    RIGHT
    |     (-1, 0) | HEAD |    (1, 0) 
    |      LEFT   +------+
    |              (0, -1)
    |               DOWN
    |(0, 0)
    +---------------------------------> x                     
    '''
    def __init__(self, initBody, initDirection):
        # body is a list [(x1, y1), (x2, y2), (x3, y3),...] body of snake
        # direction is a tuple (x, y) where snake heads to 
        self.body = initBody
        self.direction = initDirection
    def takeStep(self, position):
        # position should be a point with (x, y)
        self.body = self.body[1:] + position
    def setDirection(self, direction):
        self.direction = direction
    def head(self):
        return self.body[-1]
class Apple():
    pass
class Game():
    def __init__(self, width, height, body, direction):
        self.width = width
        self.height = height
        self.snake = Snake(body, direction)

    def boardMatrix(self):
        matrix = [[' ' for y in range(self.height)] for x in range(self.width)]
        for y, row in enumerate(matrix):
            for x in range(self.width):
                if (x, y) == self.snake.head():
                    matrix[y][x] = 'x'
                elif (x, y) in self.snake.body:
                    matrix[y][x] = 'o'
        return matrix

    def render(self):
        print(f'Board size width x height is {self.width} x {self.height}')
        print('Game on!')

        matrix = self.boardMatrix()
        
        border_top_bottom = ''.join(['+', '-' * self.width, '+'])
        print(border_top_bottom)
        for row in matrix:
            row = ['|'] + row + ['|']
            print(''.join(row))
        print(border_top_bottom)
        


def main():
    up = (0,1)
    body = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3)]
    game = Game(20, 20, body, up)
    game.render()

if __name__ == '__main__':
    main()