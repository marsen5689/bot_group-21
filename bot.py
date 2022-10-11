from aiogram import Bot, types, Dispatcher, executor
from config import TOKEN
import keyboards as kb
from list_zoom import *
from trigger_message import *
import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


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
        message_send = await message.answer_photo("https://telegra.ph/file/ac71dafd5350ad0363392.png",
                                                  reply_markup=kb.pn2)
        await asyncio.sleep(180)
        await message.delete()
        await message_send.delete()

    # вызов списка стедентов
    if message.text == '!группа' or message.text == "!студенты" or message.text == "/students" or message.text == "/students@pz11_bot":
        await message.reply(first_half, reply_markup=kb.fisrt_page_button)

    # вызвать список кодеров
    if message.text == '!админы' or message.text == "!разработчики" or message.text == "/adm" or message.text == "/adm@pz11_bot":
        message_send = await message.reply("👨‍💻 Код писали:"
                                           "\n <a href='tg://user?id=1051198514'>🔸Страхов Игорь</a>"
                                           "\n <a href='tg://user?id=562813685'>🔸Мурадян Арсен</a>", parse_mode='HTML')
        await asyncio.sleep(30)
        await message.delete()
        await message_send.delete()

    # * проверить отклик бота
    if message.text == "!бот" or message.text == "!ботик" or message.text == "/bot@pz11_bot" or message.text == "/bot":
        message_send = await bot.send_message(message.chat.id, "Тут")
        await asyncio.sleep(5)
        await message.delete()
        await message_send.delete()

    # * рассписание звонков
    if message.text == "!звонки" or message.text == "/call" or message.text == "/call@pz11_bot":
        message_send = await message.reply(f'{message.from_user.first_name}, {call_message}', parse_mode='HTML')
        await asyncio.sleep(180)
        await message.delete()
        await message_send.delete()

    # переслать ссылки на зум и гугл мит
    if message.chat.id != -1001501756386:
        if 'zoom.us' in message.text:
            message_pin = await bot.send_message(-1001501756386,
                                                 message.text + '\nСсылка на Zoom из группы: ' + message.chat.title)
            await bot.send_message(message.chat.id, 'Ссылка отправлена студентам ✅')
            await message_pin.pin(False)
    if message.chat.id != -1001501756386:
        if 'meet.google.com' in message.text:
            message_pin = await bot.send_message(-1001501756386,
                                                 message.text + '\nСсылка на Google meet из группы: ' + message.chat.title)
            await bot.send_message(message.chat.id, 'Ссылка отправлена студентам ✅')
            await message_pin.pin(False)

    # команда !помощь
    if message.text == '!помощь' or message.text == "/help" or message.text == "/help@pz11_bot":
        message_send = await message.reply(f'{message.from_user.first_name}, {message_help}', parse_mode='HTML')
    # команда ФИО
    if message.text == '/fio' or message.text == '!фио' or message.text == '/fio@pz11_bot':
        message_send = await message.answer('Выбери:', reply_markup=kb.all_button)
        await asyncio.sleep(180)
        await message.delete()
        await message_send.delete()

    if message.text == "!Обнова_в_боте":
        message_send = await message.answer(
            f"📣 Исходный код бота был обновлен 🥳\n\nА это значит что вышло обновление, добавлены следющии функции:\n🔸Появились коды и ссылки на пары в разделе /fio\n🔸Теперь бот умеет удалять сообщения за собой, будут удаляться через 3 минуты следующие команды: /call, /fio, /pr, /adm\n\nЕсли у вас есть предложения по улучшению бота - обращайтесь к разработчикам(/adm).")
        await message.delete()


