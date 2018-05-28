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

    def CreateLabTable(self):
        con = self.getSQLiteConnect()
        with con:
            con.row_factory = lite.Row
            cur = con.cursor() 
            cur.execute("CREATE TABLE IF NOT EXISTS lab_moves ( " +
                "id INTEGER, " +
                "e INTEGER, " +
                "w INTEGER, " +
                "s INTEGER, " +
                "n INTEGER, " +
                "mw INTEGER, " +
                "ms INTEGER, " +
                "me INTEGER, " +
                "mn INTEGER, " +
                "ok INTEGER, " +
                "mark_here INTEGER, " +
                "direction INTEGER, " +
                "current_score REAL, "
                "total_score REAL ); " )
            cur.execute("CREATE INDEX IF NOT EXISTS 'id_idx' on lab_moves (id);" )
            cur.execute("CREATE INDEX IF NOT EXISTS 'w_idx' on lab_moves (w);" )
            cur.execute("CREATE INDEX IF NOT EXISTS 's_idx' on lab_moves (s);" )
            cur.execute("CREATE INDEX IF NOT EXISTS 'e_idx' on lab_moves (e);" )
            cur.execute("CREATE INDEX IF NOT EXISTS 'n_idx' on lab_moves (n);" )
            cur.execute("CREATE INDEX IF NOT EXISTS 'mw_idx' on lab_moves (mw);" )
            cur.execute("CREATE INDEX IF NOT EXISTS 'ms_idx' on lab_moves (ms);" )
            cur.execute("CREATE INDEX IF NOT EXISTS 'me_idx' on lab_moves (me);" )
            cur.execute("CREATE INDEX IF NOT EXISTS 'mn_idx' on lab_moves (mn);" )
            cur.execute("CREATE INDEX IF NOT EXISTS 'ok_idx' on lab_moves (ok);" )
            cur.execute("CREATE INDEX IF NOT EXISTS 'current_score_idx' on lab_moves (current_score);" )
            cur.execute("CREATE INDEX IF NOT EXISTS 'total_score_idx' on lab_moves (total_score);" )

    def add_TrainSample(self, id, ok, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here, direction, current_score, total_score):
        con = self.getSQLiteConnect()
        with con:
            con.row_factory = lite.Row
            cur = con.cursor() 
            cur.execute("INSERT INTO LAB_MOVES (id, ok, w, s, e, n, mw, ms, me, mn, mark_here, direction, current_score, total_score) " + 
                "VALUES (:id, :ok, :w, :s, :e, :n, :mw, :ms, :me, :mn, :mark_here, :direction, :current_score, :total_score)", 
                {"id": id, "ok": ok, "w":value_w, "s":value_s, "e":value_e, "n":value_n, "mw":mark_w, "ms":mark_s, "me":mark_e, "mn":mark_n, 
                "mark_here":mark_here, "direction":direction, "current_score":current_score, "total_score":total_score})

    # predict score to some direction and get it's max total_score
    # example 
    #    e  w  s  n  me  mw  ms  mn   dir   score
    #    1  0  0  0  0   0   0   0    1     2.0
    #    1  0  0  0  0   0   0   0    2     3.0
    #    1  0  0  0  0   0   0   0    2     3.0
    # predict_score("1  0  0  0  0   0   0   0    2")
    # res = { direction = 1 }
    #
    #    e  w  s  n  me  mw  ms  mn   dir   score
    #    1  0  0  0  0   0   0   0    1     2.0
    #    1  0  0  0  0   0   0   0    2     2.0
    #    1  0  0  0  0   0   0   0    3     2.0
    # predict_score("1  0  0  0  0   0   0   0    2")
    # res = { direction = 1 }
    #
    #    e  w  s  n  me  mw  ms  mn   dir   score
    #    1  0  0  0  0   0   0   0    1     2.0
    #    1  0  0  0  0   0   0   0    2     2.0
    #    1  0  0  0  0   0   0   0    3     2.0
    # predict_score("0  0  0  0  0   0   0   0    2")
    # res = { direction = 0 }
    def predict_direction(self, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here):
        #print('predict_direction ', ' e=', value_e, ' w=', value_w, ' s=', value_s, ' n=', value_n, 
        #' m_e=', mark_e, ' m_w=', mark_w, ' m_s=', mark_s, ' m_n=', mark_n, ' m_here=', mark_here)
        direction = 0
        total_score = 0.0
        
        con = self.getSQLiteConnect()
        cursor=con.cursor()

        # count total_score
        cursor.execute("select MAX(total_score), direction from LAB_MOVES where " + 
            "w = :w AND s = :s AND e = :e AND n = :n AND mw = :mw AND ms = :ms AND me = :me " + 
            "AND mn = :mn AND ok = 1",
            {"w":value_w, "s":value_s, "e":value_e, "n":value_n, "mw":mark_w, "ms":mark_s, "me":mark_e, "mn":mark_n })
        cur_cursor = cursor.fetchone()
        total_score = cur_cursor[0]
        direction = cur_cursor[1]

        return {'total_score': total_score, 'direction': direction}

    def predict_score(self, value_e, value_w, value_s, value_n, mark_e, mark_w, mark_s, mark_n, mark_here):
        print('predict_score ', ' e=', value_e, ' w=', value_w, ' s=', value_s, ' n=', value_n, 
        ' m_e=', mark_e, ' m_w=', mark_w, ' m_s=', mark_s, ' m_n=', mark_n, ' m_here=', mark_here)

        fault = 0
        count_direction = 0
        current_score = 0.0
        total_score = 0.0
        
        con = self.getSQLiteConnect()
        cursor=con.cursor()

        # count direction
        cursor.execute("select count(direction) from LAB_MOVES where " + 
            "w = :w AND s = :s AND e = :e AND n = :n AND mw = :mw AND ms = :ms AND me = :me " + 
            "AND mn = :mn",
            {"w":value_w, "s":value_s, "e":value_e, "n":value_n, "mw":mark_w, "ms":mark_s, "me":mark_e, "mn":mark_n, "mark_here":mark_here})
        count_direction = cursor.fetchone()[0]

        # fault
        cursor.execute("select count(direction) from LAB_MOVES where " + 
            "w = :w AND s = :s AND e = :e AND n = :n AND mw = :mw AND ms = :ms AND me = :me " + 
            "AND mn = :mn AND mark_here = :mark_here and ok = 0",
            {"w":value_w, "s":value_s, "e":value_e, "n":value_n, "mw":mark_w, "ms":mark_s, "me":mark_e, "mn":mark_n, "mark_here":mark_here})
        count_direction_f = cursor.fetchone()[0]
        if(count_direction_f > 0):
            fault = 1

        # count total_score
        if(count_direction > 0):
            cursor.execute("select MAX(total_score) from LAB_MOVES where " + 
                "w = :w AND s = :s AND e = :e AND n = :n AND mw = :mw AND ms = :ms AND me = :me " + 
                "AND mn = :mn AND mark_here = :mark_here",
                {"w":value_w, "s":value_s, "e":value_e, "n":value_n, "mw":mark_w, "ms":mark_s, "me":mark_e, "mn":mark_n, "mark_here":mark_here})
            total_score = cursor.fetchone()[0]
            
        # current_score
        if(count_direction > 0):
            cursor.execute("select MAX(current_score) from LAB_MOVES where " + 
                "w = :w AND s = :s AND e = :e AND n = :n AND mw = :mw AND ms = :ms AND me = :me " + 
                "AND mn = :mn AND mark_here = :mark_here",
                {"w":value_w, "s":value_s, "e":value_e, "n":value_n, "mw":mark_w, "ms":mark_s, "me":mark_e, "mn":mark_n, "mark_here":mark_here})
            current_score = cursor.fetchone()[0]

        return {'count_direction': count_direction, 'current_score': current_score, 'total_score': total_score, 'fault': fault}

    def update_totalscore(self, id, total_score):
        con = self.getSQLiteConnect()
        with con:
            con.row_factory = lite.Row
            cur = con.cursor() 
            cur.execute("UPDATE LAB_MOVES SET total_score = :total_score WHERE id = :id",
                {"id": id, "total_score":total_score})