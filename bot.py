import asyncio
from aiogram import types,executor
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from Bot.button import group, people,daysSheduleButtonStudent,subscribeButton,teacherNameButton,daysSheduleButtonTeacher
from datetime import date

from Class.mailing import mailing
from Class.schedule_student import Student
from Class.schedule_teacher import Teacher
from Bot.token_1 import bot,db,dp




async def backDef(backCount,message: types.Message):
        db.update_back(backCount,message.from_user.id)


# 
async def infoSheduleGroup(nameGroups: str,message: types.Message):
    await backDef(0,message)
    await Student(day,week,message.from_user.id).infoGroupId(nameGroups)
   

    if db.count_verification(message.from_user.id)==0:
        await message.answer(text="Хотите подписаться на нашу рассылку?", reply_markup=subscribeButton)
    else:
        await message.answer(text="На какой день хотите расписание?", reply_markup=daysSheduleButtonStudent)

async def infoSheduleTeacher(nameTeaher: str,message:types.Message):
    await message.answer(text="На какой день хотите расписание?", reply_markup=daysSheduleButtonTeacher)
    await backDef(0,message)
    await Teacher(day,week,message.from_user.id).infoIDTeacher(nameTeaher)


#Выбор
@dp.message_handler(Text(equals="Я Студент 👩‍🎓"))
async def open_kb_group(message:types.Message):
    db.chooseTeacher(0,message.from_user.id)
    await backDef(1,message)
    await message.answer(text='Выберите группу', reply_markup=group)

@dp.message_handler(Text(equals="Я Преподаватель 👨‍🏫"))
async def open_kb_group(message:types.Message):
    db.chooseTeacher(1,message.from_user.id)
    await backDef(1,message)
    await message.answer(text="Выберите преподавателя", reply_markup=teacherNameButton)


#Преподватаели
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
    

#Группы
@dp.message_handler(Text(equals="ИЭ-21"))
async def open_rasp(message:types.Message):
    await infoSheduleGroup("ИЭ-21", message)

@dp.message_handler(Text(equals="ИВТ-211"))
async def open_rasp0(message:types.Message):
    await infoSheduleGroup("ИВТ-211", message)

@dp.message_handler(Text(equals="ИВТ-212"))
async def open_rasp1(message:types.Message):
    await infoSheduleGroup("ИВТ-212", message)

@dp.message_handler(Text(equals="ИС-211"))
async def open_rasp2(message:types.Message):
    await infoSheduleGroup("ИС-211", message)

@dp.message_handler(Text(equals="ИС-212"))
async def open_rasp3(message:types.Message):
    await infoSheduleGroup("ИС-212", message)

@dp.message_handler(Text(equals="ИПМИ-21"))
async def open_rasp4(message:types.Message):
    await infoSheduleGroup("ИПМИ-21", message)

@dp.message_handler(Text(equals="ИП-21"))
async def open_rasp5(message:types.Message):
    await infoSheduleGroup("ИП-21", message)

@dp.message_handler(Text(equals="ИАТ-21"))
async def open_rasp6(message:types.Message):
    await infoSheduleGroup("ИАТ-21", message)


#Взаимодействие с ботом для получения расписании

@dp.message_handler(lambda message: message.text == "На сегодня")
async def nowDay(message: types.Message):
    if (db.select_chooseTeacher(message.from_user.id)==0):
        if(day==6 or day==7):
            await message.answer(text='🔥Сегодня выходной🔥')
            return
        if day==7:
            await message.answer(text=await Student(day, week, message.from_user.id).shedulDay(),parse_mode='HTML')
            return
        await message.answer(text=await Student(day, week, message.from_user.id).shedulDay(),parse_mode='HTML')
        
    else:
        if(day==6 or day==7):
            await message.answer(text='🔥Сегодня выходной🔥')
            return
        if day==7:
            await message.answer(text=await Teacher(1, week, message.from_user.id).shedulDay(),parse_mode='HTML')
            return
        await message.answer(text=await Teacher(day, week, message.from_user.id).shedulDay(),parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "На завтра")
