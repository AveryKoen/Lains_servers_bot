import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from Configuration.config import BOT_TOKEN
from handlers.handlers import router
import logging
logging.basicConfig(level=logging.DEBUG)

async def main():
    bot = Bot(
        token=BOT_TOKEN, #Импортируем токен, чтобы никто его не смог украсть
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML  # Включаем распознавание HTML-разметки
            # тут ещё много других интересных настроек можно сделать
        )
    )
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        while True:
            asyncio.run(main())
    except KeyboardInterrupt:
         print("You pressed CTRL + C.")
    finally: print("Bot is stopped")

