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
    def __init__(self, XMAX, YMAX, N_ROTATIONS):
        self.connected = False
        self.con = None
        self.XMAX = XMAX
        self.YMAX = YMAX
        self.N_ROTATIONS = N_ROTATIONS

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

    # [ train_set_x, train_set_y,
    #   valid_set_x, valid_set_y,
    #   test_set_x, test_set_y ]

    # [ train_set_x, train_set_y ]
    #   train_set_x [shape=[examples_count, angle_order_number, sum]]
    #   train_set_y [shape=[examples_count, width, height]]
    def get_whole_dataset(self):
        con = self.getSQLiteConnect()
        train_set_x = np.empty(shape=[0, self.N_ROTATIONS, 0])
        train_set_x_cnt = 0
        train_set_y = np.empty(shape=[0, self.XMAX, self.YMAX])
        train_set_y_cnt = 0
        with con:
            con.row_factory = lite.Row
            cur_srcimage = con.cursor() 
            cur_srcimage.execute("select * from src_image")
            rows_src = cur_srcimage.fetchall()
            for row_src in rows_src:
                id = row_src[0]
                src_image = row_src[3]
                #train_set_y = np.append(train_set_y, [train_set_x_cnt, src_image], axis=0)
                train_set_y = np.concatenate( ( train_set_y, src_image ) )
                train_set_x_cnt += 1
                print("added", train_set_x_cnt)
                
                cur_rotimage = con.cursor() 
                cur_rotimage.execute("select * from rotated_image where image_id = :image_id order by image_id", {"image_id": id})
                rows_rot = cur_rotimage.fetchall()
                for row_rot in rows_rot:
                    id = row_rot[0]
                    rot_image = row_rot[2]
                    #train_set_x = np.append(train_set_x, [train_set_y_cnt, rot_image], axis=0)
                    train_set_x = np.concatenate( ( train_set_x, rot_image ) )
                    train_set_y_cnt += 1
        return [train_set_x, train_set_y]

