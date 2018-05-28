#!/usr/bin/python
# -*- coding: utf-8 -*-
import coredb

labDB = coredb.CoreDB()

labDB.CleanTable("lab_moves")

#    def add_TrainSample(self, id, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here, direction, current_score, total_score):
labDB.add_TrainSample(133, 1, 1, 0, 0, 1, 1, 0, 1, 1, 2, 1, 10, 11)
labDB.add_TrainSample(133, 1, 1, 0, 0, 1, 1, 0, 1, 1, 2, 2, 0, 12)
labDB.add_TrainSample(133, 1, 1, 0, 0, 1, 1, 0, 1, 1, 2, 3, 0, 13)
labDB.PrintTable2("lab_moves")
res = labDB.predict_direction(1, 0, 0, 1, 1, 0, 1, 1, 2)

labDB.CleanTable("lab_moves")
labDB.add_TrainSample(133, 1, 1, 0, 0, 1, 1, 0, 1, 1, 2, 1, 10, 11)
labDB.add_TrainSample(133, 1, 1, 0, 0, 1, 1, 0, 1, 1, 2, 2, 0, 12)
labDB.add_TrainSample(133, 1, 1, 0, 0, 1, 1, 0, 1, 1, 2, 2, 0, 13)
labDB.PrintTable2("lab_moves")
res = labDB.predict_direction(1, 0, 0, 1, 1, 0, 1, 1, 2)
print(res)

labDB.CleanTable("lab_moves")
labDB.add_TrainSample(133, 1, 1, 0, 0, 1, 1, 0, 1, 1, 2, 1, 10, 11)
labDB.add_TrainSample(133, 1, 1, 0, 0, 1, 1, 0, 1, 1, 2, 2, 0, 12)
labDB.add_TrainSample(133, 1, 1, 0, 0, 1, 1, 0, 1, 1, 2, 2, 0, 13)
labDB.PrintTable2("lab_moves")
res = labDB.predict_direction(1, 0, 0, 1, 1, 0, 1, 1, 3)
print(res)

#res = labDB.predict_score(1, 0, 0, 1, 1, 0, 1, 1, 2)

#labDB.add_TrainSample(134, 0, 1, 0, 0, 1, 1, 0, 1, 1, 3, 1, 12, 13)
#labDB.add_TrainSample(134, 1, 1, 0, 0, 1, 1, 0, 1, 1, 3, 1, 0, 1)
#res = labDB.predict_score(1, 0, 0, 1, 1, 0, 1, 1, 3)
#res = labDB.predict_direcion(1, 0, 0, 1, 1, 0, 1, 1, 3)

#print(res)
#labDB.PrintTable2("lab_moves", 14)
#labDB.update_totalscore(134, 111.5)

#labDB.add_TrainSample(134, 1, 1, 0, 0, 1, 1, 0, 1, 1, 3, 1, 0, 1)
