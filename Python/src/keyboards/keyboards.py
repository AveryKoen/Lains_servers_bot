from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Использование ресурсов"),
                                     KeyboardButton(text="Логи")]],
                           resize_keyboard=True,
                           input_field_placeholder="Тут есть несколько функций по мониторингу сервера:")