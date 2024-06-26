import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

START_TEXT = [
    'Привет! Это "Навигатор олимпиад". Я помогу подобрать олимпиаду, подходящую именно тебе, а также расскажу про детали проведения олимпиад.\nНачнем?',
    'Здравствуй! Это бот "Навигатор олимпиад". Я могу помочь тебе подобрать олимпиаду по любимому предмету или рассказать про них чуть подробнее.\nПриступим к делу?',
    'Привет! Ты запустил "Навигатор олимпиад". Я помогу тебе подобрать олимпиаду по твоему профилю или расскажу про них чуть подробнее.\nДавай начнём?',
    'Приветствую тебя в "Навигаторе олимпиад"! Я помогу тебе подобрать олимпиаду по твоему профилю или расскажу про все детали проведения олимпиад.\nСтартуем?']

START_BUTTON = ['Начинаем!', 'Погнали!', 'Стартуем!', 'Поехали!']

RANDOM_TEXT_PART_1 = [f'Тебе выпала', 'Звёзды подсказывают, что тебе подходит',
                      'Тебе может понравиться']
OLYMP_TEXT_PART_1 = ['Я нашел олимпиаду, которая тебе понравится', 'Тебе подходит', "Эта олимпиада тебе подходит"]

TOKEN = TOKEN

OLYMPIADS = pd.read_csv("data/olympiads_23_24.csv", on_bad_lines='skip')
RANDOM_PROF = {
    'Естественные науки': ['астрономия', "биология", "география", "химия"],
    'Социальные науки': ["бизнес", "история", "обществознание", "право", "социология", "экономика"],
    'Гуманитарные науки': ["журналистика", "иностранный язык", "лингвистика", "литература", "русский язык"],
    'Творчество': ["искусство", "музыка"],
    'Технические науки': ["информатика", "математика", "технология", "физика"]
}

ADMIN_ID = 770483189
SUPPORT_CHAT_ID = -1001915632946
