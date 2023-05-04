import sqlite3 as sq
con=sq.connect("database.db")
cur=con.cursor()

file1=open("Raspisan\ИС-212.txt",'r',encoding='utf-8') 
raspos={
    'group':0,
    'cht':0,
    'days':0,
    'para':0,
    'time':'',
    'object':'',
    'people':'',
    'kab':''
}
group=file1.readline()
raspos['group']=8
name='ИС-212'
cur.execute("INSERT INTO groups_uni(groups_uni) VALUES (?)",(name,))
#con.commit()
k=0

while True:
    line=file1.readline()
    if not line:
        break
    if line.strip()=='Четная:':
        raspos['cht']=1
        continue
    if line.strip()=='Нечетная:':
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


    if line.strip()=='1 пара' or line.strip()=='2 пара' or line.strip()=='3 пара' or line.strip()=='4 пара' or line.strip()=='5 пара':
        raspos['para']=int((line.strip()).replace(' пара', ''))
        continue
    
    if(raspos['para']!=0):
        k=k+1
        if(k==1):
            raspos['time']=line.strip()
            continue
        elif(k==2):
            raspos['object']=line.strip()
            continue
        elif(k==3):
            raspos['people']=line.strip()
            continue
        elif(k==4):
            raspos['kab']=line.strip()
            k=0
    
    if(raspos['para']!=0):
        mas=[]
        for line in raspos:
            mas.append(raspos[line])
        #print(mas)
        cur.execute("INSERT INTO object(group_id, week_id, day_id, para_id, time_id, object, people, kabinet) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", mas)
       # con.commit()
    
result=cur.execute("SELECT `user_id`,`group` FROM `user` WHERE `subscribe` = 1 and `group`!='NULL' and `active`=1").fetchall()
print(result[0][0])

file1.close
con.close()

   
