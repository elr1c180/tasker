from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from kb.themes_kb import get_paginated_keyboard 

router = Router()

@router.callback_query(F.data.contains('dir'))
async def themes(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "Выберите нужную тему",
        reply_markup=get_paginated_keyboard(page=1)
    )

@router.callback_query(F.data.startswith('themePage_'))
async def paginate(callback: CallbackQuery):
    page = int(callback.data.split('_')[1])
    
    await callback.message.edit_reply_markup(
        reply_markup=get_paginated_keyboard(page=page)
    )
