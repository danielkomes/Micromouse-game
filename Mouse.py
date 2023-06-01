import pygame
import Exceptions


class Mouse:

    def __init__(self, maze, x, y, direction, window):
        self.__maze = maze
        self.__x = x
        self.__y = y
        self.__direction = direction  # 0,1,2,3 -> up,right,down,left
        self.__window = window
        self.__image = pygame.image.load("bird.png")
        self.delay = 16
        self.__redraw(window, maze)

    def getPos(self):
        return (round(self.__y), round(self.__x))

    def Move(self):
        lerp = 0
        for i in range(60):
            lerp = (1/60)
            if self.__direction == 0:
                self.__y -= lerp
            elif self.__direction == 1:
                self.__x += lerp
            elif self.__direction == 2:
                self.__y += lerp
            elif self.__direction == 3:
                self.__x -= lerp
            self.__redraw(self.__window, self.__maze)
            currentY = round(self.__y)
            currentX = round(self.__x)
            if self.__maze.maze[currentY][currentX] == 1:
                raise Exceptions.Lose
            pygame.time.delay(self.delay)

    def Rotate(self, isClockwise):
        if (isClockwise):
            self.__direction += 1
        else:
            self.__direction -= 1
        self.__direction %= 4
        self.__redraw(self.__window, self.__maze)

    def SensorForward(self):
        ret = False
        if self.__direction == 0:
            ret = self.__maze.maze[self.__y-1][self.__x] == 1
        elif self.__direction == 1:
            ret = self.__maze.maze[self.__y][self.__x + 1] == 1
        elif self.__direction == 2:
            ret = self.__maze.maze[self.__y + 1][self.__x] == 1
        elif self.__direction == 3:
            ret = self.__maze.maze[self.__y][self.__x - 1] == 1
        return ret

    def __drawMaze(self, window, maze):
        tileSizeX = self.__window.get_width()/len(self.__maze.maze[0])
        tileSizeY = self.__window.get_height()/len(self.__maze.maze)
        for i in range(len(self.__maze.maze)):
            for j in range(len(self.__maze.maze[0])):
                if self.__maze.maze[i][j] == 1:
                    pygame.draw.rect(
                        self.__window,
                        (100, 100, 100),
                        (j * tileSizeX, i*tileSizeY, tileSizeX, tileSizeY))
                elif self.__maze.maze[i][j] == 2:
                    pygame.draw.rect(
                        self.__window,
                        (0, 200, 0),
                        (j * tileSizeX, i*tileSizeY, tileSizeX, tileSizeY))
                elif self.__maze.maze[i][j] == 3:
                    pygame.draw.rect(
                        self.__window,
                        (200, 0, 0),
                        (j * tileSizeX, i*tileSizeY, tileSizeX, tileSizeY))

    def __drawMouse(self, window, maze):
        tileSizeX = self.__window.get_width()/len(self.__maze.maze[0])
        tileSizeY = self.__window.get_height()/len(self.__maze.maze)
        pos = (self.__x * tileSizeX + tileSizeX / 4,
               self.__y * tileSizeY + tileSizeY / 4)
        size = (tileSizeX/2, tileSizeY/2)
        tempImage = pygame.transform.scale(self.__image, size)
        tempImage = pygame.transform.rotate(tempImage, -90 * self.__direction)
        self.__window.blit(tempImage, pos)

    def __redraw(self, window, maze, rect=None):
        # pygame.time.delay(self.delay)
        self.__window.fill((0, 0, 0))
        self.__drawMaze(window, maze)
        self.__drawMouse(window, maze)
        if rect:
            x = rect[0]
            y = rect[1]
            w = rect[2]
            h = rect[3]
            pygame.display.update(x, y, w, h)
        else:
            pygame.display.flip()
