from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
import requests

def create_tariff_keyboard():
    response = requests.get('http://193.227.240.205:8000/tariffs/')
    tariffs = response.json()
    
    menu = InlineKeyboardBuilder()

    for tariff in tariffs:
        if tariff['is_active']:
            button_text = f"{tariff['name']} - {int(tariff['price'])}"
            button_url = "https://www.google.com"  # или URL вашего сервиса
            menu.add(
                types.InlineKeyboardButton(
                    text=button_text,
                    url=button_url
                )
            )

    menu.add(
        types.InlineKeyboardButton(
            text="Главное меню",
            callback_data="main_menu"
        )
    )

    menu.adjust(1)

    return menu
