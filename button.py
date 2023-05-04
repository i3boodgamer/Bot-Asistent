from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton


student=ReplyKeyboardMarkup(resize_keyboard=True)
b_student=KeyboardButton(text='Студент')
student.add(b_student)

group=ReplyKeyboardMarkup(resize_keyboard=True)
group_GG_19=KeyboardButton(text='ГГ-19')
group_GG_20=KeyboardButton(text='ГГ-20')
group_GG_21=KeyboardButton(text='ГГ-21')
group_GG_22=KeyboardButton(text='ГГ-22')

group_GD_201=KeyboardButton(text='ГД-201')
group_GD_202=KeyboardButton(text='ГД-202')
group_GD_203=KeyboardButton(text='ГД-203')
group_GD_211=KeyboardButton(text='ГД-211')
group_GD_212=KeyboardButton(text='ГД-212')
group_GD_213=KeyboardButton(text='ГД-213')
group_GD_221=KeyboardButton(text='ГД-221')

group_GOR_18=KeyboardButton(text='ГОР-18')
group_GOR_19=KeyboardButton(text='ГОР-19')
group_GOR_22=KeyboardButton(text='ГОР-22')

group_GP_18=KeyboardButton(text='ГП-18')
group_GP_19=KeyboardButton(text='ГП-19')
group_GP_21=KeyboardButton(text='ГП-21')
group_GP_22=KeyboardButton(text='ГП-22')
group.add(group_GG_19,
group_GG_20,
group_GG_21,
group_GG_22,
group_GD_201,
group_GD_202)