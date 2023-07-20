import random

import pymorphy3
import telebot

import menus
from const import *
from db import BotDB

bot = telebot.TeleBot(TOKEN)
morph = pymorphy3.MorphAnalyzer()
db = BotDB('data/users.db')


def update_subj(call):
    bot.send_message(call.message.chat.id,
                     'Выбери предмет, по которому хочешь найти олимпиаду' + '\nЕго можно будет изменить позже',
                     reply_markup=menus.update_subj_menu)


def update_class(call):
    bot.edit_message_text('Выбери класс, за который хочешь участвовать в олимпиадах\nЕго можно будет изменить позже',
                          call.message.chat.id, call.message.message_id,
                          reply_markup=menus.update_class_menu)


def update_level(call):
    bot.edit_message_text('Выбери уровень олимпиады\nЕго можно будет изменить позже',
                          call.message.chat.id, call.message.message_id,
                          reply_markup=menus.olymp_levels_menu)


def check_choose(call):
    if db.user_exists(call.from_user.id):
        return True
    else:
        update_subj(call)
        return False


def olymp(call):
    if check_choose(call):
        user_subj = db.get_user_subj(call.from_user.id)
        user_class = db.get_user_class(call.from_user.id)
        user_level = db.get_user_level(call.from_user.id)
        try:
            if user_level == 0:
                olymp = OLYMPIADS[(OLYMPIADS['response'] == user_subj) & (OLYMPIADS['min_class'] <= user_class) & (
                        OLYMPIADS['max_class'] >= user_class)].sample()
            else:
                olymp = OLYMPIADS[(OLYMPIADS['response'] == user_subj) & (OLYMPIADS['min_class'] <= user_class) & (
                        OLYMPIADS['max_class'] >= user_class) & (
                                          OLYMPIADS['level'] == user_level)].sample()

            bot.send_message(call.message.chat.id,
                             OLYMP_TEXT_PART_1[random.randint(0, len(OLYMP_TEXT_PART_1) - 1)] + ' `' + olymp[
                                 'name'] + '` по профилю ' + olymp[
                                 'profile'] + '\n\nКлассы, в которых можно принять участие: ' + olymp[
                                 'class'] + '\n\nУровень олимпиады: ' + olymp['level'].to_string().split()[
                                 1] + '\n\n📘 Подробная информация:\n' + f'· Номер в перечне олимпиад - {int(float(olymp["num_in_list"].to_string().split()[1]))}' \
                             + f'\n· Предметы, на которые стоит обратить внимание при подготовке: {" ".join(olymp["prof_subject"].to_string().split()[1:])}' \
                             + f'\n· Этапы олимпиады - {" ".join(olymp["stage"].to_string().split()[1:])}',
                             reply_markup=menus.olymp_menu, parse_mode='MARKDOWN')
        except:
            bot.send_message(call.message.chat.id,
                             f"К сожалению, у меня не получилось найти олимпиаду {'любого' if user_level == 0 else user_level} уровня по {morph.parse(user_subj)[0].inflect({'datv'}).word} для {user_class} класса\n\nПоменяй класс, предмет или уровень олимпиады и попробуй снова!",
                             reply_markup=menus.olymp_menu2)


def random_olymp(message):
    rndm_olymp = OLYMPIADS.sample()
    bot.send_message(message.chat.id,
                     RANDOM_TEXT_PART_1[random.randint(0, len(RANDOM_TEXT_PART_1) - 1)] + ' `' + rndm_olymp[
                         'name'] + '` по профилю ' + rndm_olymp[
                         'profile'] + '\n\nКлассы, в которых можно принять участие: ' + rndm_olymp[
                         'class'] + '\n\nУровень олимпиады: ' + rndm_olymp['level'].to_string().split()[
                         1] + '\n\n📘 Подробная информация:\n' + f'· Номер в перечне олимпиад - {int(float(rndm_olymp["num_in_list"].to_string().split()[1]))}' \
                     + f'\n· Предметы, на которые стоит обратить внимание при подготовке: {" ".join(rndm_olymp["prof_subject"].to_string().split()[1:])}' \
                     + f'\n· Этапы олимпиады - {" ".join(rndm_olymp["stage"].to_string().split()[1:])}',
                     reply_markup=menus.random_olymp_menu, parse_mode='MARKDOWN')


def menu(call):
    bot.edit_message_text(f'''Ты находишься в меню "Навигатора олимпиад"\n
"Навигатор олимпиад" может подобрать олимпиаду из Перечня, утвержденного Министерством науки и высшего образования России, которая подходит именно тебе!\n
Чтобы воспользоваться ботом, используй одну из кнопок ниже\n
Подписывайся на наше сообщество во ВКонтакте и следи за всеми новостями https://vk.com/navigator_olympiad''',
                          call.message.chat.id, call.message.message_id,
                          reply_markup=menus.menu_menu)
    # bot.send_message(message.chat.id, )


