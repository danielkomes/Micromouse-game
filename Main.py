import Maze
import Mouse
import Interface
import Exceptions

import pygame
import tkinter as tk
from tkinter import messagebox

image = pygame.image.load("bird.png")
mouse, maze, window = 0, 0, 0


def main():
    width = 500
    window = pygame.display.set_mode((width, width))
    maze = Maze.Maze()
    mazeStart = maze.FindStart()
    mazeEnd = maze.FindEnd()
    mouse = Mouse.Mouse(maze,
                        mazeEnd[0], mazeStart[1], 0, window)
    mouse.delay = 1000
    interface = Interface.MouseBehavior()
    # redraw(window, mouse, maze)
    isWin = False
    isLose = False

    play = True
    while play:
        try:
            if (not isWin) & (not isLose):
                interface.Run(mouse, maze)  # MOUSE BEHAVIOR
                if mouse.getPos() == mazeEnd:
                    isWin = True
                    Win()
        except Exceptions.Lose:
            Lose()
            isLose = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                play = False


def Win():
    print("WIN")
    message_box("WIN", "Maze solved. Congratulations!")


def Lose():
    print("LOSE")
    message_box("LOSE", "The mouse hit a wall. Try again.")


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


main()
