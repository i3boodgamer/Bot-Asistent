import asyncio
import logging
import sqlite3 as sq
from aiogram import Bot, Dispatcher, types,executor
from aiogram.dispatcher.filters import Text
from button import group,student

bot = Bot(token='5749034666:AAGz8A7ON370dtBs_RwsaLTblhZ_ic5JOl0')
dp=Dispatcher(bot)



@dp.message_handler(Text(equals="Студент"))
async def open_kb_group(message:types.Message):
    await message.answer(text='Выберите группу', reply_markup=group)

@dp.message_handler(Text(equals="ГГ-19"))
async def open_rasp(message:types.Message):
    con=sq.connect("database.db")
    cur=con.cursor()
    cur.execute("SELECT ")
    res="""

    """
    await message.answer(text="""""")

@dp.message_handler(commands=['start'])
async def anny_messege(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,text="Привет! Ты студент или преподаватель СибГиу? Этот бот станет вашим спутником жизни в университете. Этот бот станет вашим спутником жизни в университете.\n" "\nЗдесь Вы можете получать информацию о расписании занятий на текущий день, на неделю и на любой другой желаемый день в удобном формате. Также вы можете оформить подписку на ежедневную рассылку расписания.\n" "\nЗдесь нет необходимости ломать голову насчет того, какая неделя тебя ждет, четная или нечетная.Выбирай нужные кнопки и вливайся в жизнь первого ВУЗа Кузбасса!\n" "\nПроект выполнен студентами группы ИВТ-211\n" "\nКоманда: KIB.org",reply_markup=student)






if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