def levels(message):
    bot.edit_message_text(f'''Выделяются такие уровни олимпиад:\n
• Олимпиада I уровня — не менее 3 тысяч участников из 20 и более регионов России, проводится не менее двух лет. Победители и призеры могут поступить в профильный ВУЗ без вступительных испытаний\n
• Олимпиада II уровня — 1,5 тысячи участников из 10 и более регионов России. Победители и призеры могут получить 100 баллов ЕГЭ по предмету, соответствующему профилю олимпиады\n
• Олимпиада III уровня — 1,5 тысячи участников из трёх и более регионов России. Победители и призеры могут получить льготы на усмотрение ВУЗа\n\n
В основном олимпиады делятся на несколько этапов:\n
• Один или два отборочных этапа, которые обычно проводятся дистанционно\n
• Заключительный этап, который обычно проходит очно''',
                          message.chat.id, message.message_id,
                          reply_markup=menus.levels_menu)


def how_prepare(message):
    bot.edit_message_text('''До начала олимпиад рекомендую тебе:\n
• Ознакомиться с форматом и условиями участия в олимпиаде\n
• Изучить задания прошлых лет\n
• Посещать дополнительные занятия для подготовки или готовиться самостоятельно\n
• Использовать дополнительные учебные материалы\n
• Не забывать про отдых и спорт\n\n
Во время решения олимпиадных заданий:\n
• Работать внимательно и сосредоточенно\n
• Старайся не нервничать и писать разборчиво''',
                          message.chat.id, message.message_id,
                          reply_markup=menus.prepare_menu)
    # bot.send_message(message.chat.id, , reply_markup=help_menu)


def advantages(message):
    bot.edit_message_text('''Преимущества, которые дают участия в олимпиадах:
• Льготы для победителей и призёров олимпиад (подробнее описано в разделе "🔥 Уровни, этапы и льготы")\n
• Мотивация узнавать больше\n
• Умение нестандартно мыслить\n
• Умение логически рассуждать\n
• Умение организовывать своё время''',
                          message.chat.id, message.message_id,
                          reply_markup=menus.advantages_menu)


def set_subj(call, subj):
    if db.user_exists(call.from_user.id):
        db.set_user_subj(call.from_user.id, subj)
    else:
        db.add_user(call.from_user.id, call.from_user.username, subj)
    bot.answer_callback_query(call.id, text="Предмет выбран")
    update_class(call)


def set_class(call, user_class):
    db.set_user_class(call.from_user.id, user_class)
    bot.answer_callback_query(call.id, text="Класс выбран")
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    update_level(call)


def set_level(call, user_level):
    db.set_user_level(call.from_user.id, user_level)
    bot.answer_callback_query(call.id, text="Уровень выбран")
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    bot.edit_message_text('✅ Предмет, класс и уровень успешно выбраны',
                          call.message.chat.id, call.message.message_id,
                          reply_markup=None)
    olymp(call)


def admin_get_users(users):
    out = []
    for i in users:
        out.append(str(i[0]) + ' ' + str(i[1]) + ' @' + i[2] + ' ' + i[3] + ' ' + str(i[4]) + ' ' + str(i[5]) + ' ' + i[7])
    return out


def admin_check_text(message):
    bot.send_message(ADMIN_ID,
                     f'Ты действительно хочешь отправить следующий текст {db.get_users_count()} пользователям\n\n' + message.text,
                     reply_markup=menus.admin_send_text)
    db.add_admin_text(message.from_user.id, message.from_user.username, message.text)


def admin_confirmation_text(message):
    bot.edit_message_text(
        f'Подтверди отправку текста {db.get_users_count()} пользователям\n\n' + db.get_last_admin_text()[3],
        message.chat.id, message.message_id, reply_markup=menus.admin_confirmation_text)


def admin_send_text(message):
    bot.edit_message_text('Рассылка успешно началась', message.chat.id, message.message_id,
                          reply_markup=menus.go_out_menu)
    db.set_admin_text_status(db.get_last_admin_text()[0])

    for user in db.get_users_list():
        try:
            bot.send_message(user[1],
                             '🔔 Тебе пришло сообщение от администрации "Навигатора олимпиад"\n\n' +
                             db.get_last_admin_text()[3])
        except:
            pass


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text=f"{START_TEXT[random.randint(0, len(START_TEXT) - 1)]}",
                     reply_markup=menus.start_menu)


@bot.message_handler(commands=['can'])
def can(message):
    bot.send_message(message.chat.id, text=f"""Я могу:
· Подобрать олимпиаду по твоему любимому предмету
· Подобрать случайную олимпиаду
· Рассказать, какие уровни, этапы и льготы бывают у олимпиад и чем они отличаются
· Дать совет, как лучше готовиться к олимпиадам и решать их
· Рассказать, какие преимущества дает участие в олимпиадах""",
                     reply_markup=menus.help_menu)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text=f'''Это - бот "Навигатор олимпиад"! \n
Я помогу подобрать олимпиаду по предмету и классу, которая тебе точно понравится!
Если ты хочешь попытать удачу, то я могу подобрать случайную олимпиаду
После подбора олимпиады ты сможешь узнать о ней подробнее - с помощью команды "Детали олимпиады" или найти ещё одну олимпиаду\n\n
А еще я могу помочь тебе разобраться с уровнями олимпиад, дам совет, как лучше готовиться, и расскажу, как решать олимпиады\n
Сообщество проекта во ВКонтакте https://vk.com/navigator_olympiad''',
                     reply_markup=menus.help_menu)


