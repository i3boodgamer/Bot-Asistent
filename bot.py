import asyncio
import sqlite3 as sq
from aiogram import types,executor
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from button import group, people,daysSheduleButtonStudent,subscribeButton,teacherNameButton,daysSheduleButtonTeacher
from datetime import datetime,date
from token_1 import bot,db,dp
# from schedule_teacher import Teacher
# from schedule_student import Student

class Student:
    async def infoGroupId(group):
        global idGroup
        with sq.connect("database.db") as con:
            cur=con.cursor()
            idGroup=(cur.execute(f'SELECT groups_uni.group_id FROM groups_uni WHERE groups_uni.groups_uni = "{group}"').fetchone())[0]
    
   
    async def shedul_week(week_id,group_id):
        with sq.connect("database.db") as con:
            cur=con.cursor()
            text=cur.execute(f"""SELECT days.day, object.para_id,object.object, object.kabinet,object.time_id,object.people
            FROM groups_uni,week,days
            JOIN object ON groups_uni.group_id = object.group_id and week.week_id=object.week_id and days.day_id=object.day_id
            WHERE (days.day_id=1 or days.day_id=2 or days.day_id=3 or days.day_id=4 or days.day_id=5) and week.week_id={week_id} and groups_uni.group_id={group_id}""").fetchall()
            currentDay=''
            shedule=""
            sheduleCurrentDay=""
            for t in text:
                if(t[0]!=currentDay):
                    shedule+="# "*20+"\n"
                    currentDay=t[0]
                    shedule+="\n"+f"<b>{t[0]}</b>"+"\n"
                if(t[2]=="ЭЛЕКТИВНЫЕ КУРСЫ ПО ФИЗИЧЕСКОЙ КУЛЬТУРЕ И СПОРТУ"):
                        shedule+=f"<i>Пара {t[1]}</i> <u>{t[4]}</u>"+"\n "+f"❗️<code>{t[2]}</code>❗️"+"\n"+"\n"
                        continue
                if(t[2]=="День самостоятельной работы"):
                    shedule+=f"🖤<code>{t[2]}</code>🖤"+"\n"+"\n"
                    shedule+="# "*20+"\n"
                    break
                sheduleCurrentDay = f"<i>Пара {t[1]}</i> <u>{t[4]}</u>\n ❗<code>{t[2]}</code>❗\n 🚪{t[3]}🚪\n 👨‍🏫{t[5]}👨‍🏫\n"
                shedule+=sheduleCurrentDay+"\n"
            return shedule
    

    async def shedulDay(day_id,week_id,group_id):
        with sq.connect("database.db") as con:
            cur=con.cursor()
            text=cur.execute(f"""SELECT object.para_id,object.object, object.kabinet,object.time_id,object.people FROM groups_uni,week,days
            JOIN object ON groups_uni.group_id = object.group_id and week.week_id=object.week_id and days.day_id=object.day_id 
            WHERE days.day_id={day_id}  and week.week_id={week_id} and groups_uni.group_id={group_id}
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
        
    
    async def sms():
        with sq.connect("database.db") as con:
            cur=con.cursor()
            idUser=cur.execute("SELECT `user_id`,`group` FROM `user` WHERE `subscribe` = 1 and `group`!='NULL' and `active`=1").fetchall()
            if(not idUser):
                print("Нету пользователей, которые подписались на рассылку")
            else:
                for i in idUser:
                    try:
                        await bot.send_message(i[0],text=await Student.shedulDay(day+1,week,i[1]),parse_mode='HTML')
                    except Exception as e:
                        db.set_active(i[0],0)
                        print(f"Пользователь {i[0]} заблокировал чат-бота!: {e}")  

class Teacher:
    

    async def infoIDTeacher(nameTeacherBD: str):
          global idTeacher
          with sq.connect("database.db") as con:
            cur=con.cursor()
            idTeacher=(cur.execute(f'SELECT prepod.ID_prepod FROM prepod WHERE prepod.FIO= "{nameTeacherBD}"').fetchone())[0]

    async def shedulWeek(week_id,prepod_id):
        with sq.connect("database.db") as con:
            cur=con.cursor()
            text=cur.execute(f"""SELECT days.day, groups_uni.groups_uni, object_prepod.para_id, object_prepod.time_id,object_prepod.kab
    FROM groups_uni,week, days, prepod
    JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
    WHERE (days.day_id=1 or days.day_id=2 or days.day_id=3 or days.day_id=4 or days.day_id=5) and week.week_id={week_id} and prepod.ID_prepod={prepod_id}""").fetchall()

            
            
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
                    
                    countPara=(cur.execute(f"""SELECT count(para_id)
    FROM groups_uni,week, days, prepod
    JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
    WHERE days.day_id={dayID+1}  and week.week_id=1 and prepod.ID_prepod={prepod_id} and para_id={item[2]}""").fetchone())[0]
                    

                    
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
            return shedule
    
    async def shedulDay(day_id,week_id,prepod_id):
        with sq.connect("database.db") as con:
            cur=con.cursor()
            text=cur.execute(f"""SELECT object_prepod.para_id,groups_uni.groups_uni, object_prepod.kab,object_prepod.time_id FROM groups_uni,week,days,prepod
JOIN object_prepod ON groups_uni.group_id = object_prepod.group_id and week.week_id=object_prepod.week_id and days.day_id=object_prepod.day_id and prepod.ID_prepod=object_prepod.prepod_id
WHERE days.day_id={day_id}  and week.week_id={week_id} and prepod.ID_prepod={prepod_id}
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
                        shedule+="Нету пар"+"\n"
                        continue

                    sheduleCurrentDay=f"<i>Пара {t[0]}</i> <u>{t[3]}</u>\n ❗<code>{groups[t[0]-1]}</code>❗\n 🚪{t[2]}\n" if(len(groups[t[0]-1].split(", "))>1 and para!=t[0]) else f"<i>Пара {t[0]}</i> <u>{t[3]}</u>\n ❗<code>{t[1]}</code>❗\n 🚪{t[2]}🚪\n"
                    para=t[0]
                    shedule+=sheduleCurrentDay+"\n"
            else:
                shedule="Нету пар!"
            return shedule


async def backDef(h):
        global back
        back=h

async def infoSheduleGroup(group: str,message:types.Message):
    await backDef(0)
   
    await Student.infoGroupId(group)
    if db.count_verification(message.from_user.id)==0:
        await message.answer(text="Хотите подписаться на нашу рассылку?", reply_markup=subscribeButton)
    else:
        await message.answer(text="На какой день хотите расписание?", reply_markup=daysSheduleButtonStudent)

async def infoSheduleTeacher(nameTeaher: str,message:types.Message):
    await message.answer(text="На какой день хотите расписание?", reply_markup=daysSheduleButtonTeacher)
    await backDef(0)
    await Teacher.infoIDTeacher(nameTeaher)



        
@dp.message_handler(Text(equals="Я Студент"))
async def open_kb_group(message:types.Message):
    global chooseStudent,chooseTeacher
    chooseStudent=1
    chooseTeacher= 0
    await backDef(1)
    await message.answer(text='Выберите группу', reply_markup=group)

@dp.message_handler(Text(equals="Я Преподаватель"))
async def open_kb_group(message:types.Message):
    global chooseStudent,chooseTeacher
    chooseStudent=0
    chooseTeacher= 1
    await backDef(1)
    await message.answer(text="Выберите преподавателя", reply_markup=teacherNameButton)


@dp.message_handler(Text(equals="Беланцева Д.Ю."))
async def open_rasp_prepod(message:types.Message):
    await infoSheduleTeacher("Белавенцева Дарья Юрьевна",message)

@dp.message_handler(Text(equals="Белый А. М."))
async def open_rasp_prepod(message:types.Message):
    await infoSheduleTeacher("Белый Андрей Михайлович",message)

@dp.message_handler(Text(equals="Богдановская Д. Е."))
async def open_rasp_prepod(message:types.Message):
    await infoSheduleTeacher("Богдановская Дарья Евгеньевна",message)

@dp.message_handler(Text(equals="Буинцев В. Н."))
async def open_rasp_prepod(message:types.Message):
    await infoSheduleTeacher("Буинцев Владимир Николаевич",message)

@dp.message_handler(Text(equals="Киселева Т. В."))
async def open_rasp_prepod(message:types.Message):
    await infoSheduleTeacher("Киселева Тамара Васильевна",message)


@dp.message_handler(Text(equals="Кожемяченко В. И."))
async def open_rasp_prepod(message:types.Message):
    await infoSheduleTeacher("Кожемяченко Вадим Иванович",message)

@dp.message_handler(Text(equals="Мартусевич Е. А."))
async def open_rasp_prepod(message:types.Message):
    await infoSheduleTeacher("Мартусевич Ефим Алесандрович",message)
    
@dp.message_handler(Text(equals="Рыжих А. Ю."))
async def open_rasp_prepod(message:types.Message):
    await infoSheduleTeacher("Рыжих Алексей Юрьевич",message)

@dp.message_handler(Text(equals="Соловьева Ю. А."))
async def open_rasp_prepod(message:types.Message):
    await infoSheduleTeacher("Соловьева Юлия Александровна",message)

@dp.message_handler(Text(equals="Четвертков Е. В."))
async def open_rasp_prepod(message:types.Message):
    await infoSheduleTeacher("Четвертков Егор Васильевич",message)
    
    
    
@dp.message_handler(Text(equals="ИЭ-21"))
async def open_rasp(message:types.Message):
    await infoSheduleGroup("ИЭ-21", message)

@dp.message_handler(Text(equals="ИВТ-211"))
async def open_rasp(message:types.Message):
    await infoSheduleGroup("ИВТ-211", message)

@dp.message_handler(Text(equals="ИВТ-212"))
async def open_rasp(message:types.Message):
    await infoSheduleGroup("ИВТ-212", message)

@dp.message_handler(Text(equals="ИС-211"))
async def open_rasp(message:types.Message):
    await infoSheduleGroup("ИС-211", message)

@dp.message_handler(Text(equals="ИС-212"))
async def open_rasp(message:types.Message):
    await infoSheduleGroup("ИС-212", message)

@dp.message_handler(Text(equals="ИПМИ-21"))
async def open_rasp(message:types.Message):
    await infoSheduleGroup("ИПМИ-21", message)

@dp.message_handler(Text(equals="ИП-21"))
async def open_rasp(message:types.Message):
    await infoSheduleGroup("ИП-21", message)

@dp.message_handler(Text(equals="ИАТ-21"))
async def open_rasp(message:types.Message):
    await infoSheduleGroup("ИАТ-21", message)


@dp.message_handler(lambda message: message.text == "На сегодня")
async def nowDay(message: types.Message):
    global week,count,back,chooseTeacher, chooseStudent, idGroup, idTeacher
    
    
    if chooseTeacher == 0:
        if((day==7 or day==6) and week==2 and count==0):
            count+=1
            week-=1
        elif ((day==7 or day==6) and week==1 and count==0):
            count+=1
            week+=1
        if(day+1==6 or day+1==7):
            await message.answer(text='🔥Завтра выходной🔥')
            return
        if day==7:
            await message.answer(text=await Student.shedulDay(1,week,idGroup),parse_mode='HTML')
            return
        await message.answer(text=await Student.shedulDay(day,week,idGroup),parse_mode='HTML')
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    else:
        if((day==7 or day==6) and week==2 and count==0):
            count+=1
            week-=1
        elif ((day==7 or day==6) and week==1 and count==0):
            count+=1
            week+=1
        if(day+1==6 or day+1==7):
            await message.answer(text='🔥Завтра выходной🔥')
            return
        if day==7:
            await message.answer(text=await Teacher.shedulDay(1,week,idTeacher),parse_mode='HTML')
            return
        await message.answer(text=await Teacher.shedulDay(day,week,idTeacher),parse_mode='HTML')
    



@dp.message_handler(lambda message: message.text == "На завтра")
async def nextDay(message: types.Message):
    global week, day, count, back,chooseTeacher, chooseStudent, idGroup, idTeacher
    if chooseTeacher == 0:
        if((day==7 or day==6) and week==2 and count==0):
            count+=1
            week-=1
        elif ((day==7 or day==6) and week==1 and count==0):
            count+=1
            week+=1
        if(day+1==6 or day+1==7):
            await message.answer(text='🔥Завтра выходной🔥')
            return
        if day==7:
            await message.answer(text=await Student.shedulDay(1,week,idTeacher),parse_mode='HTML')
            return
        await message.answer(text=await Student.shedulDay(day+1,week,idTeacher),parse_mode='HTML')
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    else:
        if((day==7 or day==6) and week==2 and count==0):
            count+=1
            week-=1
        elif ((day==7 or day==6) and week==1 and count==0):
            count+=1
            week+=1
        if(day+1==6 or day+1==7):
            await message.answer(text='🔥Завтра выходной🔥')
            return
        if day==7:
            await message.answer(text=await Teacher.shedulDay(1,week,idTeacher),parse_mode='HTML')
            return
        await message.answer(text=await Teacher.shedulDay(day+1,week,idTeacher),parse_mode='HTML')

            

@dp.message_handler(lambda message: message.text == "На всю неделю")
async def now_week(message: types.Message):
    global week,count,day,chooseTeacher, idGroup, idTeacher
    if(day==7 and week==2 and count==0):
            count+=1
            week-=1
    elif (day==7 and week==1 and count==0):
            count+=1
            week+=1
    if(chooseTeacher==0):
        await message.answer(text=await Student.shedul_week(week,idGroup),parse_mode="HTML")
    else:
        await message.answer(text=await Teacher.shedulWeek(week,idTeacher),parse_mode="HTML")
    
@dp.message_handler(lambda message: message.text == "На следующую неделю")
async def next_week(message: types.Message):
    global week,count,back,chooseTeacher, idGroup, idTeacher

    pas=week
    if(pas==2):
        pas-=1
    else:
        pas+=1
    
    if(chooseTeacher==0):
        await message.answer(text=await Student.shedul_week(pas,idGroup),parse_mode="HTML")
    else:
        await message.answer(text=await Teacher.shedulWeek(pas,idTeacher),parse_mode="HTML")
    



@dp.message_handler(Text(equals="Настроить рассылку расписания"))
async def options(message:types.Message):
    await message.answer(text='Хотите оформить рассылку расписания?', reply_markup=subscribeButton)



@dp.message_handler(Text(equals="Назад"))
async def open_days(message:types.Message):
    global chooseTeacher
    if chooseTeacher==0:
        if back==0:
            await backDef(1)
            await message.answer(text='Вы вернулись обратно', reply_markup=group)
        
        else:
            await backDef(0)
            await message.answer(text='Вы вернулись обратно', reply_markup=people)
    else:
        if back==0:
            await backDef(1)
            await message.answer(text='Вы вернулись обратно', reply_markup=teacherNameButton)
        
        else:
            await backDef(0)
            await message.answer(text='Вы вернулись обратно', reply_markup=people)








@dp.message_handler(commands=['start'])
async def anny_messege(message:types.Message):
    global max_chars_line
    text="Привет! Ты студент или преподаватель СибГиу? Этот бот станет вашим спутником жизни в университете.\n""Здесь Вы можете получать информацию о расписании занятий на текущий день, на неделю и на любой другой желаемый день в удобном формате. Также вы можете оформить подписку на ежедневную рассылку расписания.\n""Здесь нет необходимости ломать голову насчет того, какая неделя тебя ждет, четная или нечетная.Выбирай нужные кнопки и вливайся в жизнь первого ВУЗа Кузбасса!""Проект выполнен студентами группы ИВТ-211\n""Команда: KIB.org"
    if message.chat.type=='private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, text=text,reply_markup=people)
        

@dp.message_handler(commands=['help'])
async def help_command_handler(message: types.Message):
    await message.answer("Список команд: /start, /help, /subscribe")

async def schedule_sms():
    global week, day
    nowDayTime=int(datetime.now().strftime("%H:%M").split(":")[1])
    while True:
    # Получаем текущее время
        nowTime = datetime.now().strftime("%H:%M")
        if(nowTime=="18:00"):
            await Student.sms()
        await asyncio.sleep(nowDayTime-int(nowTime.split(":")[1]))   



@dp.callback_query_handler(lambda callback_query: callback_query.data == "subscribe")
async def subscribe_callback(callback_query: CallbackQuery):
    global idGroup
    db.add_user_subscribe(callback_query.from_user.id,1,idGroup)
    await bot.send_message(chat_id=callback_query.from_user.id, text="Вы согласились на рассылку!\nОжидайте рассылку расписания в 18:00 перед учебным днем!\nНастройки рассылки можно изменить в любой удобный момент через функции чат-бота!",reply_markup=daysSheduleButtonStudent)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(lambda callback_query: callback_query.data == "not_subscribe")
async def subscribe_callback(callback_query: CallbackQuery):
    db.del_user_subscribe(callback_query.from_user.id,0)
    await bot.send_message(chat_id=callback_query.from_user.id, text="Вы отказались от рассылки!",reply_markup=daysSheduleButtonStudent)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)








if __name__ == "__main__":
    day=date.today().weekday()+1
    week=2
    count=0
    loop = asyncio.get_event_loop()
    loop.create_task(schedule_sms())
    executor.start_polling(dp, skip_updates=True,loop=loop)



