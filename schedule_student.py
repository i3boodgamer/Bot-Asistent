import sqlite3 as sq
from token_1 import db
from days_week import day_week
from config import DATABASE

class Student(day_week):
    def __init__(self, day: int, week: int, idStudent:int):
        day_week.__init__(self,day,week)
        self.idStudent=idStudent
        self.group=db.select_idGroup(idStudent)

    async def infoGroupId(self,nameGroups):
        idGroup=db.select_idGroup_groups_bd(nameGroups)
        db.update_idGroup_user_bd(idGroup,self.idStudent)
    
   
    async def shedul_week(self):
        with sq.connect(DATABASE) as con:
            cur=con.cursor()
            text=cur.execute(f"""SELECT days.day, object.para_id,object.object, object.kabinet,object.time_id,object.people
            FROM groups_uni,week,days
            JOIN object ON groups_uni.group_id = object.group_id and week.week_id=object.week_id and days.day_id=object.day_id
            WHERE (days.day_id=1 or days.day_id=2 or days.day_id=3 or days.day_id=4 or days.day_id=5) and week.week_id={self.week} and groups_uni.group_id={self.group}""").fetchall()
            currentDay=''
            shedule=""
            sheduleCurrentDay=""
            for t in text:
                if(t[0]!=currentDay):
                    shedule+="# "*20+"\n"
                    currentDay=t[0]
                    shedule+="\n"+f"<code>{t[0]}</code>"+"\n"
                if(t[2]=="ЭЛЕКТИВНЫЕ КУРСЫ ПО ФИЗИЧЕСКОЙ КУЛЬТУРЕ И СПОРТУ"):
                        shedule+=f"<i>Пара {t[1]}</i> <u>{t[4]}</u>"+"\n "+f"❗️<b>{t[2]}</b>❗️"+"\n"+"\n"
                        continue
                if(t[2]=="День самостоятельной работы"):
                    shedule+=f"🖤<b>{t[2]}</b>🖤"+"\n"+"\n"
                    shedule+="# "*20+"\n"
                    break
                sheduleCurrentDay = f"<i>Пара {t[1]}</i> <u>{t[4]}</u>\n ❗<b>{t[2]}</b>❗\n 🚪{t[3]}🚪\n 👨‍🏫{t[5]}👨‍🏫\n"
                shedule+=sheduleCurrentDay+"\n"
            return shedule
    

    async def shedulDay(self):
        with sq.connect(DATABASE) as con:
            cur=con.cursor()
            if(self.day==6 or self.day==7):
                return "🔥Завтра выходной🔥"
            text=cur.execute(f"""SELECT object.para_id,object.object, object.kabinet,object.time_id,object.people FROM groups_uni,week,days
            JOIN object ON groups_uni.group_id = object.group_id and week.week_id=object.week_id and days.day_id=object.day_id 
            WHERE days.day_id={self.day}  and week.week_id={self.week} and groups_uni.group_id={self.group}
            """).fetchall()
            sheduleCurrentDay=""
            shedule=""
            
            for t in text:
                if(t[1]=="ЭЛЕКТИВНЫЕ КУРСЫ ПО ФИЗИЧЕСКОЙ КУЛЬТУРЕ И СПОРТУ"):
                    shedule+=f"<i>Пара {t[0]}</i> <u>{t[3]}</u>"+"\n "+f"❗<code>{t[1]}</code>❗"+"\n"*2
                    continue
                if(t[1]=="День самостоятельной работы"):
                    shedule+=f"🖤<code>{t[1]}</code>🖤"+"\n"+"\n"
                    shedule+="# # # # # # # # # # # # # # # # #"+"\n"
                    continue
                sheduleCurrentDay=f"<i>Пара {t[0]}</i> <u>{t[3]}</u>\n ❗<code>{t[1]}</code>❗\n 🚪{t[2]}🚪\n 👨‍🏫{t[4]}👨‍🏫\n "
                shedule+=sheduleCurrentDay+"\n"
            return shedule