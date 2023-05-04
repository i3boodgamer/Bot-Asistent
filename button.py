from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton

student=ReplyKeyboardMarkup(resize_keyboard=True)
b_student=KeyboardButton(text='Я Студент')
b_prepod=KeyboardButton(text='Я Преподователь')

student.add(b_student)

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
days_nt=ReplyKeyboardMarkup(keyboard=but,resize_keyboard=True)

subscribe_b=InlineKeyboardMarkup()
subscribe_button = InlineKeyboardButton(text="Подписаться на рассылку", callback_data="subscribe")
del_subscribe_button = InlineKeyboardButton(text="Отказаться от рассылки рассылку", callback_data="not_subscribe")
subscribe_b.add(subscribe_button,del_subscribe_button)



