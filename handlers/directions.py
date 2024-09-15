from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from kb.dirs_kb import get_paginated_keyboard 

router = Router()

@router.callback_query(F.data == 'directions')
async def directions(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "Выберите нужное направление",
        reply_markup=get_paginated_keyboard(page=1)
    )

@router.callback_query(F.data.startswith('page_'))
async def paginate(callback: CallbackQuery):
    page = int(callback.data.split('_')[1])
    
    await callback.message.edit_reply_markup(
        reply_markup=get_paginated_keyboard(page=page)
    )
