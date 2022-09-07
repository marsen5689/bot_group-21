from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# [](tg://user?id=chat_id)

# первая страница списка студентов
first_half = (
    f"🧑‍🎓1.  Бичков Михайло\n"
    f"🧑‍🎓2.  Бідило Віктор\n"   
    f"🧑‍🎓3.  Білоусов Дмитро\n"   
    f"🧑‍🎓4.  Богданов Олексій\n" 
    f"👩‍🎓5.  Бочарова Вікторія\n"     
    f"🧑‍🎓6.  Жукотський Микита\n"   
    f"🧑‍🎓7.  Іванченко Богдан\n"   
    f"🧑‍🎓8.  Ісаєнко  Гліб\n"  
    f"👩‍🎓9.  Колесник Олександра\n"   
    f"🧑‍🎓10.  Кудиненко Кирило\n"    
    f"🧑‍🎓11.  Курило   Ярослав\n"  
    f"🧑‍🎓12.  Мокренко Костянтин\n"    
    f"🧑‍🎓13.  Мурадян Арсеній\n"
    f"👩‍🎓14.  Остапенко Анжела\n")


# вторая страница списка студентов
second_half = (
    f"🧑‍🎓15.  Петрик Олександр\n"
    f"🧑‍🎓16.  Печеньов Артем\n"
    f"🧑‍🎓17.  Полянський Руслан\n" 
    f"🧑‍🎓18.  Прокудін Ігор\n"
    f"🧑‍🎓19.  Пряницький Олексій\n"
    f"🧑‍🎓20.  Рало Ілля\n"
    f"👩‍🎓21.  Рябовол Диана\n"
    f"🧑‍🎓22.  Страхов  Ігор\n"
    f"🧑‍🎓23.  Сударев Игорь\n"
    f"🧑‍🎓24.  Тарсуков Данило\n"
    f"👩‍🎓25.  Царькова Дарина\n"
    f"🧑‍🎓26.  Шахов Кирило\n"
    f"🧑‍🎓27.  Шеховцов Роман\n"
    f"🧑‍🎓28.  Шимкевич Ярослав")


@dp.message_handler(content_types='text')
async def forward(message: types.Message):
    # реакция на /start
    if message.text == "/start":
        await message.reply(f"{message.from_user.first_name}, я предназначен только для группы <pre>ПЗ-11</pre>"
                            f"\nХочешь узнать расписание? Напиши <code>!пары</code>, и я вышлю тебе фото."
                            f"\n\nТак же я умею пересылать ссылку на пары из одной группы в другую и закреплять сообщение там."
                            f"\nВесь функционал бота можно узнать по команде /help"
                            f"\n---\n👨‍💻 Код писали: \n<a href='tg://user?id=1051198514'>🔸Игорь</a>"
                            f"\n<a href='tg://user?id=562813685'>🔸Арсен</a>", parse_mode='HTML')

    # узнать свой id и id группы
    if message.text == '/id' or message.text == "!id" or message.text == "!ид" or message.text == "/id@pz11_bot":
        await message.reply(f"Твой id: {message.from_user.id}\nЧат id: `{message.chat.id}`", parse_mode="MarkdownV2")

    # вызов рассписания
    if message.text == '!пары' or message.text == "/pr" or message.text == "/pr@pz11_bot":
        await message.answer_photo("https://telegra.ph/file/6f4cbad77f99e7fa810ea.png", reply_markup=kb.pn2)

    # вызов списка стедентов
    if message.text == '!группа' or message.text == "!студенты" or message.text == "/students" or message.text == "/students@pz11_bot":
        await message.reply(first_half, reply_markup=kb.fisrt_page_button)
        
    # вызвать список кодеров
    if message.text == '!админы' or message.text == "!разработчики" or message.text == "/adm" or message.text == "/adm@pz11_bot":
        await message.reply("👨‍💻 Код писали:"
                            "\n <a href='tg://user?id=1051198514'>🔸Страхов Игорь</a>"
                            "\n <a href='tg://user?id=562813685'>🔸Мурадян Арсен</a>", parse_mode='HTML')

    # проверить отклик бота
    if message.text == "!бот" or message.text == "!ботик" or message.text == "/bot@pz11_bot":
        await message.reply("На месте")

    # рассписание звонков
    if message.text == "!звонки" or message.text == "/call" or message.text == "/call@pz11_bot":
        await message.reply(f"{message.from_user.first_name}, расписание звонков:"
                            f"\n1️⃣ пара: 8:30 - 9:50"
                            f"\n2️⃣ пара: 10:00 - 11:20"
                            f"\n3️⃣ пара: 11:50 - 13:10"
                            f"\n4️⃣ пара: 13:20 - 14:40"
                            f"\n5️⃣ пара: 14:50 - 16:10 ")

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
        await message.reply(f'{message.from_user.first_name}, все команды указываются через !название команды или /название команды\n'
                            f"----------\n"
                            f'Список команд:\n'
                            f'🆔 !id | /!id - Показывает ваш id и id группы.\n'
                            f'🗓 !пары | /pr - Выдает меню где можно посмотреть расписание.\n'
                            f'🔔 !звонки | /call - Показывает расписание звонков.\n'
                            f'🎓 !студенты | /students - Список стдентов в группе ПЗ - 11.\n'
                            f'🎓 !фио | /fio - Показывает ФИО преподавателей\n'
                            f'👨‍💻 !разработчики | /adm - Показывает кто разработал этого бота.\n \n'
                            f'Если у вас есть предложения по улучшению бота-обращайтесь к разработчикам.')
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
