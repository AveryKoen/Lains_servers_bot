import psutil
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import Python.src.keyboards.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Тут есть несколько функций по мониторингу сервера:", reply_markup=kb.main)

@router.message(F.text == "Использование ресурсов")
@router.message(Command("status"))
async def status(message: Message):
    # Получите информацию о системе
    # uptime = psutil.boot_time()
    cpu_usage = psutil.cpu_percent()
    #cpu_temperature = psutil.sensors_temperatures()
    ram_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    response = (
        f"ЦП/CPU: <b>{cpu_usage}%</b>\n"
        #f"Температура: ({cpu_temperature} - 32 * 5/9 °C)\n"
        f"ОЗУ/RAM: <b>{ram_info.percent}%</b> ({ram_info.used // (1024 ** 2)} MB из {ram_info.total // (1024 ** 2)} MB)\n"
        f"Диск/Drive: <b>{disk_usage.percent}%</b> ({disk_usage.used // (1024 ** 2)} MB из {disk_usage.total // (1024 ** 2)} MB)"
    )
    await message.answer(response)

    if cpu_usage > 90:
        await message.answer(f"⚠️ ЦП/CPU: {cpu_usage}% слишком велико.\n"
                             f"Решение: Проверьте запущенные процессы и уберите ненужные, иначе система может работать нестабильно")
    if disk_usage.percent > 90:
        await message.answer(f"⚠️ Диск/Drive: {disk_usage.percent}% слишком велико.\n"
                             f"Решение: Очистьте диск, иначе система может работать нестабильно")

@router.message(lambda message: message.sticker is not None)
async def handle_sticker(message: Message):
    sticker_info = (
        f"File ID: {message.sticker.file_id}\n"
        f"Set Name: {message.sticker.set_name}"
    )
    await message.answer(sticker_info)