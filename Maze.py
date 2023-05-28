
class Maze:
    def __init__(self):
        self.maze = self.generate()

    def generate(self):
        return [[1, 1, 1, 1, 1],
                [0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1]]
