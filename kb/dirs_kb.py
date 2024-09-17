from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
import requests

def create_dirs_keyboard():
    response = requests.get('http://193.227.240.205:8000/directions/')
    dirs = response.json()
    
    buttons = []
    
    for dir in dirs:
        if dir['is_active']:
            button_text = f"{dir['name']}"
            button_callback = f"dir_{dir['id']}"
            buttons.append(
                types.InlineKeyboardButton(
                    text=button_text,
                    callback_data=button_callback
                )
            )

    return buttons

def get_paginated_keyboard(page: int, page_size: int = 3):
    buttons = create_dirs_keyboard()
    
    keyboard = InlineKeyboardBuilder()
    
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    # Check bounds to avoid index errors
    if start_index < len(buttons):
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
