from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

rates = InlineKeyboardBuilder()

rates.add(
    types.InlineKeyboardButton(
        text="Пополнить на 50 рублей",
        url="https://google.com"
    )
)

rates.add(
    types.InlineKeyboardButton(
        text="Пополнить на 100 рублей",
        url="https://google.com"
    )
)

rates.add(
    types.InlineKeyboardButton(
        text="Пополнить на 150 рублей",
        url="https://google.com"
    )
)

rates.add(
    types.InlineKeyboardButton(
        text="Пополнить на 500 рублей",
        url="https://google.com"
    )
)

rates.add(
    types.InlineKeyboardButton(
        text="Главное меню",
        callback_data="main_menu"
    )
)



rates.adjust(1)