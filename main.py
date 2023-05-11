from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os

API_TOKEN = '6203385209:AAGE6opfT7GF-l2Vnldcm6bNReMlRh4po5w'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
sound = pyttsx3.init()
voices = sound.getProperty('voices')
one_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Aleksandr"
two_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"

@dp.message_handler(commands=['start'])
async def send_welcome(message: aiogram.types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}🥰! Я могу преобразовывать текст в аудио. Напиши мне текст и мы получим аудио.")
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = KeyboardButton('Иринa')
    item2 = KeyboardButton('Алeксандр')
    item3 = KeyboardButton('Пока нихуя')
    markup.add(item1, item2, item3)

    await message.answer('Выбери голос и напиши сообщение!', reply_markup=markup)
    print(message.text)


@dp.message_handler()
async def send_file(message: aiogram.types.Message):
    print(message.text)

    if message.text == '<':
        sound.save_to_file("Меньше чем", "mp3")
    elif message.text == '>':
        sound.save_to_file("Больше чем", "mp3")
    else:
        sound.save_to_file(message.text, "mp3")
        sound.runAndWait()

    if message.text == "Алeксандр":
        sound.setProperty('voice', one_voice_id)
        os.remove('mp3')
    elif message.text == "Иринa":
        sound.setProperty('voice', two_voice_id)
        os.remove('mp3')


    with open('mp3', 'rb') as audio_file:
        audio_data = audio_file.read()
    await bot.send_audio(chat_id=message.chat.id, audio=audio_data, title='аудио123')
    os.remove('mp3')

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=False)
