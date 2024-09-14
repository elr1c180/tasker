from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

comm = InlineKeyboardBuilder()
comm.add(
    types.InlineKeyboardButton(
        text="Перейти к выбору направления",
        callback_data=""
    )
)
comm.add(
    types.InlineKeyboardButton(
        text="Пополнить баланс",
        callback_data=""
    )
)

comm.adjust(1)