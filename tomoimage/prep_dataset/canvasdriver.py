import canvas
import random

class CanvasDriver:
    XMAX = 31
    YMAX = 31
    COLORMAX = 10
    N_ROTATIONS = 10
    N_TRIANGLES = 10
    N_RECTANGLES = 10

    def __init__(self):
        self.canvas = canvas.Canvas(self.XMAX, self.YMAX)

    def putOriginalImageToStorage(self, canvas):
        print("Original:")
        #canvas.printme()
        
    def putNextDatasetToStorage(self, newcanvas):
        print("Next:")
        newcanvas.printme()
        print(newcanvas.get_dataset())
        print()
                
    def fillTriangles(self):
        for x in range(0, self.N_TRIANGLES):
            x_top = random.randint(round(self.XMAX / 3.5), round(self.XMAX / 4 * 2))
            y_top = random.randint(round(self.YMAX / 3.7), round(self.YMAX / 3 * 2.3))
            height = random.randint(5, round(self.XMAX / 2.5))
            y0 = random.randint(3, round(self.YMAX / 3.0 ) - 1)
            y1 = random.randint(round(self.YMAX - self.YMAX / 3.0) + 1, self.YMAX-3)
            print(x_top, y_top, height, y0, y1)
            value = random.randint(1, self.COLORMAX)
            self.canvas.draw_triangle(x_top, y_top, height, y0, y1, value)
            self.putOriginalImageToStorage(self.canvas)

    def fillRectangles(self):
        for x in range(0, self.N_RECTANGLES):
            x_top = random.randint(round(self.XMAX / 3.5), round(self.XMAX / 5.5 * 3))
            y_top = random.randint(round(self.YMAX / 3.7), round(self.YMAX / 5.5 * 3))
            height = random.randint(5, round(self.XMAX / 2.5))
            width = random.randint(5, round(self.YMAX / 2.5))
            print(x_top, y_top, height, width)
            value = random.randint(1, self.COLORMAX)
            self.canvas.draw_rectangle(x_top = x_top, y_top = y_top, height = height, width = width, value = value)
            self.putOriginalImageToStorage(self.canvas)

    def rotate(self):
        degree = 0.0
        for nrot in range(0, self.N_ROTATIONS):
            degree = 360.0 / self.N_ROTATIONS * nrot
            print("nrot=", nrot, "degree=", degree)
            newcanvas = self.canvas.rotate_over_angle(round(degree))
            self.putNextDatasetToStorage(newcanvas)
    
    def prepareDataset(self):
        self.N_ROTATIONS = 100
        for i in range (1, 1000):
            for self.N_TRIANGLES in range (1, 10):
                self.fillTriangles()
                self.rotate()

        for i in range (1, 1000):
            for self.N_RECTANGLES in range (1, 10):
                self.fillRectangles()
                self.rotate()
       
    def printme(self):
        self.canvas.printme()
