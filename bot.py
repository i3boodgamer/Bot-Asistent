import asyncio
import sqlite3 as sq
from aiogram import types,executor
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from button import group,student,days_nt,subscribe_b,prepod_name_button,days_nt_person
from datetime import datetime,date
from token_1 import bot,db,dp

class Prepod:
    async def back_def(h):
        global back
        back=h

    async def group_def(group):
        global group_uni
        

    async def shedul_week(week_id,prepod_id):
        with sq.connect("database.db") as con:
            cur=con.cursor()
            text=cur.execute(f"""SELECT days.day, groups_uni.groups_uni, object_prepod.para_id, object_prepod.time_id,object_prepod.kab
FROM groups_uni,week, days, prepod
JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
WHERE (days.day_id=1 or days.day_id=2 or days.day_id=3 or days.day_id=4 or days.day_id=5) and week.week_id={week_id} and prepod.ID_prepod={prepod_id}""").fetchall()
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
    WHERE days.day_id={d_g+1}  and week.week_id={week_id} and prepod.ID_prepod={prepod_id} and para_id={t[2]}""").fetchone())[0]
                    
                    
                    
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
                    if(len(mas[t[2]-1].split(", "))>1 and para!=t[2]):
                            para=t[2]
                            t4=f"<i>Пара {t[2]}</i> <u>{t[3]}</u>\n ❗<code>{mas[t[2]-1]}</code>❗\n 🚪{t[4]}🚪\n"
                    elif(len(mas[t[2]-1].split(", "))==1 and para!=t[2]):
                            t4=f"<i>Пара {t[2]}</i> <u>{t[3]}</u>\n ❗<code>{t[1]}</code>❗\n 🚪{t[4]}🚪\n"
                            para=t[2]
                    g+=1
                    t3+=t4+"\n"

            t3+="# "*15+"\n"
            return t3
    
    async def shedul_day(day_id,week_id,prepod_id):
        with sq.connect("database.db") as con:
            cur=con.cursor()
            text=cur.execute(f"""SELECT object_prepod.para_id,groups_uni.groups_uni, object_prepod.kab,object_prepod.time_id FROM groups_uni,week,days,prepod
JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
WHERE days.day_id={day_id}  and week.week_id={week_id} and prepod.ID_prepod={prepod_id}
            """).fetchall()

            i=0
            d=0
            
            mas=['','','','','','']
            while text!=None and i<len(text):
                    if(text[i][0]!=d):
                            d=text[i][0]
                            mas[text[i][0]-1]=text[i][1]
                            
                    else:
                            mas[text[i][0]-1]+=', '+text[i][1]
                    i+=1
            t3=""
            para=0
            
            if len(text)>0:
                for t in text:
                    t1=''
                    
                    if(t[1]=="-1"):
                        t3+="Нету пар"+"\n"
                        continue 
                    if(len(mas[t[0]-1].split(", "))>1 and para!=t[0]):
                        para=t[0]
                        t1=f"<i>Пара {t[0]}</i> <u>{t[3]}</u>\n ❗<code>{mas[t[0]-1]}</code>❗\n 🚪{t[2]}"
                    elif(len(mas[t[0]-1].split(", "))==1 and para!=t[0]):
                        t1=f"<i>Пара {t[0]}</i> <u>{t[3]}</u>\n ❗<code>{t[1]}</code>❗\n 🚪{t[2]}🚪\n"
                        para=t[0]
                            
                    t3+=t1+"\n"
                    
            else:
                t3="Нету пар!"
            return t3
                
class Student:
    async def back_def(h):
        global back
        back=h
    async def group_def(group):
        global group_uni
        with sq.connect("database.db") as con:
            cur=con.cursor()
            result=cur.execute(f'SELECT groups_uni.group_id FROM groups_uni WHERE groups_uni.groups_uni = "{group}"').fetchone()
            group_uni=result[0]
    async def shedul_week(week_id,group_id):
        with sq.connect("database.db") as con:
            cur=con.cursor()
            text=cur.execute(f"""SELECT days.day, object.para_id,object.object, object.kabinet,object.time_id,object.people
            FROM groups_uni,week,days
            JOIN object ON groups_uni.group_id = object.group_id and week.week_id=object.week_id and days.day_id=object.day_id
            WHERE (days.day_id=1 or days.day_id=2 or days.day_id=3 or days.day_id=4 or days.day_id=5) and week.week_id={week_id} and groups_uni.group_id={group_id}""").fetchall()
            d=''
            t3=""
            t4=""
            for t in text:
                if(t[0]!=d):
                    t3+="# "*20+"\n"
                    d=t[0]
                    t3+="\n"+f"<b>{t[0]}</b>"+"\n"
                if(t[2]=="ЭЛЕКТИВНЫЕ КУРСЫ ПО ФИЗИЧЕСКОЙ КУЛЬТУРЕ И СПОРТУ"):
                        t3+=f"<i>Пара {t[1]}</i> <u>{t[4]}</u>"+"\n "+f"❗️<code>{t[2]}</code>❗️"+"\n"+"\n"
                        continue
                if(t[2]=="День самостоятельной работы"):
                    t3+=f"🖤<code>{t[2]}</code>🖤"+"\n"+"\n"
                    t3+="# "*20+"\n"
                    break
                t4 = f"<i>Пара {t[1]}</i> <u>{t[4]}</u>\n ❗<code>{t[2]}</code>❗\n 🚪{t[3]}🚪\n 👨‍🏫{t[5]}👨‍🏫\n"
                t3+=t4+"\n"
            return t3
    

    async def shedul_day(day_id,week_id,group_id):
        with sq.connect("database.db") as con:
            cur=con.cursor()
            text=cur.execute(f"""SELECT object.para_id,object.object, object.kabinet,object.time_id,object.people FROM groups_uni,week,days
            JOIN object ON groups_uni.group_id = object.group_id and week.week_id=object.week_id and days.day_id=object.day_id 
            WHERE days.day_id={day_id}  and week.week_id={week_id} and groups_uni.group_id={group_id}
            """).fetchall()
            t1=""
            t3=""
            for t in text:
                if(t[1]=="ЭЛЕКТИВНЫЕ КУРСЫ ПО ФИЗИЧЕСКОЙ КУЛЬТУРЕ И СПОРТУ"):
                    t3+=f"<i>Пара {t[0]}</i> <u>{t[3]}</u>"+"\n "+f"❗<code>{t[1]}</code>❗"+"\n"*2
                    continue
                if(t[1]=="День самостоятельной работы"):
                    t3+=f"🖤<code>{t[1]}</code>🖤"+"\n"+"\n"
                    t3+="# # # # # # # # # # # # # # # # #"+"\n"
                    continue
                t1=f"""<i>Пара {t[0]}</i> <u>{t[3]}</u>
            ❗<code>{t[1]}</code>❗
            🚪{t[2]}🚪
            👨‍🏫{t[4]}👨‍🏫
                                                                                    """
                t3+=t1+"\n"
            return t3
        
    
    async def sms():
        with sq.connect("database.db") as con:
            cur=con.cursor()
            id_user=cur.execute("SELECT `user_id`,`group` FROM `user` WHERE `subscribe` = 1 and `group`!='NULL' and `active`=1").fetchall()
            if(not id_user):
                print("Нету пользователей, которые подписались на рассылку")
            else:
                for i in id_user:
                    user=i[0]
                    gr=i[1]
                    try:
                        await bot.send_message(user,text=await Student.shedul_day(days+1,daysnt,gr),parse_mode='HTML')
                    except Exception as e:
                        db.set_active(user,0)
                        print(f"Пользователь {user} заблокировал чат-бота!: {e}")  

    @dp.message_handler(Text(equals="Я Студент"))
    async def open_kb_group(message:types.Message):
        global student_,prepod_
        student_=1
        prepod_= 0
        await Student.back_def(1)
        await message.answer(text='Выберите группу', reply_markup=group)

@dp.message_handler(Text(equals="Я Преподаватель"))
async def open_kb_group(message:types.Message):
    global student_,prepod_
    student_=0
    prepod_= 1
    await Student.back_def(1)
    await message.answer(text="Выберите преподавателя", reply_markup=prepod_name_button)


@dp.message_handler(Text(equals="Беланцева Д.Ю."))
async def open_rasp_prepod(message:types.Message):
    global prepod_name
    await Student.back_def(0)
    with sq.connect("database.db") as con:
        cur=con.cursor()
        prepod_name = (cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO= "Белавенцева Дарья Юрьевна"').fetchone())[0]
        
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt_person)

@dp.message_handler(Text(equals="Белый А. М."))
async def open_rasp_prepod(message:types.Message):
    global prepod_name
    await Student.back_def(0)
    with sq.connect("database.db") as con:
        cur=con.cursor()
        prepod_name = (cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO= "Белый Андрей Михайлович"').fetchone())[0]
        
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt_person)

@dp.message_handler(Text(equals="Богдановская Д. Е."))
async def open_rasp_prepod(message:types.Message):
    global prepod_name
    await Student.back_def(0)
    with sq.connect("database.db") as con:
        cur=con.cursor()
        prepod_name = (cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO="Богдановская Дарья Евгеньевна"').fetchone())[0]
        
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt_person)

@dp.message_handler(Text(equals="Буинцев В. Н."))
async def open_rasp_prepod(message:types.Message):
    global prepod_name
    await Student.back_def(0)
    with sq.connect("database.db") as con:
        cur=con.cursor()
        prepod_name = (cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO="Буинцев Владимир Николаевич"').fetchone())[0]
        
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt_person)

@dp.message_handler(Text(equals="Киселева Т. В."))
async def open_rasp_prepod(message:types.Message):
    global prepod_name
    await Student.back_def(0)
    with sq.connect("database.db") as con:
        cur=con.cursor()
        prepod_name = (cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO="Киселева Тамара Васильевна"').fetchone())[0]
        
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt_person)



@dp.message_handler(Text(equals="Кожемяченко В. И."))
async def open_rasp_prepod(message:types.Message):
    global prepod_name
    await Student.back_def(0)
    with sq.connect("database.db") as con:
        cur=con.cursor()
        prepod_name = (cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO="Кожемяченко Вадим Иванович"').fetchone())[0]
        
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt_person)

@dp.message_handler(Text(equals="Мартусевич Е. А."))
async def open_rasp_prepod(message:types.Message):
    global prepod_name
    await Student.back_def(0)
    with sq.connect("database.db") as con:
        cur=con.cursor()
        prepod_name = (cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO="Мартусевич Ефим Алесандрович"').fetchone())[0]
        
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt_person)
    
@dp.message_handler(Text(equals="Рыжих А. Ю."))
async def open_rasp_prepod(message:types.Message):
    global prepod_name
    await Student.back_def(0)
    with sq.connect("database.db") as con:
        cur=con.cursor()
        prepod_name = (cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO="Рыжих Алексей Юрьевич"').fetchone())[0]
        
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt_person)

@dp.message_handler(Text(equals="Соловьева Ю. А."))
async def open_rasp_prepod(message:types.Message):
    global prepod_name
    await Student.back_def(0)
    with sq.connect("database.db") as con:
        cur=con.cursor()
        prepod_name = (cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO="Соловьева Юлия Александровна"').fetchone())[0]
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt_person)

@dp.message_handler(Text(equals="Четвертков Е. В."))
async def open_rasp_prepod(message:types.Message):
    global prepod_name
    await Student.back_def(0)
    with sq.connect("database.db") as con:
        cur=con.cursor()
        prepod_name = (cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO="Четвертков Егор Васильевич"').fetchone())[0]
        await Student.back_def(0)
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt_person)
    
    
    
    

@dp.message_handler(Text(equals="ИЭ-21"))
async def open_rasp(message:types.Message):
    await Student.back_def(0)
    await Student.group_def("ИЭ-21")
    if db.count_verification(message.from_user.id)==0:
        await message.answer(text="Хотите подписаться на нашу рассылку?", reply_markup=subscribe_b)
    else:
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt)

@dp.message_handler(Text(equals="ИВТ-211"))
async def open_rasp(message:types.Message):
    await Student.back_def(0)
    await Student.group_def("ИВТ-211")
    if db.count_verification(message.from_user.id)==0:
        await message.answer(text="Хотите подписаться на нашу рассылку?", reply_markup=subscribe_b)
    else:
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt)

@dp.message_handler(Text(equals="ИВТ-212"))
async def open_rasp(message:types.Message):
    await Student.back_def(0)
    await Student.group_def("ИВТ-212")
    if db.count_verification(message.from_user.id)==0:
        await message.answer(text="Хотите подписаться на нашу рассылку?", reply_markup=subscribe_b)
    else:
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt)

@dp.message_handler(Text(equals="ИС-211"))
async def open_rasp(message:types.Message):
    await Student.back_def(0)
    await Student.group_def("ИС-211")
    if db.count_verification(message.from_user.id)==0:
        await message.answer(text="Хотите подписаться на нашу рассылку?", reply_markup=subscribe_b)
    else:
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt)

@dp.message_handler(Text(equals="ИС-212"))
async def open_rasp(message:types.Message):
    await Student.back_def(0)
    await Student.group_def("ИС-212")
    if db.count_verification(message.from_user.id)==0:
        await message.answer(text="Хотите подписаться на нашу рассылку?", reply_markup=subscribe_b)
    else:
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt)

@dp.message_handler(Text(equals="ИПМИ-21"))
async def open_rasp(message:types.Message):
    await Student.back_def(0)
    await Student.group_def("ИПМИ-21")
    if db.count_verification(message.from_user.id)==0:
        await message.answer(text="Хотите подписаться на нашу рассылку?", reply_markup=subscribe_b)
    else:
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt)

@dp.message_handler(Text(equals="ИП-21"))
async def open_rasp(message:types.Message):
    await Student.back_def(0)
    await Student.group_def("ИП-21")
    if db.count_verification(message.from_user.id)==0:
        await message.answer(text="Хотите подписаться на нашу рассылку?", reply_markup=subscribe_b)
    else:
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt)

@dp.message_handler(Text(equals="ИАТ-21"))
async def open_rasp(message:types.Message):
    await Student.back_def(0)
    await Student.group_def("ИАТ-21")
    if db.count_verification(message.from_user.id)==0:
        await message.answer(text="Хотите подписаться на нашу рассылку?", reply_markup=subscribe_b)
    else:
        await message.answer(text="На какой день хотите расписание?", reply_markup=days_nt)


@dp.message_handler(lambda message: message.text == "На сегодня")
async def now_day(message: types.Message):
    global daysnt,days,group_uni,count,back,prepod_name,prepod_, student_
    print(message.message_id, "На сегодня")
    if prepod_ == 0:
        if((days==7 or days==6) and daysnt==2 and count==0):
            count+=1
            daysnt-=1
        elif ((days==7 or days==6) and daysnt==1 and count==0):
            count+=1
            daysnt+=1
        if(days+1==6 or days+1==7):
            await message.answer(text='🔥Завтра выходной🔥')
            return
        if days==7:
            await message.answer(text=await Student.shedul_day(1,daysnt,group_uni),parse_mode='HTML')
            return
        await message.answer(text=await Student.shedul_day(days,daysnt,group_uni),parse_mode='HTML')
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    else:
        if((days==7 or days==6) and daysnt==2 and count==0):
            count+=1
            daysnt-=1
        elif ((days==7 or days==6) and daysnt==1 and count==0):
            count+=1
            daysnt+=1
        if(days+1==6 or days+1==7):
            await message.answer(text='🔥Завтра выходной🔥')
            return
        if days==7:
            await message.answer(text=await Prepod.shedul_day(1,daysnt,prepod_name),parse_mode='HTML')
            return
        await message.answer(text=await Prepod.shedul_day(days,daysnt,prepod_name),parse_mode='HTML')
    



@dp.message_handler(lambda message: message.text == "На завтра")
async def next_day(message: types.Message):
    global daysnt, days, group_uni, count, back,prepod_, student_,prepod_name
    print(message.message_id, "На завтра")
    if prepod_ == 0:
        if((days==7 or days==6) and daysnt==2 and count==0):
            count+=1
            daysnt-=1
        elif ((days==7 or days==6) and daysnt==1 and count==0):
            count+=1
            daysnt+=1
        if(days+1==6 or days+1==7):
            await message.answer(text='🔥Завтра выходной🔥')
            return
        if days==7:
            await message.answer(text=await Student.shedul_day(1,daysnt,group_uni),parse_mode='HTML')
            return
        await message.answer(text=await Student.shedul_day(days+1,daysnt,group_uni),parse_mode='HTML')
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    else:
        if((days==7 or days==6) and daysnt==2 and count==0):
            count+=1
            daysnt-=1
        elif ((days==7 or days==6) and daysnt==1 and count==0):
            count+=1
            daysnt+=1
        if(days+1==6 or days+1==7):
            await message.answer(text='🔥Завтра выходной🔥')
            return
        if days==7:
            await message.answer(text=await Prepod.shedul_day(1,daysnt,prepod_name),parse_mode='HTML')
            return
        await message.answer(text=await Prepod.shedul_day(days+1,daysnt,prepod_name),parse_mode='HTML')

            

@dp.message_handler(lambda message: message.text == "На всю неделю")
async def now_week(message: types.Message):
    global daysnt,count,days,prepod_,group_uni,count,prepod_name
    if(days==7 and daysnt==2 and count==0):
            count+=1
            daysnt-=1
    elif (days==7 and daysnt==1 and count==0):
            count+=1
            daysnt+=1
    if(prepod_==0):
        await message.answer(text=await Student.shedul_week(daysnt,group_uni),parse_mode="HTML")
    else:
        await message.answer(text=await Prepod.shedul_week(daysnt,prepod_name),parse_mode="HTML")
    
@dp.message_handler(lambda message: message.text == "На следующую неделю")
async def next_week(message: types.Message):
    global daysnt,count,group_uni,back,prepod_name,prepod_

    pas=daysnt
    if(pas==2):
        pas-=1
    else:
        pas+=1
    
    if(prepod_==0):
        await message.answer(text=await Student.shedul_week(pas,group_uni),parse_mode="HTML")
    else:
        await message.answer(text=await Prepod.shedul_week(pas,prepod_name),parse_mode="HTML")
    



@dp.message_handler(Text(equals="Настроить рассылку расписания"))
async def options(message:types.Message):
    await message.answer(text='Хотите оформить рассылку расписания?', reply_markup=subscribe_b)



@dp.message_handler(Text(equals="Назад"))
async def open_days(message:types.Message):
    global prepod_
    back
    if prepod_==0:
        if back==0:
            await Student.back_def(1)
            await message.answer(text='Вы вернулись обратно', reply_markup=group)
        
        else:
            await Student.back_def(0)
            await message.answer(text='Вы вернулись обратно', reply_markup=student)
    else:
        if back==0:
            await Prepod.back_def(1)
            await message.answer(text='Вы вернулись обратно', reply_markup=prepod_name_button)
        
        else:
            await Prepod.back_def(0)
            await message.answer(text='Вы вернулись обратно', reply_markup=student)








@dp.message_handler(commands=['start'])
async def anny_messege(message:types.Message):
    global max_chars_line
    text="Привет! Ты студент или преподаватель СибГиу? Этот бот станет вашим спутником жизни в университете.\n""Здесь Вы можете получать информацию о расписании занятий на текущий день, на неделю и на любой другой желаемый день в удобном формате. Также вы можете оформить подписку на ежедневную рассылку расписания.\n""Здесь нет необходимости ломать голову насчет того, какая неделя тебя ждет, четная или нечетная.Выбирай нужные кнопки и вливайся в жизнь первого ВУЗа Кузбасса!""Проект выполнен студентами группы ИВТ-211\n""Команда: KIB.org"
    if message.chat.type=='private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, text=text,reply_markup=student)
        

@dp.message_handler(commands=['help'])
async def help_command_handler(message: types.Message):
    await message.answer("Список команд: /start, /help, /subscribe")

async def schedule_sms():
    global daysnt, days, group_uni
    now_1=int(datetime.now().strftime("%H:%M").split(":")[1])
    while True:
    # Получаем текущее время
        now = datetime.now().strftime("%H:%M")
        if(now=="18:00"):
            await Student.sms()
        await asyncio.sleep(now_1-int(now.split(":")[1]))   



@dp.callback_query_handler(lambda callback_query: callback_query.data == "subscribe")
async def subscribe_callback(callback_query: CallbackQuery):
    global group_uni
    db.add_user_subscribe(callback_query.from_user.id,1,group_uni)
    await bot.send_message(chat_id=callback_query.from_user.id, text="Вы согласились на рассылку!\nОжидайте рассылку расписания в 18:00 перед учебным днем!\nНастройки рассылки можно изменить в любой удобный момент через функции чат-бота!",reply_markup=days_nt)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(lambda callback_query: callback_query.data == "not_subscribe")
async def subscribe_callback(callback_query: CallbackQuery):
    db.del_user_subscribe(callback_query.from_user.id,0)
    await bot.send_message(chat_id=callback_query.from_user.id, text="Вы отказались от рассылки!",reply_markup=days_nt)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)








if __name__ == "__main__":
    day=date.today()
    days=day.weekday()+1
    daysnt=2
    count=0
    loop = asyncio.get_event_loop()
    loop.create_task(schedule_sms())
    executor.start_polling(dp, skip_updates=True,loop=loop)



