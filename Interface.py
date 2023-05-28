import Mouse
import Maze


class MouseBehavior():

    def __init__(self):
        self.turned = False

    def Run(self, mouse, maze):
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

        # if (mouse.SensorForward()):
        #     if self.turned:
        #         mouse.Rotate(False)
        #     else:
        #         self.turned = True
        #         mouse.Rotate(True)
