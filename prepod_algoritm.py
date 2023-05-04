import sqlite3 as sq
con=sq.connect("database.db")
cur=con.cursor()

file1=open("Raspisan_prepod\Четвертков Егор Васильевич.txt",'r',encoding='utf-8') 
raspos={
    'prepod':0,
    'cht':0,
    'days':0,
    'para':0,
    'time':'',
    'group':0,
    'kab':''
}
fio_prep=file1.readline().strip()
res_prepod=cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO = "{fio_prep}"').fetchone()
if(res_prepod!=None):
    raspos['prepod']=res_prepod[0]
else:
    cur.execute("INSERT INTO prepod(FIO) VALUES (?)",(fio_prep,))
    con.commit()
    res_prepod=cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO = "{fio_prep}"').fetchone()
    raspos['prepod']=res_prepod[0]


k=0

while True:
    line=file1.readline()
    if not line:
        break
    if line.strip()=='Четная':
        raspos['cht']=1
        continue
    if line.strip()=='Нечетная':
        raspos['cht']=2
        continue


    if line.strip()=='Понедельник':
        raspos['days']=1
        continue
    if line.strip()=='Вторник':
        raspos['days']=2
        continue
    if line.strip()=='Среда':
        raspos['days']=3
        continue
    if line.strip()=='Четверг':
        raspos['days']=4
        continue
    if line.strip()=='Пятница':
        raspos['days']=5
        continue



    if line.strip()=='1 пара' or line.strip()=='2 пара' or line.strip()=='3 пара' or line.strip()=='4 пара' or line.strip()=='5 пара' or line.strip()=='6 пара':
        raspos['para']=int((line.strip()).replace(' пара', ''))
        continue
    
    if(raspos['para']!=0):
        k=k+1
        if(k==1):
            raspos['time']=line.strip()
            continue
        
        elif(k==2):
            i=0
            result_id=[]
            group_id=line.strip().split(", ")
            if(group_id[0]!='-'):
                while i<len(group_id):
                    if((cur.execute(f'SELECT groups_uni.group_id FROM groups_uni WHERE groups_uni.groups_uni = "{group_id[i]}"').fetchone()) is None):
                        cur.execute("INSERT INTO groups_uni(groups_uni) VALUES (?)",(group_id[i],))
                        con.commit()
                        result_id.append((cur.execute(f'SELECT groups_uni.group_id FROM groups_uni WHERE groups_uni.groups_uni = "{group_id[i]}"').fetchone())[0])
                    else:
                        result_id.append((cur.execute(f'SELECT groups_uni.group_id FROM groups_uni WHERE groups_uni.groups_uni = "{group_id[i]}"').fetchone())[0])
                    i+=1
                    raspos['group']=result_id
            else:
               raspos['group']=[]
               raspos['group'].append(-1)
            continue
        elif(k==3):
            raspos['kab']=line.strip()
            k=0
        
    
    if(raspos['para']!=0):
        mas=[]
        for line in raspos:
            mas.append(raspos[line])
        i=0
        
        while i<len(mas[5]):
            cur.execute("INSERT INTO object_prepod(prepod_id, week_id, day_id, para_id, time_id, group_id, kab) VALUES (?, ?, ?, ?, ?, ?, ?)",(mas[0],mas[1],mas[2],mas[3],mas[4],mas[5][i],mas[6]))
            #con.commit()
            print(mas[0],mas[1],mas[2],mas[3],mas[4],mas[5][i],mas[6])
            i+=1
        raspos['group'].clear()
    


file1.close
con.close()