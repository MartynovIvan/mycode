import canvas
import random

class CanvasDriver:
    N_TRIANGLES = 1
    XMAX = 11
    YMAX = 11
    COLORMAX = 10
    N_ROTATIONS = 10

    def __init__(self):
        self.canvas = canvas.Canvas(self.XMAX, self.YMAX)

    def putOriginalImageToStorage(self, canvas):
        print("Original:")
        canvas.printme()
        
    def putNextDatasetToStorage(self, newcanvas):
        print("Next:")
        newcanvas.printme()
        print(newcanvas.get_dataset())
        print()
                
    def fillTriangles(self):
        for x in range(0, self.N_TRIANGLES):
            x_top = random.randint(0, round(self.XMAX / 2))
            y_top = random.randint(0, round(self.YMAX / 2))
            height = random.randint(2, round(self.XMAX / 2))
            y0 = random.randint(0, round(self.YMAX / 2) - 1)
            y1 = random.randint(round(self.YMAX / 2) + 1, self.YMAX)
            value = random.randint(1, self.COLORMAX)
            self.canvas.draw_triangle(x_top, y_top, height, y0, y1, value)
            self.putOriginalImageToStorage(self.canvas)
        degree = 0.0
        for nrot in range(0, self.N_ROTATIONS):
            print(nrot)
            degree = 360.0 / self.N_ROTATIONS * nrot
            newcanvas = self.canvas.rotate_over_angle(round(degree))
            self.putNextDatasetToStorage(newcanvas)

    def prepareDataset(self):
        self.fillTriangles()
       
    def printme(self):
        self.canvas.printme()
