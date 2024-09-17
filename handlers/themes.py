from aiogram import Router, F
from aiogram.types import CallbackQuery
from kb.themes_kb import get_paginated_keyboard 

router = Router()

@router.callback_query(F.data.contains('dir'))
async def themes(callback: CallbackQuery):
    dir_id = str(callback.data).replace("dir_", '')
    
    await callback.message.delete()
    await callback.message.answer(
        "Выберите нужную тему",
        reply_markup=get_paginated_keyboard(dir_id=dir_id, page=1)
    )

@router.callback_query(F.data.startswith('theme_'))
async def paginate(callback: CallbackQuery):
    _, dir_id, page = callback.data.split('_')
    page = int(page)
    
    kb = get_paginated_keyboard(dir_id=dir_id, page=page)
    
    await callback.message.edit_reply_markup(
        reply_markup=kb
    )
