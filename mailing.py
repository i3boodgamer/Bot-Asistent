import sqlite3 as sq


class DataBase:
    def __init__(self, db_file):
        self.connection=sq.connect(db_file)
        self.cursor=self.connection.cursor()

    def user_exists(self,user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `user` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            return bool(len(result))
        
    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `user` (`user_id`) VALUES(?)",(user_id,))
        
    def set_active(self, user_id:int, active:int):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `active` = ? WHERE `user_id`=?",(active,user_id,))
    
    def get_user(self):
        with self.connection:
            return self.cursor.execute("SELECT `user_id`, `active` FROM `user`").fetchall()
    
    def add_user_subscribe(self, user_id,subscribe,group):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `user` WHERE `subscribe` = ? and `user_id` = ?", (subscribe,user_id,)).fetchmany(1)
            if(bool(len(result))==0):
                return self.cursor.execute("UPDATE `user` SET `subscribe` = ?, `group` = ?,`count` = 1  WHERE `user_id`=?",(subscribe,group,user_id,))
            else:
                return 0
            
    def del_user_subscribe(self, user_id,subscribe):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `user` WHERE `subscribe` = ? and `user_id` = ?", (subscribe,user_id,)).fetchmany(1)
            if(bool(len(result))==0):
                return self.cursor.execute("UPDATE `user` SET `subscribe` = ?, `group` = NULL, `count` = 1  WHERE `user_id`=?",(subscribe,user_id,))
            else:
                return 0
    
    def count_verification(self,user_id):
        with self.connection:
            result=self.cursor.execute("SELECT * FROM `user` WHERE `count` = ? and `user_id` = ?", (1,user_id,)).fetchmany(1)
            if(bool(len(result))==0):
                return 0
            else:
                return 1
            



