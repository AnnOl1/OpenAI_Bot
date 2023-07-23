import asyncio # для асинхронного запуска бота
import logging # для настройки логгирования, которое поможет в отладке

from aiogram import Bot, Dispatcher # основной модуль библиотеки aiogram, из которого мы импортируем классы Bot и Dispatcher
from aiogram.enums.parse_mode import ParseMode # содержит настройки разметки сообщений (HTML, Markdown)
from aiogram.fsm.storage.memory import MemoryStorage # хранилища данных для состояний пользователей

import config # настройки бота, пока что только токен
from handlers import router # пока пустой, но скоро мы напишем в нём функционал нашего бота
from aiogram.utils.chat_action import ChatActionMiddleware

async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

dp.message.middleware(ChatActionMiddleware())