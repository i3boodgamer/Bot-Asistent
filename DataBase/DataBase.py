import sqlite3 as sq


class DataBase:
    def __init__(self, db_file):
        self.connection=sq.connect(db_file)
        self.cursor=self.connection.cursor()

    
    
    #Вывод данных
    def user_exists(self,user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `user` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            return bool(len(result))
        
    def get_user(self):
        with self.connection:
            return self.cursor.execute("SELECT `user_id`, `active` FROM `user`").fetchall()
        
    def count_verification(self,user_id):
        with self.connection:
            result=self.cursor.execute("SELECT * FROM `user` WHERE `count` = ? and `user_id` = ?", (1,user_id,)).fetchmany(1)
            if(bool(len(result))==0):
                return 0
            else:
                return 1
    
    def select_idGroup(self,userId):
        with self.connection:
            return (self.cursor.execute(f'SELECT user.idGroupСurrent FROM user WHERE user.user_id={userId}').fetchone())[0]
    
    def select_idTeacher(self,userId):
        with self.connection:
            return (self.cursor.execute(f'SELECT user.idTeacher FROM user WHERE user.user_id={userId}').fetchone())[0]
    
    def select_backCount(self,userId):
        with self.connection:
            return (self.cursor.execute(f'SELECT user.back FROM user WHERE user.user_id={userId}').fetchone())[0]
    
    def select_chooseTeacher(self,userId):
        with self.connection:
            return (self.cursor.execute(f'SELECT user.chooseTeacher FROM user WHERE user.user_id={userId}').fetchone())[0]
        
    def select_idTeacher_teacher_bd(self, nameTeacher):
        with self.connection:
            return (self.cursor.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO= "{nameTeacher}"').fetchone())[0]
    
    def select_idGroup_groups_bd(self, nameGroup: str):
        with self.connection:
            return (self.cursor.execute(f'SELECT groups_uni.group_id FROM groups_uni WHERE groups_uni.groups_uni = "{nameGroup}"').fetchone())[0]
    
    
        

    # Изменения данных
    def chooseTeacher(self, choose, userId):
        with self.connection:
            return self.cursor.execute('UPDATE `user` SET `chooseTeacher` = ? WHERE `user_id`=?',(choose,userId,))
        
    
    def update_back(self,backCount,userId):
        with self.connection:
            return self.cursor.execute('UPDATE `user` SET `back` = ? WHERE `user_id`=?',(backCount,userId,))
    
    def update_idTeacher_user_bd(self,idTeacher,userId):
        with self.connection:
            return self.cursor.execute('UPDATE `user` SET `idTeacher` = ? WHERE `user_id`=?',(idTeacher,userId,))
    
    def update_idGroup_user_bd(self,idGroup,userId):
        with self.connection:
            return self.cursor.execute('UPDATE `user` SET `idGroupСurrent` = ? WHERE `user_id`=?',(idGroup,userId,))
    

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `user` (`user_id`) VALUES(?)",(user_id,))
        
    def set_active(self, user_id:int, active:int):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `active` = ? WHERE `user_id`=?",(active,user_id,))
    
    def add_user_subscribe(self, user_id,subscribe,group):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `user` WHERE `subscribe` = ? and `user_id` = ?", (subscribe,user_id,)).fetchmany(1)
            if(bool(len(result))==0):
                return self.cursor.execute("UPDATE `user` SET `subscribe` = ?, `groupSubscribe` = ?,`count` = 1  WHERE `user_id`=?",(subscribe,group,user_id,))
            else:
                return self.cursor.execute("UPDATE `user` SET  `groupSubscribe` = ?, `active`=?  WHERE `user_id`=?",(group,1,user_id,))
            
    def del_user_subscribe(self, user_id,subscribe):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `user` WHERE `subscribe` = ? and `user_id` = ?", (subscribe,user_id,)).fetchmany(1)
            if(bool(len(result))==0):
                return self.cursor.execute("UPDATE `user` SET `subscribe` = ?, `groupSubscribe` = NULL, `count` = 1  WHERE `user_id`=?",(subscribe,user_id,))
            else:
                return 0
    
    
    
            



