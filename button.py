from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton

people=ReplyKeyboardMarkup(resize_keyboard=True)
b_student=KeyboardButton(text='Я Студент')
b_prepod=KeyboardButton(text='Я Преподаватель')

people.add(b_student,b_prepod)

group=ReplyKeyboardMarkup(resize_keyboard=True)
group_In_21=KeyboardButton(text='ИЭ-21')
group_IVT_211=KeyboardButton(text='ИВТ-211')
group_IVT_212=KeyboardButton(text='ИВТ-212')
group_IC_211=KeyboardButton(text='ИС-211')
group_IC_212=KeyboardButton(text='ИС-212')
group_IPMI_21=KeyboardButton(text='ИПМИ-21')
group_IP_21=KeyboardButton(text='ИП-21')
group_IAT_21=KeyboardButton(text='ИАТ-21')
back=KeyboardButton(text='Назад')
but_group=[[group_In_21],[group_IVT_212],[group_IVT_211],[group_IC_211],[group_IC_212],[group_IPMI_21],[group_IP_21],[group_IAT_21],[back]]
group=ReplyKeyboardMarkup(keyboard=but_group,resize_keyboard=True)


institut=InlineKeyboardMarkup()
ITiAS=InlineKeyboardButton(text="ИТиАС", callback_data="ITiAS")
institut.add(ITiAS)

group_in=InlineKeyboardMarkup()
group_In_21_in=InlineKeyboardButton(text='ИЭ-21')
group_IVT_211_in=InlineKeyboardButton(text='ИВТ-211',callback_data="IVT-211")
group_IVT_212_in=InlineKeyboardButton(text='ИВТ-212',callback_data="IVT_212")
group_IC_211_in=InlineKeyboardButton(text='ИС-211',callback_data="IC_211")
group_IC_212_in=InlineKeyboardButton(text='ИС-212',callback_data="IC_212")
group_IPMI_21_in=InlineKeyboardButton(text='ИПМИ-21',callback_data="IPMI_21")
group_IP_21_in=InlineKeyboardButton(text='ИП-21',callback_data="IP_21")
group_IAT_21_in=InlineKeyboardButton(text='ИАТ-21',callback_data="IAT_21")
but_group_in=(group_IVT_212_in,group_IVT_211_in,group_IC_211_in,group_IC_212_in,group_IPMI_21_in,group_IP_21_in,group_IAT_21_in)
group_in.add(but_group_in)

pn=KeyboardButton(text='На сегодня')
vt=KeyboardButton(text='На завтра')
all_rs=KeyboardButton(text='На всю неделю')
all_rs_next=KeyboardButton(text='На следующую неделю')
options=KeyboardButton(text='Настроить рассылку расписания')
back=KeyboardButton(text='Назад')
but=[[pn], [vt],[all_rs],[all_rs_next],[options],[back]]
daysSheduleButtonStudent=ReplyKeyboardMarkup(keyboard=but,resize_keyboard=True)
but_p=[[pn], [vt],[all_rs],[all_rs_next],[back]]
daysSheduleButtonTeacher=ReplyKeyboardMarkup(keyboard=but_p,resize_keyboard=True)



subscribeButton=InlineKeyboardMarkup()
subscribe_button = InlineKeyboardButton(text="Подписаться на рассылку", callback_data="subscribe")
del_subscribe_button = InlineKeyboardButton(text="Отказаться от рассылки рассылку", callback_data="not_subscribe")
subscribeButton.add(subscribe_button,del_subscribe_button)

teacherNameButton=ReplyKeyboardMarkup()
prepod1=KeyboardButton(text='Киселева Т. В.')
prepod2=KeyboardButton(text='Буинцев В. Н.')
prepod3=KeyboardButton(text='Богдановская Д. Е.')
prepod4=KeyboardButton(text='Белый А. М.')
prepod5=KeyboardButton(text='Беланцева Д.Ю.')
prepod6=KeyboardButton(text='Кожемяченко В. И.')
prepod7=KeyboardButton(text='Мартусевич Е. А.')
prepod8=KeyboardButton(text='Рыжих А. Ю.')
prepod9=KeyboardButton(text='Соловьева Ю. А.')
prepod10=KeyboardButton(text='Четвертков Е. В.')
teacherNameButton.add(prepod1,prepod2,prepod3,prepod4,prepod5,prepod6,prepod7,prepod8,prepod9,prepod10,back)






