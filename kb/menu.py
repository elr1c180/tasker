from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

menu = InlineKeyboardBuilder()

menu.add(
    types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="main_menu"
    )
)

menu.adjust(1)