#!/usr/bin/python
# -*- coding: utf-8 -*-
import coredb

db = coredb.CoreDB()

db.CleanTable("src_image")
db.CleanTable("rotated_image")

# returns src image_id
s = "\0"*50 + "'"*50
imageid = db.add_src_image(10, 10, s)

db.add_image_rotation(image_id, 1, s)
