from aiogram.types import KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_hi = KeyboardButton('/shn')

pn = InlineKeyboardButton('Понедельник', callback_data='pn')
vt = InlineKeyboardButton('Вторник', callback_data='vt')
sr = InlineKeyboardButton('Среда', callback_data='sr')
cht = InlineKeyboardButton('Четверг', callback_data='cht')
pt = InlineKeyboardButton('Пятница', callback_data='pt')

# c ромбиком
pn1 = InlineKeyboardButton('🔹Понедельник', callback_data='pn')
vt1 = InlineKeyboardButton('🔹Вторник', callback_data='vt')
sr1 = InlineKeyboardButton('🔹Среда', callback_data='sr')
cht1 = InlineKeyboardButton('🔹Четверг', callback_data='cht')
pt1 = InlineKeyboardButton('🔹Пятница', callback_data='pt')

pn2 = InlineKeyboardMarkup().add(pn1, vt, sr, cht, pt)
vt2 = InlineKeyboardMarkup().add(pn, vt1, sr, cht, pt)
sr2 = InlineKeyboardMarkup().add(pn, vt, sr1, cht, pt)
cht2 = InlineKeyboardMarkup().add(pn, vt, sr, cht1, pt)
pt2 = InlineKeyboardMarkup().add(pn, vt, sr, cht, pt1)

# Список студентов
page = InlineKeyboardButton("Страница: ", callback_data="page")
first_page = InlineKeyboardButton("1/2", callback_data="first_page_data")
second_page = InlineKeyboardButton("2/2", callback_data="second_page_data")
back_page_first = InlineKeyboardButton("Назад ⬅️", callback_data="back_page_data")
next_page_two = InlineKeyboardButton("Дальше ▶️", callback_data="next_page_data")
fisrt_page_button = InlineKeyboardMarkup().add(page, first_page).add(next_page_two)
fisrt1_page_button = InlineKeyboardMarkup().add(page, first_page).add(next_page_two)
second_page_button = InlineKeyboardMarkup().add(page, second_page).add(back_page_first)

# Название предметов
math = InlineKeyboardButton('Математика', callback_data='math_data')
fizra = InlineKeyboardButton('Физ-ра', callback_data='fizra_data')
history = InlineKeyboardButton('История Украины', callback_data='history_data')
eng = InlineKeyboardButton('Англ.яз', callback_data='eng_data')
ua = InlineKeyboardButton('Украинский язык и литература', callback_data='ua_data')
physics = InlineKeyboardButton('Физика', callback_data='ph_data')
BJD = InlineKeyboardButton('БЖД', callback_data='BJD_data')
info = InlineKeyboardButton('Инф.технологии', callback_data='info_data')
gr = InlineKeyboardButton('Гром.Освита', callback_data='gr_data')
Tech = InlineKeyboardButton('Технологии', callback_data='tech_data')
TKS = InlineKeyboardButton('ОС ТКС', callback_data='tks_data')
Biology = InlineKeyboardButton('Биология', callback_data='bio_data')
ECT = InlineKeyboardButton('ТЭЦ', callback_data='ect_data')

# Создаем клавиатуру кнопок
all_button = InlineKeyboardMarkup().add(math, physics)\
    .add(history, info)\
    .add(ua)\
    .add(fizra, BJD, eng)\
    .add(gr, Tech)\
    .add(TKS, ECT)\
    .add(Biology)

button_zoom = InlineKeyboardButton('Ссылка', callback_data='code_data')
back_button = InlineKeyboardButton('Назад', callback_data='back_data')

second_keyboard = InlineKeyboardMarkup().add(back_button, button_zoom)
third_keyboard = InlineKeyboardMarkup().add(back_button)