async def nextDay(message: types.Message):
    global week, day
    if db.select_chooseTeacher(message.from_user.id) == 0:
        if(day+1==6 or day+1==7):
            await message.answer(text='🔥Завтра выходной🔥')
            return
        if day==7:
            await message.answer(text=await Student(1, week, message.from_user.id).shedulDay(),parse_mode='HTML')
            return
        await message.answer(text=await Student(day+1, week, message.from_user.id).shedulDay(),parse_mode='HTML')
        
    else:
        if(day+1==6 or day+1==7):
            await message.answer(text='🔥Завтра выходной🔥')
            return
        if day==7:
            await message.answer(text=await Teacher(1, week, message.from_user.id).shedulDay(),parse_mode='HTML')
            return
        await message.answer(text=await Teacher(day+1, week, message.from_user.id).shedulDay(),parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "На всю неделю")
async def now_week(message: types.Message):
    global week,day

    if(db.select_chooseTeacher(message.from_user.id))==0:
        await message.answer(text=await Student(day, week, message.from_user.id).shedul_week(),parse_mode="HTML")
    else:
        await message.answer(text=await Teacher(day, week, message.from_user.id).shedulWeek(),parse_mode="HTML")

    
@dp.message_handler(lambda message: message.text == "На следующую неделю")
async def next_week(message: types.Message):
    global week

    pas = week - 1 if week == 2 else week + 1
    
    if(db.select_chooseTeacher(message.from_user.id)==0):
        await message.answer(text=await Student(day, pas, message.from_user.id).shedul_week(),parse_mode="HTML")
    else:
        await message.answer(text=await Teacher(day, pas, message.from_user.id).shedulWeek(),parse_mode="HTML")


@dp.message_handler(Text(equals="Настроить рассылку расписания"))
async def options(message:types.Message):
    await message.answer(text='Хотите оформить рассылку расписания?', reply_markup=subscribeButton)


@dp.message_handler(Text(equals="Назад"))
async def open_days(message:types.Message):
    if db.select_chooseTeacher(message.from_user.id)==0:
        if db.select_backCount(message.from_user.id)==0:
            await backDef(1,message)
            await message.answer(text='Вы вернулись обратно', reply_markup=group)
        
        else:
            await backDef(0,message)
            await message.answer(text='Вы вернулись обратно', reply_markup=people)
    else:
        if db.select_backCount(message.from_user.id)==0:
            await backDef(1,message)
            await message.answer(text='Вы вернулись обратно', reply_markup=teacherNameButton)
        
        else:
            await backDef(0,message)
            await message.answer(text='Вы вернулись обратно', reply_markup=people)





#команды

@dp.message_handler(commands=['start'])
async def anny_messege(message:types.Message):
    text="Привет! Ты студент или преподаватель СибГиу? Этот бот станет вашим спутником жизни в университете.\n""\n""Здесь Вы можете получать информацию о расписании занятий на текущий день, на неделю и на любой другой желаемый день в удобном формате. Также вы можете оформить подписку на ежедневную рассылку расписания.\n""\n""Здесь нет необходимости ломать голову насчет того, какая неделя тебя ждет, четная или нечетная.\n\nВыбирай нужные кнопки и вливайся в жизнь первого ВУЗа Кузбасса!\n""\n""Проект выполнен студентами группы ИВТ-211\n""Команда: KIB.org"
    if message.chat.type=='private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        print(message.from_user.id)
        await bot.send_message(message.from_user.id, text=text,reply_markup=people)
        
@dp.message_handler(commands=['help'])
async def help_command_handler(message: types.Message):
    await message.answer("Список команд: /start, /help, /subscribe")        
        
        
        
        
        


#инлайн кнопки подписки

@dp.callback_query_handler(lambda callback_query: callback_query.data == "subscribe")
async def subscribe_callback(callback_query: CallbackQuery):
    db.add_user_subscribe(callback_query.from_user.id,1,db.select_idGroup(callback_query.from_user.id))
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
    loop = asyncio.get_event_loop()
    loop.create_task(mailing(day,week).schedule_sms())
    executor.start_polling(dp, skip_updates=True,loop=loop)



