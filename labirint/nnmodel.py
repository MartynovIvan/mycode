import numpy as np
import labirint as lab
from random import randint
import coredb

class NNModel:
    DIRECT_UNDEF = 'undef'
    DIRECT_W = 'w' # 0
    DIRECT_E = 'e' # 1
    DIRECT_S = 's' # 2
    DIRECT_N = 'n' # 3
        
    def __init__(self):
        self.labDB = coredb.CoreDB()
        #self.labDB.CleanTable("lab_moves")
    '''
         value_e, value_w, value_s, value_n = values from labirint matrix in direction (e, w, s, n)
         `  0 - blocked
            >0 - a value from matrix

         mark_e, mark_w, mark_s, mark_n = a value from mark matrix in direction (e, w, s, n)
            0 - a cell is not marked
            >0 - a cell is marked

         mark_here = a value from current cell 
            0 - a cell is not marked
            >0 - a cell is marked

         cur_direction = a previous move direction 
            DIRECT_UNDEF = 'undef'
            DIRECT_W = 'w'
            DIRECT_E = 'e'
            DIRECT_S = 's'
            DIRECT_N = 'n'

         return value =
            DIRECT_W = 'w'
            DIRECT_E = 'e'
            DIRECT_S = 's'
            DIRECT_N = 'n'            
    '''
    def get_nextTurn(self, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here):
        #print('get_nextTurn ', ' e=', value_e, ' w=', value_w, ' s=', value_s, ' n=', value_n, ' m_here=', mark_here, 
        #    ' m_e=', mark_e, ' m_w=', mark_w, ' m_s=', mark_s, ' m_n=', mark_n )
        # def predict_direction(self, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here):
        predicted_res = self.labDB.predict_direction(value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here)
        direction = predicted_res.get('direction')
        if(direction == None):
            #print('get_nextTurn - None')
            direction = randint(0, 3)
        else:
            direction = int(direction)
        return direction

    def predict_direction(self, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here):

    # predict score by it's maximum value
#def predict_score(self, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here):
#return {'count_direction': count_direction, 'current_score': current_score, 'total_score': total_score, 'fault': fault}

        """
        if (direction == 0):
            return self.DIRECT_W 
        elif (direction == 1):
            return self.DIRECT_E 
        elif (direction == 2):
            return self.DIRECT_S 
        elif (direction == 3):
            return self.DIRECT_N 
        """

    '''
        fault_direction = a direction where fault occured 
            DIRECT_W = 'w'
            DIRECT_E = 'e'
            DIRECT_S = 's'
            DIRECT_N = 'n'            
    '''
    def add_FaultSample(self, id, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here, fault_direction):
        #print('fault ', ' e=', value_e, ' w=', value_w, ' s=', value_s, ' n=', value_n, ' m_here=', mark_here, ' m_e=', mark_e, ' m_w=', mark_w, 
        #    ' m_s=', mark_s, ' m_n=', mark_n, ' direction=', fault_direction)
        self.labDB.add_TrainSample(id, 0, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here, fault_direction, 0, 0)
        #     def add_TrainSample(self, id, ok, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here, direction, current_score, total_score): 
        """ """

    '''
        ok_direction = a direction where travel can go on 
            DIRECT_W = 'w'
            DIRECT_E = 'e'
            DIRECT_S = 's'
            DIRECT_N = 'n'            
    '''
    def add_TrainSample(self, id, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here, ok_direction, cur_score):
        #print('train ', ' e=', value_e, ' w=', value_w, ' s=', value_s, ' n=', value_n, ' m_here=', mark_here, ' m_e=', mark_e, ' m_w=', mark_w, 
        #    ' m_s=', mark_s, ' m_n=', mark_n, ' direction=', ok_direction, ' cur_score=', cur_score )
        self.labDB.add_TrainSample(id, 1, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here, ok_direction, cur_score, 0)
        #     def add_TrainSample(self, id, ok, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here, direction, current_score, total_score): 
        """ """

    def update_totalscore(self, id, total_score):
        self.labDB.update_totalscore(id, total_score)

    def Print(self):
        #self.labDB.PrintTable2("lab_moves")
        """ """
