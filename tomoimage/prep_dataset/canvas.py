import numpy as np
import math

# 0  - >  Y
# |
# V
#
# X
# matr_canvas[x][y]

class Canvas:
    XMAX = 10
    YMAX = 10
    matr_canvas = None
    
    def __init__(self, XMAX = 10, YMAX = 10):
        self.XMAX = XMAX
        self.YMAX = YMAX
        self.matr_canvas = np.zeros((self.XMAX, self.YMAX))

    def getmatr_canvas(self):
        return self.matr_canvas

    def printme(self):
        for x in range(0, self.XMAX):
            for y in range(0, self.YMAX ):
                print ("%3d" % (self.matr_canvas[x][y]), end='')        
            print()
        print()

    def set_pixel(self, x, y, value = 1):
        if(x < 0 or y < 0):
            return
        if(x >= self.XMAX or y >= self.YMAX):
            return
        self.matr_canvas[x][y] = value

    def get_pixel(self, x, y):
        if(x < 0 or y < 0):
            return 0
        if(x >= self.XMAX or y >= self.YMAX):
            return 0
        return self.matr_canvas[x][y]

    def add_pixel(self, x, y, value = 1):
        if(x < 0 or y < 0):
            return
        if(x >= self.XMAX or y >= self.YMAX):
            return
        self.matr_canvas[x][y] += value

    def draw_hlne(self, x, y0, y1, value = 1):
        for y in range(y0, y1 + 1):
            self.add_pixel(x, y, value)

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
            self.draw_hlne(x, round(y_triangle0), round(y_triangle1), value)
            y_triangle0 += y0_inc
            y_triangle1 += y1_inc

    def draw_rectangle(self, x_top, y_top, width, height, value = 1):
        for x in range(x_top, x_top + height):
            self.draw_hlne(x, y_top, y_top + width - 1, value)
    
    # angle in degree clockwise
    #  function returns a Canvas object rotated by angle with a center pivot point
    #  points that exceed an area disappear
    def rotate_over_angle(self, angle):
        a = angle * math.pi / 180.0
        centerx = self.XMAX / 2
        centery = self.XMAX / 2
        canvas2 = Canvas(self.XMAX, self.YMAX)
        sina = math.sin(a)
        cosa = math.cos(a)
        for x in range(0, self.XMAX):
            for y in range(0, self.YMAX ):
                y_ = (y - centery) * cosa - (x - centery) * sina
                x_ = (y - centery) * sina + (x - centery) * cosa
                y_ += centery
                x_ += centerx
                color = self.matr_canvas[x][y]
                canvas2.set_pixel(round(x_), round(y_), color)
        return canvas2
        
    # angle in degree clockwise
    #  function returns a Canvas object rotated by angle with a center pivot point
    #  points that exceed an area disappear
    def rotate_over_angle2(self, angle):
        a = -angle * math.pi / 180.0
        centerx = self.XMAX / 2
        centery = self.XMAX / 2
        canvas2 = Canvas(self.XMAX, self.YMAX)
        sina = math.sin(a)
        cosa = math.cos(a)
        for x in range(0, self.XMAX):
            for y in range(0, self.YMAX ):
                y_ = (y - centery) * cosa - (x - centery) * sina
                x_ = (y - centery) * sina + (x - centery) * cosa
                y_ += centery
                x_ += centerx
                color = self.get_pixel(round(x_), round(y_))
                canvas2.set_pixel(x, y, color)
        return canvas2
        
    def get_dataset(self):
        matr_res = np.zeros((self.YMAX))
        for y in range(0, self.YMAX):
            for x in range(0, self.XMAX):
                matr_res[y] += self.matr_canvas[x][y]
        return matr_res