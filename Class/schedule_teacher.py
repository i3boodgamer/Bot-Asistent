import sqlite3 as sq
from Bot.token_1 import db
from Class.days_week import day_week

class Teacher(day_week):
        def __init__(self,day:int, week: int, idPeople: int):
                day_week.__init__(self,day,week)
                self.idPeople=idPeople
                self.teacher=db.select_idTeacher(idPeople)
        async def infoIDTeacher(self, nameTeacherBD: str):
                teacherId=db.select_idTeacher_teacher_bd(nameTeacherBD)
                db.update_idTeacher_user_bd(teacherId, self.idPeople)

        async def shedulWeek(self):
                with sq.connect("C:/Users/ignat/Desktop/Projec/DataBase/database.db") as con:
                        cur=con.cursor()
                        text=cur.execute(f"""SELECT days.day, groups_uni.groups_uni, object_prepod.para_id, object_prepod.time_id,object_prepod.kab
                FROM groups_uni,week, days, prepod
                JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
                WHERE (days.day_id=1 or days.day_id=2 or days.day_id=3 or days.day_id=4 or days.day_id=5) and week.week_id={self.week} and prepod.ID_prepod={self.teacher}""").fetchall()

                        
                        
                        shedule=""
                        currentPara=dayID=i=currentDay=0
                        
                        groups=['','','','','','']
                        weekDaysCount=[0,0,0,0,0]

                        weekDays = ["Понедельник",'Вторник','Среда','Четверг','Пятница']
                        for item in text:
                                weekDaysCount[weekDays.index(item[0])]+=1

                
                        i=0
                        sheduleCurrentDay=""
                        for item in text:
                                if(item[1]=="-1" and weekDaysCount[dayID]==0):
                                        shedule+="Нету пар"+"\n"
                                        continue 
                                if(item[0]!=currentPara):
                                        currentPara=item[0]
                                        shedule+="# "*15+"\n"
                                        shedule+="\n"+f"<code>{item[0]}</code>"+"\n"
                                        i=0
                                        para=0
                                dayID = int(weekDays.index(item[0]))
                                
                                countPara=(cur.execute(f"""SELECT count(para_id)
                FROM groups_uni,week, days, prepod
                JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
                WHERE days.day_id={dayID+1}  and week.week_id=1 and prepod.ID_prepod={self.teacher} and para_id={item[2]}""").fetchone())[0]
                                

                                
                                if(weekDaysCount[dayID]!=0):
                                        if(item[2]!=currentDay):
                                                currentDay=item[2]
                                                groups[item[2]-1]=item[1]
                                        else:
                                                groups[item[2]-1]+=', '+item[1]
                                        i+=1
                                        if i<countPara:
                                                continue
                                        else:
                                                i=0

                                def printText (lesson, time, group, office):
                                        return f"<i>Пара {lesson}</i> <u>{time}</u>\n ❗<b>{group}</b>❗\n 🚪{office}🚪\n" 

                                sheduleCurrentDay = printText(item[2],item[3], groups[item[2]-1] if (len(groups[item[2]-1].split(", "))>1 and para!=item[2]) else item[1] ,item[4])                

                                para=item[2]        
                                shedule+=sheduleCurrentDay+"\n"

                        
                        shedule+="# "*15+"\n"
                        return shedule
        
        async def shedulDay(self):
                with sq.connect("C:/Users/ignat/Desktop/Projec/DataBase/database.db") as con:
                        cur=con.cursor()
                        text=cur.execute(f"""SELECT object_prepod.para_id,groups_uni.groups_uni, object_prepod.kab,object_prepod.time_id FROM groups_uni,week,days,prepod
                JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
                WHERE days.day_id={self.day}  and week.week_id={self.week} and prepod.ID_prepod={self.teacher}
                        """).fetchall()
                        

                        currentPara=i=0
                        
                        groups=['','','','','','']
                        while text!=None and i<len(text):
                                if(text[i][0]!=currentPara):
                                        currentPara=text[i][0]
                                        groups[text[i][0]-1]=text[i][1]
                                else:
                                        groups[text[i][0]-1]+=', '+text[i][1]
                                i+=1
                        shedule=""
                        para=0
                        
                        if len(text)>0:
                                for t in text:
                                        sheduleCurrentDay=''
                                        
                                        if(t[1]=="-1"):
                                                shedule+="Нету пар!"+"\n"
                                                continue
                                        
                                        if(len(groups[t[0]-1].split(", "))>1 and para!=t[0]):sheduleCurrentDay=f"<i>Пара {t[0]}</i> <u>{t[3]}</u>\n ❗<code>{groups[t[0]-1]}</code>❗\n 🚪{t[2]}\n"
                                        elif(len(groups[t[0]-1].split(", "))!=0 and para!=t[0]):sheduleCurrentDay=f"<i>Пара {t[0]}</i> <u>{t[3]}</u>\n ❗<code>{t[1]}</code>❗\n 🚪{t[2]}🚪\n"
                                        para=t[0]
                                        shedule+=sheduleCurrentDay+"\n"
                                        
                        else:
                                shedule="Нету пар!"
                        
                        return shedule
                