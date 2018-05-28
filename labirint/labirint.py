import numpy as np

class Labirint:
    def __init__(self):

        self.x_FIN = 0
        self.y_FIN = 14

        self.x_START = 15
        self.y_START = 14

        self.x_MAX = 16
        self.y_MAX = 15
        
        self.MIN_SCORE = -72
        self.MAX_SCORE = -1

        self.matr = np.array(
            [[  0,    0,   0,   0,   0, -16, -15, -14, -13, -12,   0,  -4,  -3,  -2,  -1],
             [  0,    0,   0,   0,   0, -17,   0,   0,   0, -11,   0,   0,  -4,   0,   0],
             [  0,    0,   0,   0,   0, -18,   0,   0,   0, -10,   0,   0,  -5,   0,   0],
             [ -38,   0,   0, -21, -20, -19,   0,   0,   0,  -9,  -8,  -7,  -6,  -7,  -8],
             [ -37,   0,   0,   0, -21,   0, -54, -53, -52,   0,   0,   0,   0,   0,  -9],
             [ -36, -35,   0,   0, -22,   0,   0,   0, -51,   0,   0,   0, -12, -11, -10],
             [  0,  -34,   0, -24, -23,   0,   0,   0, -49, -50, -51, -52,   0, -12,   0],
             [  0,  -33,   0,   0, -24,   0,   0, -49, -48,   0,   0, -53, -54,   0, -64],
             [  0,  -32,   0, -26, -25,   0,   0,   0, -47,   0,   0,   0, -55,   0, -63],
             [  0,  -31,   0,   0, -26,   0,   0,   0, -46,   0,   0,   0, -56,   0, -62],
             [-31,  -30, -29, -28, -27,   0,   0,   0, -45,   0, -69,   0, -57,   0, -61],
             [  0,  -31,   0,   0,   0, -41, -42, -43, -44,   0, -68,   0, -58, -59, -60],
             [  0,  -32,   0,   0,   0, -40,   0,   0, -45,   0, -67,   0,   0,   0, -61],
             [  0,  -33,   0, -37,   0, -39,   0,   0, -46,   0, -66, -65, -64, -63, -62],
             [ -35, -34, -35, -36, -37, -38, -40,   0, -47,   0, -67,   0,   0,   0,   0],
             [   0, -35,   0, -37,   0, -39,   0,   0, -48,   0, -68, -69, -70, -71, -72]])

