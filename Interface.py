import Mouse
import Maze


class MouseBehavior():

    def __init__(self):
        self.turned = False

    def Run(self, mouse, maze):
        # self.testSolution(mouse, maze)
        self.testSensors(mouse, maze)

    def testSolution(self, mouse, maze):
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

    def testSensors(self, mouse, maze):
        print(mouse.SensorForward())
        mouse.Rotate(True)
        print(mouse.SensorForward())
        mouse.Rotate(True)
        print(mouse.SensorForward())
        mouse.Rotate(True)
        print(mouse.SensorForward())
        mouse.Rotate(True)