@bot.message_handler(commands=['admin'])
def admin(message):
    if message.from_user.id == ADMIN_ID:
        bot.send_message(message.from_user.id, f'''Admin панель
Количество пользователей - `{db.get_users_count()}`
Количество олимпиад - `{len(OLYMPIADS)}`''', reply_markup=menus.admin_menu, parse_mode='MARKDOWN')
    else:
        bot.send_message(message.chat.id,
                         'Тебя нет в списке администраторов!\n\nВоспользуйся кнопками ниже, для использования бота',
                         reply_markup=menus.help_menu)


@bot.message_handler(
    content_types=["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location",
                   "contact"])
def not_command(message):
    bot.send_message(message.chat.id, 'Я пока не научился понимать сообщения, пожалуйста, воспользуйся кнопками ниже',
                     reply_markup=menus.not_text_menu)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'menu':
        menu(call)
    elif call.data == 'help':
        help(call.message)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    elif call.data == 'olymp':
        olymp(call)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    elif call.data == 'random_olymp_menu':
        random_olymp(call.message)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    elif call.data == 'levels':
        levels(call.message)
    elif call.data == 'how_prepare':
        how_prepare(call.message)
    elif call.data == 'advantages':
        advantages(call.message)
    elif call.data == 'update':
        update_subj(call)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

    elif call.data == 'astronomy':
        set_subj(call, 'астрономия')
    elif call.data == 'business':
        set_subj(call, 'бизнес')
    elif call.data == 'biology':
        set_subj(call, 'биология')
    elif call.data == 'geography':
        set_subj(call, 'география')
    elif call.data == 'journalism':
        set_subj(call, 'журналистика')
    elif call.data == 'art':
        set_subj(call, 'искусство')
    elif call.data == 'foreign_lang':
        set_subj(call, 'иностранный язык')
    elif call.data == 'informatics':
        set_subj(call, 'информатика')
    elif call.data == 'history':
        set_subj(call, 'история')
    elif call.data == 'literature':
        set_subj(call, 'литература')
    elif call.data == 'math':
        set_subj(call, 'математика')
    elif call.data == 'music':
        set_subj(call, 'музыка')
    elif call.data == 'social':
        set_subj(call, 'обществознание')
    elif call.data == 'law':
        set_subj(call, 'право')
    elif call.data == 'russian_lang':
        set_subj(call, 'русский язык')
    elif call.data == 'sociology':
        set_subj(call, 'социология')
    elif call.data == 'physics':
        set_subj(call, 'физика')
    elif call.data == 'chemistry':
        set_subj(call, 'химия')
    elif call.data == 'economy':
        set_subj(call, 'экономика')

    elif call.data == '2':
        set_class(call, 2)
    elif call.data == '3':
        set_class(call, 3)
    elif call.data == '4':
        set_class(call, 4)
    elif call.data == '5':
        set_class(call, 5)
    elif call.data == '6':
        set_class(call, 6)
    elif call.data == '7':
        set_class(call, 7)
    elif call.data == '8':
        set_class(call, 8)
    elif call.data == '9':
        set_class(call, 9)
    elif call.data == '10':
        set_class(call, 10)
    elif call.data == '11':
        set_class(call, 11)

    elif call.data == 'level_1':
        set_level(call, 1)
    elif call.data == 'level_2':
        set_level(call, 2)
    elif call.data == 'level_3':
        set_level(call, 3)
    elif call.data == 'level_0':
        set_level(call, 0)


    elif call.data == 'admin_get_db':
        bot.send_document(ADMIN_ID, open('data/users.db', 'rb'))
    elif call.data == 'admin_20_users':
        bot.send_message(ADMIN_ID, '\n'.join(admin_get_users(db.get_users_list()[:20])))
    elif call.data == 'admin_all_users':
        bot.send_message(ADMIN_ID, '\n'.join(admin_get_users(db.get_users_list())))
    elif call.data == 'admin_start_message':
        mesg = bot.edit_message_text('Введи текст, которых хочешь отправить', call.message.chat.id,
                                     call.message.message_id)
        bot.register_next_step_handler(mesg, admin_check_text)
    elif call.data == 'admin_no':
        menu(call)
    elif call.data == 'admin_yes':
        admin_confirmation_text(call.message)
    elif call.data == 'admin_yes_yes':
        admin_send_text(call.message)


bot.polling(non_stop=True)
