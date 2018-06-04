import numpy as np

# 0  - >  Y
# |
# V
#
# X
# matr_canvas[x][y]

class Canvas:
    XMAX = 10
    YMAX = 10
    #matr_canvas = None
    
    def __init__(self, XMAX = 10, YMAX = 10):
        self.XMAX = XMAX
        self.YMAX = YMAX
        self.matr_canvas = np.zeros((self.XMAX, self.YMAX))


    def printme(self):
        for x in range(0, self.XMAX):
            for y in range(0, self.YMAX ):
                print ("%3d" % (self.matr_canvas[x][y]), end='')        
            print()
        print()

    def draw_hlne(self, x, y0, y1, value = 1):
        for y in range(y0, y1 + 1):
            self.matr_canvas[x][y] = value

    #         *
    #         **
    #        *** 
    #       *****
    #
    def draw_triangle(self, x_top, y_top, height, y0, y1, value = 1):
        y0_inc = (y0 - y_top) / (float)(height)
        y1_inc = (y1 - y_top) / (float)(height)
        y_triangle0 = y_top
        y_triangle1 = y_top
        for x in range(x_top, x_top + height):
            self.draw_hlne(x, round(y_triangle0), round(y_triangle1))
            y_triangle0 += y0_inc
            y_triangle1 += y1_inc
