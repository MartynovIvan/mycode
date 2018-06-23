#!/usr/bin/python
# -*- coding: utf-8 -*-
import coredb
import numpy as np

XMAX = 31
YMAX = 31
N_ROTATIONS = 10

db = coredb.CoreDB(XMAX, YMAX, N_ROTATIONS)

if(1 == 0):
    db.CleanTable("src_image")
    db.CleanTable("rotated_image")

    # returns src image_id
    s = np.arange(12).reshape(2,6)
    imageid = db.add_src_image(10, 10, s)

    db.add_image_rotation(imageid, 1, s)

if(1 == 1):
    [x, y] = db.get_whole_dataset()
    print(x)
    print(y)
    
    print("x.shape[0]", x.shape[0])
    print("x.shape[1]", x.shape[1])
    print("x.shape[2]", x.shape[2])

    print("y.shape[0]", y.shape[0])
    print("y.shape[1]", y.shape[1])
    print("y.shape[2]", y.shape[2])
