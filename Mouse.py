import pygame


class Mouse:

    def __init__(self, maze, x, y, direction, window):
        self.maze = maze
        self.x = x
        self.y = y
        self.direction = direction  # 0,1,2,3 -> up,right,down,left
        self.window = window
        self.image = pygame.image.load("bird.png")
        self.delay = 1000

    def Move(self):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1
        self.redraw(self.window, self.maze)
        pygame.time.delay(self.delay)

    def Rotate(self, isClockwise):
        if (isClockwise):
            self.direction += 1
        else:
            self.direction -= 1
        self.direction %= 4
        self.redraw(self.window, self.maze)
        pygame.time.delay(self.delay)

    def SensorForward(self):
        ret = False
        if self.direction == 0:
            ret = self.maze.maze[self.y-1][self.x] == 1
        elif self.direction == 1:
            ret = self.maze.maze[self.y][self.x + 1] == 1
        elif self.direction == 2:
            ret = self.maze.maze[self.y + 1][self.x] == 1
        elif self.direction == 3:
            ret = self.maze.maze[self.y][self.x - 1] == 1
        return ret

    def drawMaze(self, window, maze):
        tileSizeX = self.window.get_width()/len(self.maze.maze[0])
        tileSizeY = self.window.get_height()/len(self.maze.maze)
        for i in range(len(self.maze.maze)):
            for j in range(len(self.maze.maze[0])):
                if self.maze.maze[i][j] == 1:
                    pygame.draw.rect(
                        self.window,
                        (100, 100, 100),
                        (j * tileSizeX, i*tileSizeY, tileSizeX, tileSizeY))

    def drawMouse(self, window, maze):
        tileSizeX = self.window.get_width()/len(self.maze.maze[0])
        tileSizeY = self.window.get_height()/len(self.maze.maze)
        pos = (self.x * tileSizeX + tileSizeX / 4,
               self.y * tileSizeY + tileSizeY / 4)
        size = (tileSizeX/2, tileSizeY/2)

        tempImage = pygame.transform.scale(self.image, size)
        tempImage = pygame.transform.rotate(tempImage, -90 * self.direction)
        self.window.blit(tempImage, pos)

    def redraw(self, window, maze):
        self.window.fill((0, 0, 0))
        self.drawMaze(window, maze)
        self.drawMouse(window, maze)
        pygame.display.update()
