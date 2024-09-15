from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

buttons = [
    types.InlineKeyboardButton(text=str(i), callback_data=f"dir_{i}")
    for i in range(1, 8)
]

def get_paginated_keyboard(page: int, page_size: int = 3):
    keyboard = InlineKeyboardBuilder()
    
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    keyboard.row(*buttons[start_index:end_index])
    
    navigation_buttons = []
    
    if start_index > 0:
        navigation_buttons.append(
            types.InlineKeyboardButton(text="⬅️ Назад", callback_data=f"page_{page-1}")
        )
    
    if end_index < len(buttons):
        navigation_buttons.append(
            types.InlineKeyboardButton(text="Вперед ➡️", callback_data=f"page_{page+1}")
        )
    
    if navigation_buttons:
        keyboard.row(*navigation_buttons)

    keyboard.row(types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu"))
    
    return keyboard.as_markup()

