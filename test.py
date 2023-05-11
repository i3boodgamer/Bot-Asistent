import sqlite3 as sq
with sq.connect("database.db") as con:
        cur=con.cursor()
        text=cur.execute(f"""SELECT days.day, groups_uni.groups_uni, object_prepod.para_id, object_prepod.time_id,object_prepod.kab
FROM groups_uni,week, days, prepod
JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
WHERE (days.day_id=1 or days.day_id=2 or days.day_id=3 or days.day_id=4 or days.day_id=5) and week.week_id=1 and prepod.ID_prepod=4""").fetchall()
        
        
        
        
      
        t3=""
        d=g=d_t=d_g=i=0
        mas=['','','','','','']
        mas_nt=[0,0,0,0,0]

        while text!=None and i<len(text):
                if(text[i][0]=='Понедельник'): mas_nt[0]+=1
                elif(text[i][0]=='Вторник'): mas_nt[1]+=1
                elif(text[i][0]=='Среда'): mas_nt[2]+=1
                elif(text[i][0]=='Четверг'): mas_nt[3]+=1
                elif(text[i][0]=='Пятница'): mas_nt[4]+=1
                i+=1
        

        
        
        i=0
        t4=""
        for t in text:
                if(t[1]=="-1" and mas_nt[d_g]==0):
                        t3+="Нету пар"+"\n"
                        continue 
                if(t[0]!=d):
                        d=t[0]
                        t3+="# "*15+"\n"
                        t3+="\n"+f"<b>{t[0]}</b>"+"\n"
                        i=0
                        para=0

                if(t[0]=='Понедельник'): d_g=0
                elif(t[0]=='Вторник'): d_g=1
                elif(t[0]=='Среда'): d_g=2
                elif(t[0]=='Четверг'): d_g=3
                elif(t[0]=='Пятница'): d_g=4
                count_par=(cur.execute(f"""SELECT count(para_id)
FROM groups_uni,week, days, prepod
JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
WHERE days.day_id={d_g+1}  and week.week_id=2 and prepod.ID_prepod=4 and para_id={t[2]}""").fetchone())[0]
                
                
                
                if(mas_nt[d_g]!=0):
                        if(t[2]!=d_t):
                                d_t=t[2]
                                mas[t[2]-1]=t[1]
                        elif d_t==t[2]:
                                mas[t[2]-1]+=', '+t[1]
                        i+=1
                        if i<count_par:
                                continue
                        else:
                                i=0
                print(count_par)
                if(len(mas[t[2]-1].split(", "))>1 and para!=t[2]):
                        para=t[2]
                        t4=f"<i>Пара {t[2]}</i> <u>{t[3]}</u>\n ❗<code>{mas[t[2]-1]}</code>❗\n 🚪{t[4]}🚪"
                elif(len(mas[t[2]-1].split(", "))==1 and para!=t[2]):
                        t4=f"<i>Пара {t[2]}</i> <u>{t[3]}</u>\n ❗<code>{t[1]}</code>❗\n 🚪{t[4]}🚪\n"
                        para=t[2]
                g+=1
                t3+=t4+"\n"

        t3+="# "*15+"\n"
                
        print(t3)
        


