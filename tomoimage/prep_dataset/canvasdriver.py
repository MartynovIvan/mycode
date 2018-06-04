import canvas
import random

class CanvasDriver:
    N_TRIANGLES = 1
    XMAX = 10
    YMAX = 10
    COLORMAX = 10

    def __init__(self):
        self.canvas = canvas.Canvas(self.XMAX, self.YMAX)

    def fillArea(self):
        for x in range(0, self.N_TRIANGLES):
            x_top = random.randint(0, self.XMAX / 2)
            y_top = random.randint(0, self.YMAX / 2)
            height = random.randint(2, self.XMAX / 2)
            y0 = random.randint(0, self.YMAX / 2 - 1)
            y1 = random.randint(self.YMAX / 2 + 1, self.YMAX)
            value = random.randint(1, self.COLORMAX)
            self.canvas.draw_triangle(x_top, y_top, height, y0, y1, value)

    def printme(self):
        self.canvas.printme()
