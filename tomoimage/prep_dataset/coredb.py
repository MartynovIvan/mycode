import sqlite3 as lite
import pandas as pd
import numpy as np
import io

def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return lite.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)
        
class CoreDB:
    def __init__(self):
        self.connected = False
        self.con = None

        # Converts np.array to TEXT when inserting
        lite.register_adapter(np.ndarray, adapt_array)

        # Converts TEXT to np.array when selecting
        lite.register_converter("array", convert_array)
    
    def getSQLiteConnect(self):
        if (not self.connected):
            self.con = lite.connect('sqlite.db', detect_types=lite.PARSE_DECLTYPES)
            self.connected = True
            self.CreateTables()
        return self.con

    ########################################################################################################
    ################################## COMMON FUNCTIONS ####################################################
    ########################################################################################################

    '''
        Print database table
    '''
    def PrintTable(self, table):
        print("--- TABLE ", table)
        con = self.getSQLiteConnect()
        # Pretty way
        print(pd.read_sql_query("select * from " + table, con))

    '''
        Clean database table
    '''
    def CleanTable(self, table):
        con = self.getSQLiteConnect()
        with con:
            con.row_factory = lite.Row
            cur = con.cursor() 
            cur.execute("delete from " +  table)

    def CreateTables(self):
        con = self.getSQLiteConnect()
        with con:
            con.row_factory = lite.Row
            cur = con.cursor() 
            cur.execute("CREATE TABLE IF NOT EXISTS src_image ( "
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "width INTEGER, "
                "height INTEGER, "
                "image array );" )
            cur.execute("CREATE TABLE IF NOT EXISTS rotated_image ( "
                "image_id INTEGER, "
                "angle REAL, "
                "image array );" )
            cur.execute("CREATE INDEX IF NOT EXISTS 'image_id_idx' on rotated_image (image_id);" )


    # returns src image_id
    def add_src_image(self, width, height, image_numpyarr):
        con = self.getSQLiteConnect()
        with con:
            con.row_factory = lite.Row
            cur = con.cursor() 
            cur.execute("INSERT INTO src_image (width, height, image) " + 
                "VALUES (:width, :height, :image)", 
                {"width": width, "height": height, "image": image_numpyarr })
            return (cur.lastrowid)

    def add_image_rotation(self, image_id, angle, image_numpyarr):
        con = self.getSQLiteConnect()
        with con:
            con.row_factory = lite.Row
            cur = con.cursor() 
            cur.execute("INSERT INTO rotated_image (image_id, angle, image) " + 
                "VALUES (:image_id, :angle, :image)", 
                {"image_id": image_id, "angle": angle, "image": image_numpyarr })

