import random

from telebot import types

from const import START_BUTTON

help_menu = types.InlineKeyboardMarkup()
not_text_menu = types.InlineKeyboardMarkup()
start_menu = types.InlineKeyboardMarkup()
olymp_menu = types.InlineKeyboardMarkup()
olymp_menu2 = types.InlineKeyboardMarkup()
random_olymp_menu = types.InlineKeyboardMarkup()
menu_menu = types.InlineKeyboardMarkup()
levels_menu = types.InlineKeyboardMarkup()
prepare_menu = types.InlineKeyboardMarkup()
advantages_menu = types.InlineKeyboardMarkup()
update_subj_menu = types.InlineKeyboardMarkup()
update_class_menu = types.InlineKeyboardMarkup()
admin_menu = types.InlineKeyboardMarkup()
admin_send_text = types.InlineKeyboardMarkup()
admin_confirmation_text = types.InlineKeyboardMarkup()
go_out_menu = types.InlineKeyboardMarkup()
olymp_levels_menu = types.InlineKeyboardMarkup()

btn1 = types.InlineKeyboardButton(text=f'🏆 Олимпиада по профилю, классу и уровню', callback_data='olymp')
btn2 = types.InlineKeyboardButton(text=f'✅ Рандомная олимпиада', callback_data='random_olymp_menu')
btn3 = types.InlineKeyboardButton(text=f'🔥 Уровни, этапы и льготы', callback_data='levels')
btn4 = types.InlineKeyboardButton(text=f'📘 Как готовиться и решать олимпиады', callback_data='how_prepare')
btn5 = types.InlineKeyboardButton(text=f'😎 Преимущества участия в олимпиадах', callback_data='advantages')
btn6 = types.InlineKeyboardButton(text=f'❌️ Вернуться в меню', callback_data='menu')
btn7 = types.InlineKeyboardButton(text=f'😎 {START_BUTTON[random.randint(0, len(START_BUTTON) - 1)]}',
                                  callback_data='menu')
btn8 = types.InlineKeyboardButton(text=f'⚙️ Что я умею', callback_data='help')
btn9 = types.InlineKeyboardButton(text=f'⭐️ Еще одна олимпиада', callback_data='olymp')
btn10 = types.InlineKeyboardButton(text=f'🔄 Другой предмет или класс', callback_data='update')
btn11 = types.InlineKeyboardButton(text=f'⭐️ Еще одна олимпиада', callback_data='random_olymp_menu')
btn12 = types.InlineKeyboardButton(text=f"Астрономия", callback_data='astronomy')
btn13 = types.InlineKeyboardButton(text=f'Бизнес', callback_data='business')
btn14 = types.InlineKeyboardButton(text=f'Биология', callback_data='biology')
btn15 = types.InlineKeyboardButton(text=f'География', callback_data='geography')
btn16 = types.InlineKeyboardButton(text=f'Журналистика', callback_data='journalism')
btn17 = types.InlineKeyboardButton(text=f'Искусство', callback_data='art')
btn18 = types.InlineKeyboardButton(text=f'Иностранный язык', callback_data='foreign_lang')
btn19 = types.InlineKeyboardButton(text=f'Информатика', callback_data='informatics')
btn20 = types.InlineKeyboardButton(text=f'История', callback_data='history')
btn20_1 = types.InlineKeyboardButton(text=f'Лингвистика', callback_data='linguistics')
btn21 = types.InlineKeyboardButton(text=f'Литература', callback_data='literature')
btn22 = types.InlineKeyboardButton(text=f'Математика', callback_data='math')
btn23 = types.InlineKeyboardButton(text=f'Музыка', callback_data='music')
btn24 = types.InlineKeyboardButton(text=f'Обществознание', callback_data='social')
btn25 = types.InlineKeyboardButton(text=f'Право', callback_data='law')
btn26 = types.InlineKeyboardButton(text=f'Русский язык', callback_data='russian_lang')
btn27 = types.InlineKeyboardButton(text=f'Социология', callback_data='sociology')
btn27_1 = types.InlineKeyboardButton(text=f'Технология', callback_data='technology')
btn28 = types.InlineKeyboardButton(text=f'Физика', callback_data='physics')
btn29 = types.InlineKeyboardButton(text=f'Химия', callback_data='chemistry')
btn30 = types.InlineKeyboardButton(text=f'Экономика', callback_data='economy')
btn31 = types.InlineKeyboardButton(text=f"2", callback_data='2')
btn32 = types.InlineKeyboardButton(text=f"3", callback_data='3')
btn33 = types.InlineKeyboardButton(text=f"4", callback_data='4')
btn34 = types.InlineKeyboardButton(text=f"5", callback_data='5')
btn35 = types.InlineKeyboardButton(text=f"6", callback_data='6')
btn36 = types.InlineKeyboardButton(text=f"7", callback_data='7')
btn37 = types.InlineKeyboardButton(text=f"8", callback_data='8')
btn38 = types.InlineKeyboardButton(text=f"9", callback_data='9')
btn39 = types.InlineKeyboardButton(text=f"10", callback_data='10')
btn40 = types.InlineKeyboardButton(text=f"11", callback_data='11')
btn41 = types.InlineKeyboardButton(text=f"Получить базу данных", callback_data='admin_get_db')
btn42 = types.InlineKeyboardButton(text=f"Первые 20 пользователей", callback_data='admin_20_users')
btn43 = types.InlineKeyboardButton(text=f"Все пользователи", callback_data='admin_all_users')
btn44 = types.InlineKeyboardButton(text=f"Отправить сообщение всем пользователям", callback_data='admin_start_message')
btn45 = types.InlineKeyboardButton(text=f"❌ Нет", callback_data='admin_no')
btn46 = types.InlineKeyboardButton(text=f"✅ Да", callback_data='admin_yes')
btn47 = types.InlineKeyboardButton(text=f"✅ Подтверждаю", callback_data='admin_yes_yes')
btn48 = types.InlineKeyboardButton(text=f"1️⃣", callback_data='level_1')
btn49 = types.InlineKeyboardButton(text=f"2️⃣", callback_data='level_2')
btn50 = types.InlineKeyboardButton(text=f"3️⃣", callback_data='level_3')
btn51 = types.InlineKeyboardButton(text=f"Любой", callback_data='level_0')

