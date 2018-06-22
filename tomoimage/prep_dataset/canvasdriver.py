import canvas
import random
import coredb
import numpy as np

class CanvasDriver:
    XMAX = 31
    YMAX = 31
    COLORMAX = 10
    N_ROTATIONS = 10
    N_RECT_SQUARE_COUNT = 2
    N_RECT_TRIANGL_COUNT = 2
    N_MAX_TRIANGLES = 10
    N_MAX_RECTANGLES = 10
    db = None
    canvas = None 

    def __init__(self):
        self.canvas = canvas.Canvas(self.XMAX, self.YMAX)
        self.db = coredb.CoreDB(self.XMAX, self.YMAX,  self.N_ROTATIONS)
        self.db.CleanTable("src_image")
        self.db.CleanTable("rotated_image")

    def putOriginalImageToStorage(self, canvas_original):
        #print("Original:")
        self.imageid = self.db.add_src_image(self.XMAX, self.YMAX, canvas_original.getmatr_canvas())
        print("self.imageid=", self.imageid)
        #canvas.printme()
        
    def putNextDatasetToStorage(self, angle, newcanvas):
        #print("Next:")
        #newcanvas.printme()
        dataset = newcanvas.get_dataset()
        #print(dataset)
        self.db.add_image_rotation(self.imageid, angle, dataset)
        print("imageid for rot=", self.imageid)
        #print()
                
    def fillTriangles(self):
        for x in range(0, self.N_TRIANGLES):
            x_top = random.randint(round(self.XMAX / 3.5), round(self.XMAX / 4 * 2))
            y_top = random.randint(round(self.YMAX / 3.7), round(self.YMAX / 3 * 2.3))
            height = random.randint(5, round(self.XMAX / 2.5))
            y0 = random.randint(3, round(self.YMAX / 3.0 ) - 1)
            y1 = random.randint(round(self.YMAX - self.YMAX / 3.0) + 1, self.YMAX-3)
            #print(x_top, y_top, height, y0, y1)
            value = random.randint(1, self.COLORMAX)
            self.canvas.draw_triangle(x_top, y_top, height, y0, y1, value)
        self.putOriginalImageToStorage(self.canvas)

    def fillRectangles(self):
        for x in range(0, self.N_RECTANGLES):
            x_top = random.randint(round(self.XMAX / 3.5), round(self.XMAX / 5.5 * 3))
            y_top = random.randint(round(self.YMAX / 3.7), round(self.YMAX / 5.5 * 3))
            height = random.randint(5, round(self.XMAX / 2.5))
            width = random.randint(5, round(self.YMAX / 2.5))
            #print(x_top, y_top, height, width)
            value = random.randint(1, self.COLORMAX)
            self.canvas.draw_rectangle(x_top = x_top, y_top = y_top, height = height, width = width, value = value)
        self.putOriginalImageToStorage(self.canvas)

    def rotate(self):
        degree = 0.0
        for nrot in range(0, self.N_ROTATIONS):
            degree = 360.0 / self.N_ROTATIONS * nrot
            #print("nrot=", nrot, "degree=", degree)
            newcanvas = self.canvas.rotate_over_angle(round(degree))
            self.putNextDatasetToStorage(degree, newcanvas)
    
    def prepareDataset(self):
        for i in range (self.N_RECT_TRIANGL_COUNT):
            for self.N_TRIANGLES in range (1, self.N_MAX_TRIANGLES + 1):
                self.fillTriangles()
                canv_rotated = self.rotate()
                print("triangle i=", i, " N=", self.N_TRIANGLES)

        for i in range (self.N_RECT_SQUARE_COUNT):
            for self.N_RECTANGLES in range (1, self.N_MAX_RECTANGLES + 1):
                self.fillRectangles()
                canv_rotated = self.rotate()
                print("rect i=", i, " N=", self.N_RECTANGLES)
       
    def printme(self):
        self.canvas.printme()