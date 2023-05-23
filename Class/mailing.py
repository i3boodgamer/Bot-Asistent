from datetime import datetime
from Class.schedule_student import Student
import asyncio
from aiogram import types
from Bot.token_1 import bot,db
import sqlite3 as sq
from Class.days_week import day_week
class mailing(day_week):
        def __init__(self,day,week):
                day_week.__init__(self,day,week)
                
                

        async def schedule_sms(self):
                nowDayTime=int(datetime.now().strftime("%H:%M:%S").split(":")[1])
                while True:
                # Получаем текущее время
                        nowTime = datetime.now().strftime("%H:%M:%S")
                        if(nowTime=="11:56:00"):
                                await mailing.sms(self)
                        await asyncio.sleep(abs(nowDayTime-int(nowTime.split(":")[1])))
                        
                
        async def sms(self):
                with sq.connect("C:/Users/ignat/Desktop/Projec/DataBase/database.db") as con:
                        cur=con.cursor()
                        idUser=cur.execute("SELECT `user_id`,`groupSubscribe` FROM `user` WHERE `subscribe` = 1 and `groupSubscribe`!='NULL' and `active`=1").fetchall()
                        if(not idUser):
                                print("Нету пользователей, которые подписались на рассылку")
                        else:
                                for i in idUser:
                                        try:
                                                await bot.send_message(i[0],text=await Student(self.day+1,self.week,i[0]).shedulDay(),parse_mode='HTML')
                                        except Exception as e:
                                                db.set_active(i[0],0)
                                                print(f"Пользователь {i[0]} заблокировал чат-бота!: {e}")
