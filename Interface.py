import Mouse
import Maze


class MouseBehavior():

    def __init__(self):
        self.turned = False

    def Run(self, mouse, maze):
        self.test1(mouse, maze)
        # mouse.Move()

    def test1(self, mouse, maze):
        # mouse.Move()
        mouse.Rotate(True)
        mouse.Rotate(True)
        mouse.Move()
        mouse.Move()
        mouse.Rotate(False)
        mouse.Move()
        mouse.Move()
        mouse.Rotate(False)
        mouse.Move()
        mouse.Move()
