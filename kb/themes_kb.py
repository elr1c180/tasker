from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
import requests

def create_themes_keyboard(dir_id):
    response = requests.get(f'http://193.227.240.205:8000/directions/{dir_id}/themes')
    themes = response.json()
    
    buttons = []
    
    for theme in themes:
        if theme['is_active']:
            button_text = f"{theme['name']}"
            button_callback = f"theme_{theme['id']}"
            buttons.append(
                types.InlineKeyboardButton(
                    text=button_text,
                    callback_data=button_callback
                )
            )

    return buttons

def get_paginated_keyboard(dir_id, page: int, page_size: int = 3):
    buttons = create_themes_keyboard(dir_id=dir_id)
    
    keyboard = InlineKeyboardBuilder()
    
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    # Check bounds to avoid index errors
    if start_index < len(buttons):
        keyboard.row(*buttons[start_index:end_index])
    
    navigation_buttons = []
    
    if start_index > 0:
        navigation_buttons.append(
            types.InlineKeyboardButton(text="⬅️ Назад", callback_data=f"theme_{dir_id}_{page-1}")
        )
    
    if end_index < len(buttons):
        navigation_buttons.append(
            types.InlineKeyboardButton(text="Вперед ➡️", callback_data=f"theme_{dir_id}_{page+1}")
        )
    
    if navigation_buttons:
        keyboard.row(*navigation_buttons)
    
    keyboard.row(types.InlineKeyboardButton(text="К выбору направлений", callback_data="directions"))
    keyboard.row(types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu"))
    
    return keyboard.as_markup()
