import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram.types.input_file import BufferedInputFile
from input import token
from fuctions import remove_bg

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: Message, bot: Bot):
    await message.answer('Привет, я бот удаляющий фон, скинь мне картинку и я удалю с нее фон')

@dp.message(F.content_type == ContentType.PHOTO)
async def get_photo(message: Message, bot: Bot):
    photo = message.photo[-1]
    file_name = f'img/Photo_From_{message.from_user.full_name}.png'

    await bot.download(photo, file_name)
   
    remove_bg(file_name)

    with open(file_name, 'rb') as photo_file:
        photo_input = BufferedInputFile(photo_file.read(), file_name)
        await bot.send_document(chat_id=message.chat.id, document=photo_input)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())