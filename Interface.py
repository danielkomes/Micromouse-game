import Mouse
import Maze


class MouseBehavior():

    def __init__(self):
        self.turned = False

    def Run(self, mouse, maze):
        mouse.Move()
        if (mouse.SensorForward()):
            if self.turned:
                mouse.Rotate(False)
            else:
                self.turned = True
                mouse.Rotate(True)
