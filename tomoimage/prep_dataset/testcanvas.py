import canvas


if(1 == 0):    
    cv = canvas.Canvas()
    cv.printme()

if(1 == 0):    
    cv = canvas.Canvas()
    cv.draw_hlne(1, 0, 1, 1)
    cv.printme()

#     def draw_triangle(self, x_top, y_top, height, y0, y1, value = 1)
if(0 == 1):    
    cv = canvas.Canvas()
    cv.draw_triangle(x_top = 0, y_top = 0, height = 5, y0 = 0, y1 = 5, value = 1)
    cv.printme()

#     def draw_triangle(self, x_top, y_top, height, y0, y1, value = 1)
if(0 == 1):    
    cv = canvas.Canvas()
    cv.draw_triangle(x_top = 0, y_top = 5, height = 5, y0 = 0, y1 = 5, value = 1)
    cv.draw_triangle(x_top = 0, y_top = 0, height = 5, y0 = 0, y1 = 5, value = 1)
    cv.printme()

#     def draw_triangle(self, x_top, y_top, height, y0, y1, value = 1)
if(1 == 0):    
    cv = canvas.Canvas()
    cv.draw_rectangle(x_top = 0, y_top = 0, height = 5, width = 2)
    cv.printme()

#     def draw_triangle(self, x_top, y_top, height, y0, y1, value = 1)
if(1 == 0):    
    cv = canvas.Canvas(11, 11)
    cv.draw_rectangle(x_top = 3, y_top = 3, height = 7, width = 2)
    cv.printme()
    rot = cv.rotate_over_angle2(90)
    rot.printme()

#     def draw_triangle(self, x_top, y_top, height, y0, y1, value = 1)
if(1 == 1):    
    cv = canvas.Canvas()
    cv.draw_rectangle(x_top = 0, y_top = 0, height = 5, width = 2)
    cv.draw_rectangle(x_top = 0, y_top = 8, height = 10, width = 2, value = 2)
    cv.printme()
    print(cv.get_dataset())
