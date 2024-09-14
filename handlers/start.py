from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from kb import start

router = Router() 

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"<b>Здравствуйте!</b>\nИмя: {message.from_user.first_name}\nБаланс: 100\nКоличество решеных задач: 100",
        parse_mode='html',
        reply_markup=start.comm.as_markup()
    )
