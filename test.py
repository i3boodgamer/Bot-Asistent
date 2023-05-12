import sqlite3 as sq
with sq.connect("database.db") as con:
        cur=con.cursor()
        text=cur.execute(f"""SELECT days.day, groups_uni.groups_uni, object_prepod.para_id, object_prepod.time_id,object_prepod.kab
FROM groups_uni,week, days, prepod
JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
WHERE (days.day_id=1 or days.day_id=2 or days.day_id=3 or days.day_id=4 or days.day_id=5) and week.week_id=1 and prepod.ID_prepod=4""").fetchall()

        
        
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
                        shedule+="\n"+f"<b>{item[0]}</b>"+"\n"
                        i=0
                        para=0
                dayID = int(weekDays.index(item[0]))
                print(dayID)
                countPara=(cur.execute(f"""SELECT count(para_id)
FROM groups_uni,week, days, prepod
JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
WHERE days.day_id={dayID+1}  and week.week_id=1 and prepod.ID_prepod=4 and para_id={item[2]}""").fetchone())[0]
                

                
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
                        return f"<i>Пара {lesson}</i> <u>{time}</u>\n ❗<code>{group}</code>❗\n 🚪{office}🚪\n" 

                sheduleCurrentDay = printText(item[2],item[3], groups[item[2]-1] if (len(groups[item[2]-1].split(", "))>1 and para!=item[2]) else item[1] ,item[4])                

                para=item[2]        
                shedule+=sheduleCurrentDay+"\n"

        
        shedule+="# "*15+"\n"


