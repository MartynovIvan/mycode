#!/usr/bin/python
# -*- coding: utf-8 -*-
import coredb

labDB = coredb.CoreDB()

#labDB.PrintTable2('LAB_MOVES')
#res = labDB.predict_direction(0, 1, 0, 0, 0, 1, 0, 0, 2)
labDB.PrintTable('LAB_MOVES', 14)
