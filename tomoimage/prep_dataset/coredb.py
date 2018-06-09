import sqlite3 as lite
import pandas as pd

class CoreDB:
    def __init__(self):
        self.connected = False
        self.con = None
    
    def getSQLiteConnect(self):
        if (not self.connected):
            self.con = lite.connect('sqlite.db')
            self.connected = True
            self.CreateLabTable()
        return self.con

    ########################################################################################################
    ################################## COMMON FUNCTIONS ####################################################
    ########################################################################################################

    '''
        Print database table
    '''
    def PrintTable(self, table, ncols):
        print("--- TABLE ", table)
        con = self.getSQLiteConnect()
        with con:
            con.row_factory = lite.Row
            cur = con.cursor() 
            cur.execute("select * from " + table)
            rows = cur.fetchall()
            for row in rows:
                str1 = ""
                for j in range(ncols):
                    str1 = str1 + " [" + str(j) + "]=" + str(row[j]) 
                print(str1)

    '''
        Print database table
    '''
    def PrintTable2(self, table):
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
            cur.execute("PRAGMA foreign_keys=on; "
                "CREATE TABLE IF NOT EXISTS src_image ( "
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "width INTEGER, "
                "height INTEGER, "
                "image BLOB );"
                "CREATE TABLE IF NOT EXISTS rotated_image ( "
                "FOREIGN KEY (image_id) REFERENCES src_image(id), "
                "angle REAL, "
                "image BLOB );" )

    # returns src image_id
    def add_src_image(self, width, height, image_bytes):
        con = self.getSQLiteConnect()
        with con:
            con.row_factory = lite.Row
            cur = con.cursor() 
            cur.execute("INSERT INTO src_image (width, height, image) " + 
                "VALUES (:width, :height, :image)", 
                {"width": width, "height": height, "image":[buffer(image_bytes)]})
            return (cur.lastrowid)

    def add_image_rotation(self, image_id, angle, image_bytes):
        con = self.getSQLiteConnect()
        with con:
            con.row_factory = lite.Row
            cur = con.cursor() 
            cur.execute("INSERT INTO rotated_image (image_id, angle, image) " + 
                "VALUES (:image_id, :angle, :image)", 
                {"image_id": image_id, "angle": angle, "image":[buffer(image_bytes)]})
