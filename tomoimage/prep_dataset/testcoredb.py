#!/usr/bin/python
# -*- coding: utf-8 -*-
import coredb
import numpy as np

db = coredb.CoreDB()

db.CleanTable("src_image")
db.CleanTable("rotated_image")

# returns src image_id
s = np.arange(12).reshape(2,6)
imageid = db.add_src_image(10, 10, s)

db.add_image_rotation(imageid, 1, s)