#       self.matr = np.array([[-12, -13,  0, -1],
#                             [-11,   0,  0, -2],
#                             [-10, -11,  0, -3],
#                             [-9 ,   0, -5, -4],
#                              [-8 ,  -7, -6,  0]])

        self.matr_mark = np.zeros((self.x_MAX, self.y_MAX))

        """ private section """        
        self.x_cur = self.x_START
        self.y_cur = self.y_START
        
        """     - > Y   """
        """|            """
        """X            """
        """  matr[X][Y] """

        """   n   """
        """ w   e """
        """   s   """

    def getCurPos(self):        
        return {'x': self.x_cur, 'y': self.y_cur}

    def is_finished(self):
        if(self.x_cur == self.x_FIN and self.y_cur == self.y_FIN):
            return True
        else:
            return False

    def setCurPos(self, x, y):        
        self.x_cur = x
        self.y_cur = y

    def look_around(self):
        if (self.x_cur == 0):
            n = 0
        else:
            n = self.matr[self.x_cur - 1][self.y_cur]

        if (self.x_cur >= (self.x_MAX-1)):
            s = 0
        else:
            s = self.matr[self.x_cur + 1][self.y_cur]

        if (self.y_cur == 0):
            w = 0
        else:
            w = self.matr[self.x_cur][self.y_cur - 1]

        if (self.y_cur >= (self.y_MAX-1)):
            e = 0
        else:
            e = self.matr[self.x_cur][self.y_cur + 1]

        here = self.matr[self.x_cur][self.y_cur]
        if (here > 0):
            here = 1
            
        score = self.matr[self.x_cur][self.y_cur]
        
        # preprocess 
        if(n < 0):
            n = 1
        if(w < 0):
            w = 1
        if(s < 0):
            s = 1
        if(e < 0):
            e = 1

        # return data
        return {'n': n, 'w': w, 's': s, 'e': e, 'here': here, 'score': score}

    def marks_around(self):
        if (self.x_cur == 0):
            n = 0
        else:
            n = self.matr_mark[self.x_cur - 1][self.y_cur]

        if (self.x_cur >= (self.x_MAX-1)):
            s = 0
        else:
            s = self.matr_mark[self.x_cur + 1][self.y_cur]

        if (self.y_cur == 0):
            w = 0
        else:
            w = self.matr_mark[self.x_cur][self.y_cur - 1]

        if (self.y_cur >= (self.y_MAX-1)):
            e = 0
        else:
            e = self.matr_mark[self.x_cur][self.y_cur + 1]

        here = self.matr_mark[self.x_cur][self.y_cur]

        return {'n': n, 'w': w, 's': s, 'e': e, 'here': here}

    def mark(self, to, val = 0):
        if (to == 'inc'):
            self.matr_mark[self.x_cur][self.y_cur] = self.matr_mark[self.x_cur][self.y_cur] + 1
        elif (to == 'dec'):
            self.matr_mark[self.x_cur][self.y_cur] = self.matr_mark[self.x_cur][self.y_cur] - 1
        elif (to == 'set'):
            self.matr_mark[self.x_cur][self.y_cur] = val

    def mark_pos(self, x, y, to, val = 0):
        if (to == 'inc'):
            self.matr_mark[x][y] += 1
        elif (to == 'dec'):
            self.matr_mark[x][y] -= 1
        elif (to == 'set'):
            self.matr_mark[x][y] = val

    def get_mark(self, to):
        return self.matr_mark[self.x_cur][self.y_cur]

    def printme(self):
        for x in range(0, self.x_MAX):
            for y in range(0, self.y_MAX ):
                if (x == self.x_cur and y == self.y_cur):
                    print ('*', end='')        
                elif (self.matr[x][y] < 0):
                    print ('-', end='')        
                elif (self.matr[x][y] != 0):
                    print (self.matr[x][y], end='')        
                elif (self.matr[x][y] == 0):
                    print ('.', end='')
            print()
        print()

    def printmarks(self):
        for x in range(0, self.x_MAX):
            for y in range(0, self.y_MAX ):
                print (self.matr_mark[x][y], end='')
            print()

    # move to direction
    #   and marks previous state as 'inc' in case of success
    def move_and_mark(self, to):
        x_prev = self.x_cur
        y_prev = self.y_cur        
        res_move = self.move(to)
        sig = res_move.get('sig')
        if(sig == 0):
            self.mark_pos(x_prev, y_prev, 'inc')
        return res_move

    # return 
    #   sig = 0: OK
    #   sig = 1: out of bounds
    #   sig = 2: wall
    def move(self, to):
        self.sig = 0
        x_cur = self.x_cur
        y_cur = self.y_cur

        if (to == 'w'):
            if (y_cur == 0):
                self.sig = 1
            else:
                y_cur = y_cur - 1

        elif (to == 's'):
            if (x_cur >= (self.x_MAX-1)):
                self.sig = 1
            else:
                x_cur = x_cur + 1

        elif (to == 'e'):
            if (y_cur >= (self.y_MAX-1)):
                self.sig = 1
            else:
                y_cur = y_cur + 1

        elif (to == 'n'):
            if (x_cur == 0):
                self.sig = 1
            else:
                x_cur = x_cur - 1

        if(self.matr[x_cur][y_cur] == 0):
            self.sig = 2
        else:
            self.x_cur = x_cur
            self.y_cur = y_cur

        return {'x': self.x_cur, 'y': self.y_cur, 'sig': self.sig, 'score': self.matr[x_cur][y_cur]}
