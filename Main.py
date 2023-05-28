import Maze
import Mouse
import Interface

import pygame
import tkinter as tk

image = pygame.image.load("bird.png")
mouse, maze, window = 0, 0, 0


def main():
    width = 500
    window = pygame.display.set_mode((width, width))
    maze = Maze.Maze()
    mouse = Mouse.Mouse(maze, 0, 1, 1, window)
    interface = Interface.MouseBehavior()
    # redraw(window, mouse, maze)

    play = True
    while play:
        # pygame.time.Clock().tick(1)
        interface.Run(mouse, maze)
        # mouse.Move()
        # redraw(window, mouse, maze)
        # pygame.time.delay(500)
        # mouse.Move()
        # redraw(window, mouse, maze)
        # pygame.time.delay(500)
        # mouse.Rotate(True)
        # redraw(window, mouse, maze)
        # pygame.time.delay(500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                play = False


def drawMaze(window, maze):
    tileSizeX = window.get_width()/len(maze.maze[0])
    tileSizeY = window.get_height()/len(maze.maze)
    for i in range(len(maze.maze)):
        for j in range(len(maze.maze[0])):
            # print(f'{i},{j}')
            if maze.maze[i][j] == 1:
                pygame.draw.rect(
                    window,
                    (100, 100, 100),
                    (j * tileSizeX, i*tileSizeY, tileSizeX, tileSizeY))


def drawMouse(window, mouse, maze):
    tileSizeX = window.get_width()/len(maze.maze[0])
    tileSizeY = window.get_height()/len(maze.maze)
    pos = (mouse.x * tileSizeX + tileSizeX / 4,
           mouse.y * tileSizeY + tileSizeY / 4)
    size = (tileSizeX/2, tileSizeY/2)

    tempImage = pygame.transform.scale(image, size)
    tempImage = pygame.transform.rotate(tempImage, -90 * mouse.direction)
    window.blit(tempImage, pos)
    # pygame.draw.rect(
    #     window,
    #     (100, 255, 255),
    #     (mouse.x * tileSizeX + tileSizeX / 4, mouse.y * tileSizeY + tileSizeY / 4, tileSizeX / 2, tileSizeY / 2))


def redraw(window, mouse, maze):
    window.fill((0, 0, 0))
    drawMaze(window, maze)
    drawMouse(window, mouse, maze)
    pygame.display.update()


main()
