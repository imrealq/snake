class Snake():
    pass
class Apple():
    pass
class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def boardMatrix(self):
        # TODO: return the matrix
        pass

    def renderBoard(self):
        matrix = self.boardMatrix()
        print(f'Board size width x height is {self.width} x {self.height}')
        # TODO: print the matrix with border board


def main():
    game = Game(5, 5)
    game.renderBoard()
    print('Game on!')

if __name__ == '__main__':
    main()