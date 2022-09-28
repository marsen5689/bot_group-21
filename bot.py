from email import message
from aiogram import Bot, types
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
import keyboards as kb
from trigger_message import message_help, first_half, message_start, second_half, call_message
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# [](tg://user?id=chat_id)


@dp.message_handler(content_types='text')
async def forward(message: types.Message):
    # реакция на /start
    if message.text == "/start":
        await message.reply(f'{message.from_user.first_name}, {message_start}', parse_mode='HTML')

    # узнать свой id и id группы
    if message.text == '/id' or message.text == "!id" or message.text == "!ид" or message.text == "/id@pz11_bot":
        await message.reply(f"Твой id: {message.from_user.id}\nЧат id: `{message.chat.id}`", parse_mode="MarkdownV2")

    # вызов рассписания
    if message.text == '!пары' or message.text == "/pr" or message.text == "/pr@pz11_bot":
        message_send = await message.answer_photo("https://telegra.ph/file/6f4cbad77f99e7fa810ea.png", reply_markup=kb.pn2)
        await message.delete()
        await asyncio.sleep(8)
        await message_send.delete()

    # вызов списка стедентов
    if message.text == '!группа' or message.text == "!студенты" or message.text == "/students" or message.text == "/students@pz11_bot":
        await message.reply(first_half, reply_markup=kb.fisrt_page_button)
        
    # вызвать список кодеров
    if message.text == '!админы' or message.text == "!разработчики" or message.text == "/adm" or message.text == "/adm@pz11_bot":
        await message.reply("👨‍💻 Код писали:"
                            "\n <a href='tg://user?id=1051198514'>🔸Страхов Игорь</a>"
                            "\n <a href='tg://user?id=562813685'>🔸Мурадян Арсен</a>", parse_mode='HTML')

    # проверить отклик бота
    if message.text == "!бот" or message.text == "!ботик" or message.text == "/bot@pz11_bot" or message.text == "/bot" :
        message_send = await bot.send_message(message.chat.id, "Тут")
        await message.delete()
        await asyncio.sleep(3)
        await message_send.delete()


    # * рассписание звонков
    if message.text == "!звонки" or message.text == "/call" or message.text == "/call@pz11_bot":
        message_send = await message.reply(f'{message.from_user.first_name}, {call_message}', parse_mode='HTML')
        await asyncio.sleep(5)
        await message_send.delete()

    # переслать ссылки на зум и гугл мит
    if message.chat.id != -1001501756386:
        if 'zoom.us' in message.text:
            message_pin = await bot.send_message(-1001501756386, message.text + '\nСсылка на Zoom из группы: ' + message.chat.title)
            await bot.send_message(message.chat.id, 'я отправил ссылку студентам ✅')
            await message_pin.pin(False)
    if message.chat.id != -1001501756386:
        if 'meet.google.com' in message.text:
            message_pin = await bot.send_message(-1001501756386, message.text + '\nСсылка на Google meet из группы: ' + message.chat.title)
            await bot.send_message(message.chat.id, 'я отправил ссылку студентам ✅')
            await message_pin.pin(False)

    # команда !помощь
    if message.text == '!помощь' or message.text == "/help" or message.text == "/help@pz11_bot":
        await message.reply(f'{message.from_user.first_name}, {message_help}', parse_mode='HTML')
    # команда ФИО
    if message.text == '/fio' or message.text == '!фио' or message.text == '/fio@pz11_bot':
        await message.answer('Выбери:', reply_markup=kb.all_button)
    

@dp.callback_query_handler()
async def button(query: types.CallbackQuery):
    if query.data == 'pn':
        media = types.InputMediaPhoto('https://telegra.ph/file/6f4cbad77f99e7fa810ea.png')
        await bot.edit_message_media(media, query.message.chat.id, query.message.message_id, reply_markup=kb.pn2)
    if query.data == 'vt':
        media = types.InputMediaPhoto('https://telegra.ph/file/81ab8b5b475dcb00798ff.png')
        await bot.edit_message_media(media, query.message.chat.id, query.message.message_id, reply_markup=kb.vt2)
    if query.data == 'sr':
        media = types.InputMediaPhoto('https://telegra.ph/file/82ae56b5c61854dbd5ef5.png')
        await bot.edit_message_media(media, query.message.chat.id, query.message.message_id, reply_markup=kb.sr2)
    if query.data == 'cht':
        media = types.InputMediaPhoto('https://telegra.ph/file/97a0f47b56f0abc7451ff.png')
        await bot.edit_message_media(media, query.message.chat.id, query.message.message_id, reply_markup=kb.cht2)
    if query.data == 'pt':
        media = types.InputMediaPhoto('https://telegra.ph/file/d4118ae8cbd5c10306a50.png')
        await bot.edit_message_media(media, query.message.chat.id, query.message.message_id, reply_markup=kb.pt2)

    # список студентов
    if query.data == 'next_page_data':      
        await bot.edit_message_text(second_half, query.message.chat.id, query.message.message_id, reply_markup=kb.second_page_button)

    if query.data == 'back_page_data':
        await bot.edit_message_text(first_half, query.message.chat.id, query.message.message_id, reply_markup=kb.fisrt1_page_button)     

    # кнопки с фио преподавателей
    if query.data == 'math_data':
        await bot.edit_message_text('Математика: Матвейченко Елена Владимировна', query.message.chat.id,
                                    query.message.message_id, reply_markup=kb.all_button)
    if query.data == 'fizra_data':
        await bot.edit_message_text('Физра: Малик Инна Николаевна', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

    if query.data == 'history_data':
        await bot.edit_message_text('История Украины: Гуленко Людмила Филипповна', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

    if query.data == 'eng_data':
        await bot.edit_message_text('Английский:\nИгнатьева  Наталия Викторовна\n'
                                    'Каташов Олександр Анатольевич.', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

    if query.data == 'ua_data':
        await bot.edit_message_text('Укр яз и лит: Волкова Лилия Владимировна.', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

    if query.data == 'ph_data':
        await bot.edit_message_text('Физика:\nСеменченко Татьяна Александровна.\n'
                                    'Корнеева Ирина Анатаоливна', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

    if query.data == 'BJD_data':
        await bot.edit_message_text('БЖД: Мирошиченко Юрий Викторович.', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

    if query.data == 'info_data':
        await bot.edit_message_text('Инф.технологии: Беликова Виктория Викторовна.', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

    if query.data == 'gr_data':
        await bot.edit_message_text('Гром.освита: Оксененко Светлана Петровна', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

    if query.data == 'tech_data':
        await bot.edit_message_text('Технологии: Милютина Ольга Святославовна', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

    if query.data == 'tks_data':
        await bot.edit_message_text('ОС ТКС: Качуров Вячеслав Евгеньевич', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

    if query.data == 'bio_data':
        await bot.edit_message_text('Биология: Каплун Елена Анатольевна', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

    if query.data == 'ect_data':
        await bot.edit_message_text('ТЭЦ: Беликова Станислава Олеговна', query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.all_button)

if __name__ == '__main__':
    executor.start_polling(dp)
# 