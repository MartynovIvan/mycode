#!/usr/bin/python
# -*- coding: utf-8 -*-
import coredb

db = coredb.CoreDB()

labDB.CleanTable("src_image")
labDB.CleanTable("rotated_image")

# returns src image_id
s = "\0"*50 + "'"*50
imageid = labDB.add_src_image(10, 10, s):

labDB.add_image_rotation(image_id, 1, s)
