class Mouse:
    def __init__(self, Maze, x, y, direction):
        self.Maze = Maze
        self.x = x
        self.y = y
        self.direction = direction  # 0,1,2,3 -> up,right,down,left

    def Move(self):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1

    def Rotate(self, isClockwise):
        if (isClockwise):
            self.direction += 1
        else:
            self.direction -= 1
        self.direction %= 4
