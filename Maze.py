
class Maze:
    def __init__(self):
        self.maze = self.generate()

    def generate(self):
        return [[1, 1, 1, 1, 1],
                [1, 2, 1, 3, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]]

    def FindStart(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 2:
                    return (i, j)

    def FindEnd(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 3:
                    return (i, j)
