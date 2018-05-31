import numpy as np
import labirint as lab
from random import randint
import random as random
import nnmodel as nm

class Traveller:
    def __init__(self):
        """ INIT PARAMS"""
        self.RUN_COUNT = 1000
        self.MAX_MOVES = 170
        self.PENALTY_FOR_FAULT_MOVE = 0.0
        self.PENALTY_FOR_ONE_MOVE = 4.0 / self.MAX_MOVES
        self.PENALTY_FOR_MORE_THAN_2_MARKS = 4.0 / self.MAX_MOVES
        
        """ Private """
        self.move_count = 0
        self.nnmodel = nm.NNModel()

    def move(self):
        gamma = 0.501 # coefficient ratio new moves / predicted moves
        gamma_inc = (1.0 - gamma) / self.RUN_COUNT # increase gamma coeff on each run
                          
        for cur_run in range(0, self.RUN_COUNT):
            self.labirint = lab.Labirint()
                      # 0 = only new moves
                      # 1 = only predicted moves
            labir_max_score = self.labirint.MIN_SCORE
            fault_moves = 0
            self.move_count = 0
            finished = 0
            marks_failed = 0

            print('--------------------------- NEW RUN ---------------------------')

            for cur_move in range(0, self.MAX_MOVES):
                marks = self.labirint.marks_around()                
                look = self.labirint.look_around()

                e = look.get('e')
                w = look.get('w')
                s = look.get('s')
                n = look.get('n')
                mark_e = marks.get('e')
                mark_w = marks.get('w')
                mark_s = marks.get('s')
                mark_n = marks.get('n')
                mark_here = marks.get('here')
                sig = 0

                #print(' e=', e, ' w=', w, ' s=', s, ' n=', n, ' m_here=', mark_here, ' m_e=', mark_e, 
                #    ' m_w=', mark_w, ' m_s=', mark_s, ' m_n=', mark_n)
               
                rand_gamm = random.random()
                #print('rand_gamm =', rand_gamm)
                if(rand_gamm < gamma):
                    #self.nnmodel.Print()
                    dir_nn = self.nnmodel.get_nextTurn(int(e), int(w), int(s), int(n), int(mark_e), int(mark_w), int(mark_s), int(mark_n), int(mark_here))
                    direction = dir_nn
                    #print('dir_nn =', dir_nn)
                else:
                    direction = randint(0, 3)
                
                #print('cur_run =', cur_run, ' cur_move=', cur_move)
                #print('direction =', direction)
                #print('gamma =', gamma)
                move_to = ''
                if (direction == 0):
                    move_to = self.nnmodel.DIRECT_W
                elif (direction == 1):
                    move_to = self.nnmodel.DIRECT_S
                elif (direction == 2):
                    move_to = self.nnmodel.DIRECT_E
                elif (direction == 3):
                    move_to = self.nnmodel.DIRECT_N

                res = self.labirint.move_and_mark(move_to)
                sig = res.get('sig')
                #print('move_to=', move_to, ' sig=', sig, ' score=', res.get('score'))
                if(sig == 0):
                    labir_max_score = max(res.get('score'), labir_max_score)
                    self.move_count += 1
                    self.nnmodel.add_TrainSample(cur_run, int(e), int(w), int(s), int(n), mark_e, mark_w, mark_s, mark_n, mark_here, int(direction), float(res.get('score')))
                    if(mark_here > 2):
                        marks_failed += 1
                    #     def add_TrainSample(self, id, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here, ok_direction, cur_score)
                    self.labirint.printme()
                    """print()"""
                                         
                    if(self.labirint.is_finished()):
                        finished = 1
                        print('finished!')
                        break
                else:
                    # 1-st case to get bad mark:
                    #  move to a wall or out of bounds
                    self.nnmodel.add_FaultSample(cur_run, int(e), int(w), int(s), int(n), mark_e, mark_w, mark_s, mark_n, mark_here, int(direction))
                    #def add_FaultSample(self, id, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here, fault_direction):
                    fault_moves += 1
                
            gamma += gamma_inc
            total_score = labir_max_score - fault_moves * self.PENALTY_FOR_FAULT_MOVE - self.move_count * self.PENALTY_FOR_ONE_MOVE - marks_failed * self.PENALTY_FOR_MORE_THAN_2_MARKS
            self.nnmodel.update_totalscore(cur_run, float(total_score))
            print('cur_run = ', cur_run, ' move_count=', self.move_count, ' labir_max_score=', labir_max_score, ' fault_moves=', fault_moves, " marks_failed=", marks_failed, ' total_score=', total_score)
        
        self.nnmodel.Print()

 # ToDo
 # 1. add fault samples
 # 2. add OK samples
 # 3. implement predict direction