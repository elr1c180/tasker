from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

comm = InlineKeyboardBuilder()

comm.add(
    types.InlineKeyboardButton(
        text="Перейти к выбору направления",
        callback_data="directions"
    )
)

comm.add(
    types.InlineKeyboardButton(
        text="Пополнить баланс",
        callback_data="balance"
    )
)

comm.adjust(1)