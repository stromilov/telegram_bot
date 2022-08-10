#Telegram bot


import logging, time, subprocess
#import bot_token
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token="??????")

# Диспетчер для бота
dp = Dispatcher(bot)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /time на распберри
@dp.message_handler(commands = "time")
async def cmd_test1(message: types.Message):
    await message.answer( time.strftime( "%H:%M:%S", time.localtime() ) )


@dp.message_handler(commands = "hello")
async def hello_you(message: types.Message):
    await message.answer("и тебе привет")

@dp.message_handler(commands = "os")
async def os_command(message: types.Message):
    await message.answer(subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True, input="hello").stdout)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
