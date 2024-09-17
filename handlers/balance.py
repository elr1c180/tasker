from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from kb import tarrifs

router = Router() 

@router.callback_query(F.data == 'balance')
async def balance(callback: CallbackQuery):
    kb = tarrifs.create_tariff_keyboard()
    await callback.message.delete()
    await callback.message.answer(
        f"Выберете подходящий для вас тариф",
        parse_mode='html',
        reply_markup=kb.as_markup()
    )