@dp.callback_query_handler()
async def button(query: types.CallbackQuery):
    if query.data == 'pn':
        media = types.InputMediaPhoto('https://telegra.ph/file/ac71dafd5350ad0363392.png')
        await bot.edit_message_media(media, query.message.chat.id, query.message.message_id, reply_markup=kb.pn2)
    if query.data == 'vt':
        media = types.InputMediaPhoto('https://telegra.ph/file/7bd73ba68968e335c6548.png')
        await bot.edit_message_media(media, query.message.chat.id, query.message.message_id, reply_markup=kb.vt2)
    if query.data == 'sr':
        media = types.InputMediaPhoto('https://telegra.ph/file/f7d61b317d6593100a5d3.png')
        await bot.edit_message_media(media, query.message.chat.id, query.message.message_id, reply_markup=kb.sr2)
    if query.data == 'cht':
        media = types.InputMediaPhoto('https://telegra.ph/file/82a6db2874bbb75ea5a8c.png')
        await bot.edit_message_media(media, query.message.chat.id, query.message.message_id, reply_markup=kb.cht2)
    if query.data == 'pt':
        media = types.InputMediaPhoto('https://telegra.ph/file/b57b76a414f1cb1c4bfce.png')
        await bot.edit_message_media(media, query.message.chat.id, query.message.message_id, reply_markup=kb.pt2)

    if query.data == 'next_page_data':
        await bot.edit_message_text(second_half, query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.second_page_button)

    if query.data == 'back_page_data':
        await bot.edit_message_text(first_half, query.message.chat.id, query.message.message_id,
                                    reply_markup=kb.fisrt1_page_button)

    if query.data == 'math_data':
        await bot.edit_message_text('Математика: Матвейченко Елена Владимировна',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'fizra_data':
        await bot.edit_message_text('Физра: Малик Инна Николаевна',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'history_data':
        await bot.edit_message_text('История Украины: Гуленко Людмила Филипповна',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'eng_data':
        await bot.edit_message_text('Английский:\nИгнатьева  Наталия Викторовна\n'
                                    'Каташов Олександр Анатольевич.',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'ua_data':
        await bot.edit_message_text('Укр яз и лит: Волкова Лилия Владимировна.',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'ph_data':
        await bot.edit_message_text('Физика:\nСеменченко Татьяна Александровна.\n\n'
                                    'Астрономия:\nКорнеева Ирина Анатаоливна',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'BJD_data':
        await bot.edit_message_text('БЖД: Мирошиченко Юрий Викторович.',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'info_data':
        await bot.edit_message_text('Инф.технологии: Беликова Виктория Викторовна.',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'gr_data':
        await bot.edit_message_text('Гром.освита: Оксененко Светлана Петровна',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'tech_data':
        await bot.edit_message_text('Технологии: Милютина Ольга Святославовна',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'tks_data':
        await bot.edit_message_text('ОС ТКС: Качуров Вячеслав Евгеньевич',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'bio_data':
        await bot.edit_message_text('Биология: Каплун Елена Анатольевна',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'ect_data':
        await bot.edit_message_text('ТЭЦ: Беликова Станислава Олеговна',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.second_keyboard)

    if query.data == 'back_data':
        await bot.edit_message_text('Выбери предмет: ',
                                    query.message.chat.id, query.message.message_id, reply_markup=kb.all_button)

    if query.data == 'code_data':
        if 'Математика' in query.message.text:
            await bot.edit_message_text(f'Математика: Матвейченко Елена Владимировна\n\n'
                                        f'Код конференции: <code>{math_code}</code>\n'
                                        f'Код доступа: <code>{math_password}</code>\n'
                                        f'<a href="https://us05web.zoom.us/j/6032452922?pwd=ZjNZRlJJempEaW5vQ1Y3MDJuWlQvUT09">Open Zoom</a>',
                                        query.message.chat.id, query.message.message_id, disable_web_page_preview=True,
                                        reply_markup=kb.third_keyboard,
                                        parse_mode='HTML')

        if 'Физра' in query.message.text:
            await bot.edit_message_text(f'Физра: Малик Инна Николаевна\n\n'
                                        f'Код конференции: <code>{pe_code}</code>\n'
                                        f'Код доступа: <code>{pe_password}</code>',
                                        query.message.chat.id, query.message.message_id, reply_markup=kb.third_keyboard,
                                        parse_mode='HTML')

        if 'История Украины' in query.message.text:
            await bot.edit_message_text(f'История Украины: Гуленко Людмила Филипповна\n\n'
                                        f'Код конференции: <code>{history_code}</code>\n'
                                        f'Код доступа: <code>{history_password}</code>\n'
                                        f'<a href="https://us05web.zoom.us/j/3623752350?pwd=MXcxS0lhYU1RYUdTUGVDeGFIbGtZUT09">Open Zoom</a>',
                                        query.message.chat.id, query.message.message_id, disable_web_page_preview=True,
                                        reply_markup=kb.third_keyboard,
                                        parse_mode='HTML')

        if 'Физика' in query.message.text:
            await bot.edit_message_text(f'Физика: Семенченко Татьяна Александровна\n'
                                        f'Код конференции: <code>{physics_code}</code>\n'
                                        f'Код доступа: <code>{physics_password}</code>\n'
                                        f'<a href="https://us05web.zoom.us/j/6105813910?pwd=Nld5MlBLSmdKaG4rZFA3UVNkMkNOZz09">Open Zoom</a>\n\n'
                                        f'Астрономия: Корнеева Ирина Анатаоливна\n'
                                        f'Код конференции: <code>{ast_code}</code>\n'
                                        f'Код доступа: <code>{ast_password}</code>\n'
                                        f'<a href="https://us05web.zoom.us/j/2380384754?pwd=MVRxdGpoM2FPd3BYcUU3VlJFQW4wUT09">Open Zoom</a>',
                                        query.message.chat.id, query.message.message_id, disable_web_page_preview=True,
                                        reply_markup=kb.third_keyboard,
                                        parse_mode='HTML')

        if 'Английский' in query.message.text:
            await bot.edit_message_text(f'Английский язык:\n'
                                        f'Игнатьева  Наталия Викторовна: <a href="meet.google.com/ghe-fvss-rwo">Google Meet</a>\n'
                                        f'Каташов Олександр Анатольевич: <a href="meet.google.com/pwc-cdjj-xjp">Google Meet</a> ',
                                        query.message.chat.id, query.message.message_id,
                                        reply_markup=kb.third_keyboard, disable_web_page_preview=True,
                                        parse_mode='HTML')

        if 'Укр яз и лит' in query.message.text:
            await bot.edit_message_text(f'Укр яз и лит: Волкова Лилия Владимировна\n\n'
                                        f'Код конференции: <code>{ua_code}</code>\n'
                                        f'Код доступа: <code>{ua_password}</code>\n'
                                        f'<a href="https://us04web.zoom.us/j/9651861969?pwd=TW1BaWdRSVExNzBPaHk4T2t1emxpQT09 ">Open Zoom</a>',
                                        query.message.chat.id, query.message.message_id, disable_web_page_preview=True,
                                        reply_markup=kb.third_keyboard,
                                        parse_mode='HTML')

        if 'БЖД' in query.message.text:
            await bot.edit_message_text(
                f'БЖД: Мирошиченко Юрий Викторович: <a href="meet.google.com/ogw-qguh-tyu">Google Meet</a>',
                query.message.chat.id, query.message.message_id,
                reply_markup=kb.third_keyboard, disable_web_page_preview=True,
                parse_mode='HTML')

        if 'Инф.технологии' in query.message.text:
            await bot.edit_message_text(f'Инф.технологии: Беликова Виктория Викторовна\n\n'
                                        f'Код конференции: <code>{info_code}</code>\n'
                                        f'Код доступа:<code>{info_password}</code>\n'
                                        f'<a href="https://us05web.zoom.us/j/3746736250?pwd=S2dvc25vSXJGeXJCYXd3T3pxMlNHUT09">Open Zoom</a>',
                                        query.message.chat.id, query.message.message_id, disable_web_page_preview=True,
                                        reply_markup=kb.third_keyboard,
                                        parse_mode='HTML')

        if 'Гром.освита' in query.message.text:
            await bot.edit_message_text(f'Гром.освита: Оксененко Светлана Петровна\n\n'
                                        f'Код конференции: <code>{grom_code}</code>\n'
                                        f'Код доступа:<code>{grom_password}</code>',
                                        query.message.chat.id, query.message.message_id,
                                        reply_markup=kb.third_keyboard,
                                        parse_mode='HTML')

        if 'Технологии' in query.message.text:
            await bot.edit_message_text(f'Технологии: Милютина Ольга Святославовна\n\n'
                                        f'Код конференции: <code>{tech_code}</code>\n'
                                        f'Код доступа:<code>{tech_password}</code>\n'
                                        f'<a href="https://us04web.zoom.us/j/4606731017?pwd=1uiAKZ1BzgAZhJawjyd1WldxIbHi8b.1">Open Zoom</a>',
                                        query.message.chat.id, query.message.message_id, disable_web_page_preview=True,
                                        reply_markup=kb.third_keyboard,
                                        parse_mode='HTML')

        if 'ОС ТКС' in query.message.text:
            await bot.edit_message_text(f'ОС ТКС: Качуров Вячеслав Евгеньевич\n\n'
                                        f'<a href="discord.gg/kBGHsUj3">Discord</a>',
                                        query.message.chat.id, query.message.message_id,
                                        reply_markup=kb.third_keyboard, disable_web_page_preview=True,
                                        parse_mode='HTML')

        if 'Биология' in query.message.text:
            await bot.edit_message_text(f'Биология: Каплун Елена Анатольевна\n\n'
                                        f'Код конференции: <code>{bio_code}</code>\n'
                                        f'Код доступа:<code>{bio_password}</code>\n'
                                        f'<a href="https://us04web.zoom.us/j/5698912902?pwd=Ia6IrL0bfl0JP1PxidpDWdD4YKrRUO.1">Open Zoom</a>',
                                        query.message.chat.id, query.message.message_id, disable_web_page_preview=True,
                                        reply_markup=kb.third_keyboard,
                                        parse_mode='HTML')

        if 'ТЭЦ' in query.message.text:
            await bot.edit_message_text(f'ТЭЦ: Беликова Станислава Олеговна\n\n'
                                        f'Код конференции: <code>{ect_code}</code>\n'
                                        f'Код доступа:<code>{ect_password}</code>\n'
                                        f'<a href="https://us05web.zoom.us/j/86829275931?pwd=THVRLzdLUllveGlEY0J5aEVzSjQ5UT09">Open Zoom</a>',
                                        query.message.chat.id, query.message.message_id, disable_web_page_preview=True,
                                        reply_markup=kb.third_keyboard,
                                        parse_mode='HTML')


if __name__ == '__main__':
    executor.start_polling(dp)