help_menu.row(btn1)
help_menu.row(btn2)
help_menu.row(btn3)
help_menu.row(btn4)
help_menu.row(btn5)
help_menu.row(btn6)

not_text_menu.row(btn1)
not_text_menu.row(btn2)
not_text_menu.row(btn6)

start_menu.row(btn7)
start_menu.row(btn8)

olymp_menu.row(btn9)
olymp_menu.row(btn10)
olymp_menu.row(btn6)

olymp_menu2.row(btn10)
olymp_menu2.row(btn6)

random_olymp_menu.row(btn11)
random_olymp_menu.row(btn6)

menu_menu.row(btn1)
menu_menu.row(btn2)
menu_menu.row(btn3)
menu_menu.row(btn4)
menu_menu.row(btn5)

levels_menu.row(btn4)
levels_menu.row(btn5)
levels_menu.row(btn6)

prepare_menu.row(btn3)
prepare_menu.row(btn5)
prepare_menu.row(btn6)

advantages_menu.row(btn3)
advantages_menu.row(btn4)
advantages_menu.row(btn6)

update_subj_menu.row(btn12, btn13, btn14)
update_subj_menu.row(btn15, btn16)
update_subj_menu.row(btn17, btn18)
update_subj_menu.row(btn19, btn20)
update_subj_menu.row(btn20_1, btn21)
update_subj_menu.row(btn22, btn23)
update_subj_menu.row(btn24, btn25)
update_subj_menu.row(btn26, btn27)
update_subj_menu.row(btn27_1, btn28)
update_subj_menu.row(btn29, btn30)
update_subj_menu.row(btn6)

update_class_menu.row(btn31, btn32, btn33, btn34)
update_class_menu.row(btn35, btn36, btn37)
update_class_menu.row(btn38, btn39, btn40)
update_class_menu.row(btn6)

admin_menu.row(btn41)
admin_menu.row(btn42)
admin_menu.row(btn43)
admin_menu.row(btn44)
admin_menu.row(btn6)

admin_send_text.row(btn45)
admin_send_text.row(btn46)

admin_confirmation_text.row(btn45)
admin_confirmation_text.row(btn47)

go_out_menu.row(btn6)

olymp_levels_menu.row(btn48, btn49, btn50)
olymp_levels_menu.row(btn51)
olymp_levels_menu.row(btn6)
