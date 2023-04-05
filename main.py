import telebot
from telebot import types
import random
import sqlite3

bot = telebot.TeleBot("token")


# Случайные элементы из списка
def send_random_items(message, items, count=5):
    for item in random.sample(items, count):
        bot.send_message(message.from_user.id, item)


technologies = [
    "Смарт-часы",
    "Беспроводные наушники",
    "Портативное зарядное устройство",
    "Беспроводной динамик",
    "Виртуальные очки",
    "Цифровая камера",
    "Игровая приставка",
    "Игровые наушники",
    "Механическая клавиатура",
    "Игровая мышь",
    "Игровое кресло",
    "Устройство умного дома",
    "Умный термостат",
    "Умный звонок",
    "Робот-пылесос",
    "Умные весы",
    "Электронная книга",
    "Умные наручные часы"
]
kitchen = [
    "Керамические ножи",
    "Кухонный комбайн",
    "Блендер высокой мощности",
    "Аэрогриль",
    "Фритюрница",
    "Сковорода-гриль",
    "Электрический гриль",
    "Кофемолка",
    "Кофеварка",
    "Капсульная кофемашина",
    "Мультиварка",
    "Соковыжималка",
    "Миксер",
    "Вакуумный упаковщик",
    "Набор керамических кастрюль",
    "Набор посуды из чугуна",
    "Набор керамической посуды",
    "Набор столовых приборов",
    "Набор для приготовления суши",
    "Сервировочная доска из мрамора",
    "Набор для гриля"
]
healthAndBeauty = [
    "Массажер для шеи и плеч",
    "Массажер для ног",
    "Массажер для тела",
    "Электрическая зубная щетка",
    "Уход за кожей лица (набор косметики)",
    "Уход за волосами (набор косметики)",
    "Набор для маникюра и педикюра",
    "Электрическая бритва",
    "Электрический триммер для волос",
    "Фитнес-браслет",
    "Инфракрасная лампа для лечения простудных заболеваний",
    "Паровой ингалятор для лечения простудных заболеваний",
    "Набор для массажа стоп",
    "Устройство для обработки кожи стоп",
    "Электронные весы",
    "Набор для ухода за ногтями",
    "Набор для бритья и ухода за бородой",
    "Электрический скрабер для тела",
    "Набор для эпиляции",
    "Косметическое зеркало с подсветкой",
    "Набор для ухода за волосами (например, щипцы для выпрямления волос)"
]
styleAndFashion = [
    "Стильная шляпа",
    "Кожаный ремень",
    "Наручные часы",
    "Сумка или рюкзак",
    "Качественные носки",
    "Классический галстук",
    "Зонтик",
    "Перчатки из натуральной кожи",
    "Свитер",
    "Футболка с интересным принтом",
    "Кожаная портмоне",
    "Набор шарфа и перчаток",
    "Удобные кроссовки",
    "Очки солнцезащитные",
    "Пиджак",
    "Куртка из натуральной кожи",
    "Брюки из качественной ткани",
    "Стильные наушники",
    "Рубашка",
    "Классические брюки",
    "Кошелек"
]
sportsAndRecreation = [
    "Надувной каяк",
    "Рюкзак для пеших прогулок",
    "Компактный гриль",
    "Набор для пикника",
    "Гамак",
    "Набор для игры в бадминтон",
    "Роликовые коньки",
    "Самокат",
    "Набор для гольфа",
    "Велосипед",
    "Набор для горного туризма",
    "Лонгборд",
    "Компактный палаточный лагерь",
    "Набор для барбекю",
    "Надувной матрас",
    "Скейтборд",
    "Смарт-часы для спорта",
    "Набор для рыбалки"
]
interior = [
    "Картина",
    "Керамическая ваза",
    "Набор свечей",
    "Декоративный подсвечник",
    "Плед из натурального материала",
    "Книга по дизайну интерьера",
    "Набор фоторамок",
    "Декоративная подушка",
    "Скульптура",
    "Настольные часы",
    "Ковер",
    "Декоративный поднос",
    "Ароматический диффузор",
    "Декоративная свеча в стекле",
    "Декоративный чехол на подушку",
    "Статуэтка",
    "Декоративная коробка для хранения",
    "Набор предметов декора из стекла",
    "Декоративный бокал для вина",
    "Панно настенное",
    "Декоративный термос"
]
creativity = [
    "Набор для вышивания",
    "Набор для рисования акварелью",
    "Набор для рисования маслом",
    "Набор для рисования графикой",
    "Набор кистей для рисования",
    "Набор карандашей для рисования",
    "Набор фломастеров для рисования",
    "Набор для лепки",
    "Набор для создания украшений",
    "Набор для выжигания дерева",
    "Набор для скрапбукинга",
    "Набор для резьбы по дереву",
    "Набор для рисования каллиграфией",
    "Набор для создания картин на номерах"
]
entertainment = [
    "Карточные игры",
    "Настольные игры",
    "Игры для Playstation",
    "Игры для Xbox",
    "Игры для Nintendo Switch",
    "Книга",
    "Книга с рецептами",
    "Пазл",
    "Кубик Рубика",
    "Мозаика",
    "Фигурки Funko Pop",
    "Набор Lego",
    "Музыкальная игрушка",
    "Детская книга",
    "Игрушка-робот",
    "Радиоуправляемая машина",
    "Детский музыкальный инструмент",
    "Конструктор"
]
diy = [
    "Альбом с фотографиями или рисунками",
    "Вязаный шарф или шапка",
    "Набор мыла, сделанного в домашних условиях",
    "Свеча, изготовленная вручную",
    "Браслет или колье из бисера",
    "Картина, нарисованная вами",
    "Кружка, расписанная вручную",
    "Книга рецептов, составленная самостоятельно",
    "Брелок для ключей, изготовленный из полимерной глины",
    "Настенный календарь, сделанный самостоятельно",
    "Кукла или мягкая игрушка, сшитая вручную",
    "Создать футболку с оригинальным принтом",
    "Создать картину из бутылочных крышек",
    "Создать коллаж из фотографий",
]


# Команда /start
@bot.message_handler(commands=["start"])
def start(message):
    database = sqlite3.connect("db_giftmate.db")
    c = database.cursor()
    # Берём идентификатор пользователя из базы данных
    c.execute("SELECT user_id FROM users WHERE user_id = ?", (message.from_user.id,))
    user_id = c.fetchone()

    # Проверяем, существует ли пользователь в базе данных
    if user_id is None:
        phone_number = ""
        c.execute('INSERT INTO users (user_id, user_phone_number, user_first_name, user_last_name) VALUES (?, ?, ?, ?)',
                  (message.from_user.id, phone_number, message.from_user.first_name, message.from_user.last_name))
        database.commit()
    database.close()
    full_name = " ".join(filter(None, [message.from_user.first_name, message.from_user.last_name]))
    msg = f"👋 Здравствуй, {full_name}! Я бот-помощник по составлению списка желаний."
    bot.send_message(message.from_user.id, msg)
    cmd_home(message)


# Команда /home
@bot.message_handler(commands=["home"])
def cmd_home(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    wishlist = types.KeyboardButton("📝 Мой Список желаний")
    ideas = types.KeyboardButton("🎁 Идеи для подарка")
    find_wishlist = types.KeyboardButton("🔍 Найти Список желаний")
    commands = types.KeyboardButton("📌 Список команд")
    markup.add(wishlist, ideas, find_wishlist, commands)
    bot.send_message(message.from_user.id, "👀 Выберите интересующий Вас раздел.", reply_markup=markup)


# Команда /find_wishlist
@bot.message_handler(commands=["find_wishlist"])
def cmd_find_wishlist(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    home = types.KeyboardButton("🔙 Главное меню")
    markup.add(home)
    bot.send_message(message.from_user.id, "Введите номер телефона человека, список желаний которого Вы хотите найти.")
    bot.send_message(message.from_user.id, 'Напишите номер с цифры 7 и без знака "+".'
                                           '\n✅ 79876543210\n❌ +79876543210\n❌ 89876543210', reply_markup=markup)
    bot.register_next_step_handler(message, check_phone_number)


# Функция проверки номера телефона для дальнейшей обработки
def check_phone_number(message):
    try:
        # Проверяем, является ли сообщение командой "Главное меню"
        if message.text == '🔙 Главное меню':
            cmd_home(message)

        else:
            database = sqlite3.connect('db_giftmate.db')
            c = database.cursor()
            # Получаем номер телефона пользователя из сообщения
            phone_number = message.text
            phone_number.replace(' ', '')

            # Проверяем, соответствует ли номер формату 7XXXXXXXXXX
            if phone_number.startswith('7') and phone_number.isdigit() and len(phone_number) == 11:
                # Проверяем, существует ли пользователь с таким номером в базе данных
                c.execute("SELECT * FROM users WHERE user_phone_number = ?", (phone_number,))
                user = c.fetchone()
                if user is None:
                    bot.send_message(message.from_user.id, "🙁 Извините, такого пользователя нет в базе данных. "
                                                           "Пожалуйста, пригласите его использовать нашего бота, "
                                                           "чтобы начать пользоваться нашими услугами.")
                    cmd_home(message)
                else:
                    # Если пользователь существует, то ищем его список желаний
                    find_other_wishlist(message, phone_number)
            else:
                bot.send_message(message.from_user.id,
                                 '<b>❗️ Ошибка.</b> Номер телефона введён неверно, повторите попытку.',
                                 parse_mode='html')
                bot.register_next_step_handler(message, check_phone_number)

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function add_phone_number: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Функция для поиска список желаний пользователя с заданным номером телефона в базе данных
def find_other_wishlist(message, phone_number):
    database = sqlite3.connect('db_giftmate.db')
    c = database.cursor()
    # Берём данные пользователя из базы данных
    c.execute(
        "SELECT user_id, user_first_name, user_last_name, wishlist_name, wishlist_description, wishlist_booking, wishlist_booking_user FROM users WHERE user_phone_number = ?",
        (phone_number,))
    result = c.fetchall()[0]
    database.close()
    user_id, first_name, last_name, wishlist_name, wishlist_description, wishlist_booking, wishlist_booking_user = result

    names = wishlist_name.split("@<>@")
    descriptions = wishlist_description.split("@<>@")
    booking = wishlist_booking.split("@<>@")
    booking_user = wishlist_booking_user.split("@<>@")
    # Формируем имя пользователя
    full_name = " ".join(filter(None, [first_name, last_name]))

    # Проверяем, что пользователь не запрашивает свой список желаний
    if user_id != message.from_user.id:

        # Если список желаний отсутствует, выводим сообщение об этом
        if not any(wishlist_name):
            response = f"🙁 У {full_name} нет списка желаний."
            bot.send_message(message.from_user.id, response)
            cmd_home(message)

        else:
            bot.send_message(message.from_user.id, f"📝 {full_name} хочет:")
            # Перебираем все желания в списке
            for i in range(1, len(booking)):
                # Если желание свободно, то устанавливаем статус "Свободно",
                # иначе устанавливаем статус "Забронировано"
                if booking[i] == "🟢":
                    status = "🟢 Свободно"
                else:
                    booked = ' '.join(map(str, booking_user[i].split("@><@")))
                    status = f"🔴 {booked} забронировал это желание"
                response = f"{status}\n"
                response += f"⭐️ Желание №{i}:\n{names[i]}"
                if descriptions[i]:
                    response += f"\n📎 Описание:\n{descriptions[i]}"
                bot.send_message(message.from_user.id, response)

            # Отправляем клавиатуру с возможными действиями со списком желаний другого человека
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            free = types.KeyboardButton("🟢 Убрать бронирование")
            book = types.KeyboardButton("🔴 Забронировать желание")
            home = types.KeyboardButton("🔙 Главное меню")
            markup.add(free, book, home)
            bot.send_message(message.from_user.id, "⬇ Выберите действие.", reply_markup=markup)
            bot.register_next_step_handler(message, add_wish_booking_choice, phone_number)

    else:
        cmd_wishlist(message)


# Функция для определения действия (убрать бронирование, забронировать желание, выйти в главное меню)
def add_wish_booking_choice(message, phone_number):
    try:
        response = message.text.lower()

        # Если пользователь выбрал "Убрать бронирование"
        if response == "🟢 убрать бронирование":
            action = False
            bot.send_message(message.from_user.id,
                             "Напишите номер желания, у которого Вы бы хотели убрать бронирование.",
                             reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.from_user.id, "✅4\n❌№4")
            bot.register_next_step_handler(message, add_wish_booking, phone_number, action)

        # Если пользователь выбрал "Забронировать желание"
        elif response == "🔴 забронировать желание":
            action = True
            bot.send_message(message.from_user.id, "Напишите номер желания, которого Вы бы хотели забронировать.",
                             reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.from_user.id, "✅4\n❌№4")
            bot.register_next_step_handler(message, add_wish_booking, phone_number, action)

        # Если пользователь выбрал "Главное меню"
        elif response == "🔙 главное меню":
            cmd_home(message)

        # Если пользователь выбрал что-то другое
        else:
            bot.send_message(message.from_user.id, "Пожалуйста, выберите действие из предложенного.")
            bot.register_next_step_handler(message, add_wish_booking_choice, phone_number)

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function add_wish_booking_choice: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Функция, которая убирает бронирование и бронирует желания
def add_wish_booking(message, phone_number, action):
    try:
        database = sqlite3.connect("db_giftmate.db")
        c = database.cursor()
        # Берём информацию о пользователе из базы данных
        c.execute(
            "SELECT wishlist_booking, wishlist_booking_user, wishlist_booking_user_id FROM users WHERE user_phone_number = ?",
            (phone_number,))
        result = c.fetchall()
        current_booking, current_booking_user, current_booking_user_id = result[0]
        current_booking = current_booking.split("@<>@")
        current_booking_user = current_booking_user.split("@<>@")
        current_booking_user_id = current_booking_user_id.split("@<>@")
        # определение имени пользователя, который забронировал желание
        first_name = f"{message.from_user.first_name}"
        last_name = "" if message.from_user.last_name is None else f"{message.from_user.last_name}"
        name = first_name + "@><@" + last_name
        # определение номера выбранного желания
        first_wish = 1
        number = message.text
        # обработка действий пользователя
        if number == "🔙 Главное меню":
            cmd_home(message)

        # Если пользователь выбрал "Забронировать желание"
        elif action and number.isdigit():
            # Проверяем, что номер желания не выходит из диапазона
            if first_wish <= int(number) < len(current_booking_user):
                # Проверяем, что желание свободно
                if current_booking[int(number)] == "🟢":
                    # Обновляем информацию о желании
                    current_booking_user_id[int(number)] = message.from_user.id
                    current_booking_user[int(number)] = name
                    current_booking[int(number)] = "🔴"
                    new_booking_user_id = "@<>@".join(map(str, current_booking_user_id))
                    new_booking_user = "@<>@".join(map(str, current_booking_user))
                    new_booking = "@<>@".join(map(str, current_booking))
                    c.execute(
                        "UPDATE users SET wishlist_booking = ?, wishlist_booking_user = ?, wishlist_booking_user_id = ? WHERE user_phone_number = ?",
                        (new_booking, new_booking_user, new_booking_user_id, phone_number))
                    database.commit()
                    database.close()

                    bot.send_message(message.from_user.id, 'Готово!')
                    find_other_wishlist(message, phone_number)
                else:
                    bot.send_message(message.from_user.id,
                                     '<b>❗️ Ошибка.</b> Желание уже забронировано, выберите другое желание.',
                                     parse_mode='html')
                    bot.register_next_step_handler(message, add_wish_booking, phone_number, action)
            else:
                bot.send_message(message.from_user.id,
                                 '<b>❗️ Ошибка.</b> Номер желания введён неверно, повторите попытку.',
                                 parse_mode='html')
                bot.register_next_step_handler(message, add_wish_booking, phone_number, action)

        # Если пользователь выбрал "Убрать бронирование"
        elif not action and number.isdigit():
            # Проверяем, что пользователь бронировал хотя бы одно желание
            if str(message.from_user.id) in current_booking_user_id:
                # Проверяем, что номер желания не выходит из диапазона
                if first_wish <= int(number) < len(current_booking_user):
                    # Проверяем, что желание забронировано
                    if current_booking[int(number)] == "🔴":
                        # Проверяем, что пользователь бронировал это желание
                        if current_booking_user_id[int(number)] == f"{message.from_user.id}":
                            # Обновляем информацию о желании
                            current_booking_user_id[int(number)] = ""
                            current_booking_user[int(number)] = ""
                            current_booking[int(number)] = "🟢"
                            new_booking_user_id = "@<>@".join(map(str, current_booking_user_id))
                            new_booking_user = "@<>@".join(map(str, current_booking_user))
                            new_booking = "@<>@".join(map(str, current_booking))
                            c.execute(
                                "UPDATE users SET wishlist_booking = ?, wishlist_booking_user = ?, wishlist_booking_user_id = ? WHERE user_phone_number = ?",
                                (new_booking, new_booking_user, new_booking_user_id, phone_number))
                            database.commit()
                            database.close()

                            bot.send_message(message.from_user.id, 'Готово!')
                            find_other_wishlist(message, phone_number)
                        else:
                            bot.send_message(message.from_user.id,
                                             "<b>❗️ Ошибка.</b> Желание забронировано не вами, выберите другое желание.",
                                             parse_mode='html')
                            bot.register_next_step_handler(message, add_wish_booking, phone_number, action)
                    else:
                        bot.send_message(message.from_user.id,
                                         "<b>❗️ Ошибка.</b> Желание не забронировано, выберите другое желание.",
                                         parse_mode='html')
                        bot.register_next_step_handler(message, add_wish_booking, phone_number, action)
                else:
                    bot.send_message(message.from_user.id,
                                     "<b>❗️ Ошибка.</b> Номер желания введён неверно, повторите попытку.",
                                     parse_mode='html')
                    bot.register_next_step_handler(message, add_wish_booking, phone_number, action)
            else:
                bot.send_message(message.from_user.id, "<b>❗️ Ошибка.</b> Вы не бронировали никакое желание.",
                                 parse_mode='html')
                cmd_home(message)
        else:
            bot.send_message(message.from_user.id, "<b>❗️ Ошибка.</b> Попробуйте еще раз.", parse_mode='html')
            bot.register_next_step_handler(message, add_wish_booking, phone_number, action)

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function add_wish_booking: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Команда /wishlist
@bot.message_handler(commands=["wishlist"])
def cmd_wishlist(message):
    database = sqlite3.connect("db_giftmate.db")
    c = database.cursor()
    # Берём номер телефона пользователя из базы данных
    c.execute("SELECT user_phone_number FROM users WHERE user_id = ?", (message.from_user.id,))
    user_phone_number = c.fetchone()[0]

    # Если номер не был введен ранее, то отправляем сообщение с запросом номера
    if not user_phone_number:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        home = types.KeyboardButton("🔙 Главное меню")
        markup.add(home)
        bot.send_message(message.from_user.id,
                         "📞 Для создания списка желаний необходимо ввести свой номер телефона.")
        bot.send_message(message.from_user.id,
                         'Напишите номер с цифры 7 и без знака "+".\n'
                         '✅ 79876543210\n❌ +79876543210\n❌ 89876543210', reply_markup=markup)
        # Регистрируем обработчик для ввода номера телефона
        bot.register_next_step_handler(message, add_phone_number)

    # Если номер телефона уже введен, то показываем список желаний пользователя
    else:
        database = sqlite3.connect("db_giftmate.db")
        c = database.cursor()
        # Берём желания и описания к желаниям из базы данных
        c.execute("SELECT wishlist_name, wishlist_description FROM users WHERE user_id = ?", (message.from_user.id,))
        result = c.fetchone()
        database.close()
        if result == ('', ''):
            bot.send_message(message.from_user.id, "🙁 У вас нет списка желаний.")

        else:
            # Если у пользователя есть список желаний, то показываем его
            names = result[0].split("@<>@")
            descriptions = result[1].split("@<>@")
            for i in range(1, len(names)):
                response = f"⭐️ Желание №{i}:\n{names[i]}"
                if descriptions[i]:
                    response += f"\n📎 Описание:\n{descriptions[i]}"
                bot.send_message(message.from_user.id, response)

        # Отправляем клавиатуру с возможными действиями со списком желаний
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        add = types.KeyboardButton("➕ Добавить желание")
        edit = types.KeyboardButton("✏️ Изменить желание")
        delete = types.KeyboardButton("➖ Удалить желание")
        home = types.KeyboardButton("🔙 Главное меню")
        markup.add(add, edit, delete, home)
        bot.send_message(message.from_user.id, "⬇ Выберите действие.", reply_markup=markup)


# Обработчик для ввода номера телефона пользователем
def add_phone_number(message):
    try:
        # Проверяем, является ли сообщение командой "Главное меню"
        if message.text == "🔙 Главное меню":
            cmd_home(message)
        else:
            database = sqlite3.connect("db_giftmate.db")
            c = database.cursor()
            c.execute("SELECT user_phone_number FROM users")
            phone_numbers = c.fetchall()
            # Получаем номер телефона пользователя из сообщения
            phone_number = message.text
            phone_number.replace(' ', '')
            # Проверяем, соответствует ли номер формату 7XXXXXXXXXX
            if phone_number.startswith("7") and (phone_number.isdigit()) and len(phone_number) == 11:
                if not any(phone_number in phone[0] for phone in phone_numbers):
                    # Обновляем базу данных с номером телефона пользователя
                    c.execute(
                        "UPDATE users SET user_phone_number = ?, wishlist_name = '', wishlist_description = '', wishlist_booking = '', wishlist_booking_user = '', wishlist_booking_user_id = '' WHERE user_id = ?",
                        (phone_number, message.from_user.id))
                    database.commit()
                    database.close()
                    bot.send_message(message.from_user.id,
                                     '👌 Номер телефона успешно добавлен.')
                    cmd_wishlist(message)
                else:
                    bot.send_message(message.from_user.id,
                                     "<b>❗️ Ошибка.</b> Данный номер телефона уже зарегистрирован.", parse_mode='html')
                    cmd_home(message)
            else:
                bot.send_message(message.from_user.id,
                                 "<b>❗️ Ошибка.</b> Номер телефона введён неверно, повторите попытку.",
                                 parse_mode='html')
                bot.register_next_step_handler(message, add_phone_number)

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function add_phone_number: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Функция для записи желания в базу данных
def add_wish_name(message):
    try:
        database = sqlite3.connect("db_giftmate.db")
        c = database.cursor()
        c.execute(
            "SELECT wishlist_name, wishlist_booking, wishlist_booking_user, wishlist_booking_user_id FROM users WHERE user_id = ?",
            (message.from_user.id,))
        result = c.fetchall()[0]
        current_wishlist_name, current_wishlist_booking, \
            current_wishlist_booking_user, current_wishlist_booking_user_id = result
        new_wishlist_name = message.text
        length = len(current_wishlist_name.split("@<>@"))
        # Максимальное количество желаний
        max_length = 15
        # Стандартные данные
        new_wishlist_booking = "🟢"
        new_wishlist_booking_user = "@><@"
        new_wishlist_booking_user_id = ""
        if new_wishlist_name == "🔙 Главное меню":
            cmd_home(message)
        else:
            if length <= max_length:
                if current_wishlist_name is not None:
                    updated_wishlist_name = current_wishlist_name + "@<>@" + new_wishlist_name
                    updated_wishlist_booking = current_wishlist_booking + "@<>@" + new_wishlist_booking
                    updated_wishlist_booking_user = current_wishlist_booking_user + "@<>@" + new_wishlist_booking_user
                    updated_wishlist_booking_user_id = current_wishlist_booking_user_id + "@<>@" + new_wishlist_booking_user_id
                else:
                    updated_wishlist_name = new_wishlist_name
                    updated_wishlist_booking = new_wishlist_booking
                    updated_wishlist_booking_user = new_wishlist_booking_user
                    updated_wishlist_booking_user_id = new_wishlist_booking_user_id
                # Обновляем базу данных пользователя
                c.execute(
                    "UPDATE users SET wishlist_name = ?, wishlist_booking = ?, wishlist_booking_user = ?, wishlist_booking_user_id = ? WHERE user_id = ?",
                    (updated_wishlist_name, updated_wishlist_booking, updated_wishlist_booking_user,
                     updated_wishlist_booking_user_id, message.from_user.id))
                database.commit()
                database.close()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                yes = types.KeyboardButton("✅ Да")
                no = types.KeyboardButton("❌ Нет")
                markup.add(yes, no)
                bot.send_message(message.from_user.id, "Хотите добавить описание к желанию?", reply_markup=markup)
                bot.register_next_step_handler(message, add_wish_description)
            else:
                bot.send_message(message.from_user.id,
                                 "Вы достигли максимального количества желаний, поэтому не можете добавить новое.")
                cmd_wishlist(message)

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function add_wish_name: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Функция для определения действия (добавить описание, не добавлять описание)
def add_wish_description(message):
    try:
        response = message.text.lower()
        # Если пользователь выбрал "Да"
        if response in ("давай", "да", "✅ да"):
            bot.send_message(message.from_user.id, "Пожалуйста, напишите описание:",
                             reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, add_wish_to_database)

        # Если пользователь выбрал "Нет"
        elif response in ("не", "нет", "❌ нет"):
            bot.send_message(message.from_user.id, "Хорошо. Ваше желание добавлено!")
            add_wish_to_database(message)

        # Если пользователь выбрал что-то другое
        else:
            bot.send_message(message.from_user.id, "Пожалуйста, выберите действие из предложенного.")
            bot.register_next_step_handler(message, add_wish_description)

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function add_wish_description: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Функция добавления описания в базу данных
def add_wish_to_database(message):
    try:
        database = sqlite3.connect("db_giftmate.db")
        c = database.cursor()
        c.execute("SELECT wishlist_description FROM users WHERE user_id = ?", (message.from_user.id,))
        current_wishlist_description = c.fetchone()[0]
        response = message.text.lower()

        # Если пользователь выбрал "Нет"
        if response == "не" or response == "нет" or response == "❌ нет":
            new_wishlist_description = ""
        else:
            new_wishlist_description = message.text
        if current_wishlist_description is not None:
            updated_wishlist_description = current_wishlist_description + "@<>@" + new_wishlist_description
        else:
            updated_wishlist_description = new_wishlist_description
        c.execute("UPDATE users SET wishlist_description = ? WHERE user_id = ?",
                  (updated_wishlist_description, message.from_user.id))
        database.commit()
        database.close()
        cmd_wishlist(message)

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function add_wish_to_database: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Функция для начала редактирования желания
def edit_wish(message):
    try:
        database = sqlite3.connect("db_giftmate.db")
        c = database.cursor()
        # Получаем название текущего списка желаний для пользователя
        c.execute("SELECT wishlist_name FROM users WHERE user_id = ?", (message.from_user.id,))
        current_wishlist_name = c.fetchone()[0].split("@<>@")
        database.close()
        # Проверяем, что список желаний не пустой
        if len(current_wishlist_name) == 1:
            bot.send_message(message.from_user.id, "<b>❗️ Ошибка.</b> У вас нет списка желаний.", parse_mode='html')
            cmd_wishlist(message)
        first_wish = 1
        number = message.text
        if number == "🔙 Главное меню":
            cmd_home(message)
        else:
            # Проверяем, что номер желания находится в диапазоне
            if first_wish <= int(number) < len(current_wishlist_name):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                wish_name = types.KeyboardButton("🎁 Желание")
                wish_description = types.KeyboardButton("📎 Описание")
                wish_all = types.KeyboardButton("📄 Всё")
                markup.add(wish_name, wish_description, wish_all)
                bot.send_message(message.from_user.id, "Выберите то, что вы хотели бы изменить.", reply_markup=markup)
                bot.register_next_step_handler(message, edit_wish_choice, int(number))
            else:
                bot.send_message(message.from_user.id,
                                 "<b>❗️ Ошибка.</b> Номер желания введён неверно, повторите попытку.",
                                 parse_mode='html')
                bot.register_next_step_handler(message, edit_wish)

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function edit_wish: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Функция для определения действия (ред. желание, ред. описание, ред. всё)
def edit_wish_choice(message, number):
    try:
        response = message.text.lower()

        # Если пользователь выбрал "Желание"
        if response == "желание" or response == "🎁 желание":
            choice = False
            bot.send_message(message.from_user.id, "Пожалуйста, напиши новое желание:",
                             reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, edit_wish_name, number, choice)

        # Если пользователь выбрал "Описание"
        elif response == "описание" or response == "📎 описание":
            bot.send_message(message.from_user.id, "Пожалуйста, напиши новое описание:",
                             reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, edit_wish_description, number)

        # Если пользователь выбрал "Всё"
        elif response == "все" or response == "всё" or response == "📄 всё":
            choice = True
            bot.send_message(message.from_user.id, "Пожалуйста, напиши новое желание:",
                             reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, edit_wish_name, number, choice)

        # Если пользователь выбрал что-то другое
        else:
            bot.send_message(message.from_user.id, "Пожалуйста, выберите действие из предложенного.")

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function edit_wish_choice: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Функция для редактирования желания и/или описания
def edit_wish_name(message, number, choice):
    try:
        database = sqlite3.connect("db_giftmate.db")
        c = database.cursor()
        # Получаем текущее имя списка желаний
        c.execute("SELECT wishlist_name FROM users WHERE user_id = ?", (message.from_user.id,))
        current_wishlist_name = c.fetchone()[0].split("@<>@")
        # Получаем новое имя списка желаний от пользователя
        new_wishlist_name = message.text

        # Если пользователь выбирает "Главное меню"
        if new_wishlist_name == "🔙 Главное меню":
            cmd_home(message)
        else:
            # Обновляем желание в базе данных
            current_wishlist_name[number] = new_wishlist_name
            new_wishlist_name = "@<>@".join(map(str, current_wishlist_name))
            c.execute("UPDATE users SET wishlist_name = ? WHERE user_id = ?", (new_wishlist_name, message.from_user.id))
            database.commit()
            database.close()
            bot.send_message(message.from_user.id, "Готово!")

        # Если пользователь хочет отредактировать описание желания, запрашиваем новое описание
        if choice:
            bot.send_message(message.from_user.id, "Пожалуйста, напиши новое описание:",
                             reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, edit_wish_description, number)
        else:
            cmd_wishlist(message)

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function edit_wish_name: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Функция для редактирования описания
def edit_wish_description(message, number):
    try:
        database = sqlite3.connect("db_giftmate.db")
        c = database.cursor()
        # Получаем текущее описание списка желаний из базы данных
        c.execute("SELECT wishlist_description FROM users WHERE user_id = ?", (message.from_user.id,))
        current_wishlist_description = c.fetchone()[0].split("@<>@")
        # Получаем новое описание списка желаний из сообщения пользователя
        new_wishlist_description = message.text
        current_wishlist_description[number] = new_wishlist_description
        new_wishlist_description = "@<>@".join(map(str, current_wishlist_description))
        # Обновляем описание списка желаний в базе данных
        c.execute("UPDATE users SET wishlist_description = ? WHERE user_id = ?",
                  (new_wishlist_description, message.from_user.id))
        database.commit()
        database.close()
        bot.send_message(message.from_user.id, "Готово!")
        cmd_wishlist(message)

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function edit_wish_description: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Функция определяющая номер желания и определяет действие (удалить всё, удалить описание)
def delete_wish(message):
    try:
        database = sqlite3.connect("db_giftmate.db")
        c = database.cursor()
        # Получаем название текущего списка желаний пользователя
        c.execute("SELECT wishlist_name FROM users WHERE user_id = ?", (message.from_user.id,))
        current_wishlist_name = c.fetchone()[0].split("@<>@")
        database.close()
        first_wish = 1

        # Если пользователь нажал кнопку "Главное меню"
        if message.text == "🔙 Главное меню":
            cmd_home(message)
        else:
            number = message.text
            if current_wishlist_name is not None:
                # Если у пользователя есть список желаний, то проверяем, что номер желания находится в диапазоне
                # от первого до последнего желания
                if first_wish <= int(number) < len(current_wishlist_name):
                    # Создаем клавиатуру с двумя кнопками - "Удалить всё" и "Удалить описание"
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    wish_all = types.KeyboardButton("📄 Всё")
                    wish_description = types.KeyboardButton("📎 Описание")
                    markup.add(wish_all, wish_description)
                    bot.send_message(message.from_user.id, "Выберите то, что вы хотели бы изменить.",
                                     reply_markup=markup)
                    bot.register_next_step_handler(message, delete_wish_choice, int(number))
                else:
                    bot.send_message(message.from_user.id,
                                     "<b>❗️ Ошибка.</b> Номер желания введён неверно, повторите попытку.",
                                     parse_mode='html')
                    bot.register_next_step_handler(message, edit_wish)
            else:
                bot.send_message(message.from_user.id, "<b>❗️ Ошибка.</b> У вас нет списка желаний.", parse_mode='html')
                cmd_wishlist(message)

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function delete_wish: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Функция для удаления всего желания или описания к желанию
def delete_wish_choice(message, number):
    try:
        response = message.text.lower()

        # Если пользователь хочет удалить всё желание
        if response in ("все", "всё", "📄 всё"):
            database = sqlite3.connect("db_giftmate.db")
            c = database.cursor()
            # Получаем данные о текущих желаниях пользователя
            c.execute(
                "SELECT wishlist_booking, wishlist_booking_user, wishlist_booking_user_id, wishlist_name, wishlist_description FROM users WHERE user_id = ?",
                (message.from_user.id,))
            current_wishlist_booking, current_wishlist_booking_user, current_wishlist_booking_user_id, \
                current_wishlist_name, current_wishlist_description = c.fetchone()

            # Разделяем данные о желаниях на списки
            current_wishlist_booking = current_wishlist_booking.split("@<>@")
            current_wishlist_booking_user = current_wishlist_booking_user.split("@<>@")
            current_wishlist_booking_user_id = current_wishlist_booking_user_id.split("@<>@")
            current_wishlist_name = current_wishlist_name.split("@<>@")
            current_wishlist_description = current_wishlist_description.split("@<>@")

            # Удаляем данные о желании по указанному номеру из каждого списка
            current_wishlist_booking.pop(number)
            current_wishlist_booking_user.pop(number)
            current_wishlist_booking_user_id.pop(number)
            current_wishlist_name.pop(number)
            current_wishlist_description.pop(number)

            # Объединяем списки в строки с разделителями "@<>@"
            new_wishlist_booking = "@<>@".join(map(str, current_wishlist_booking))
            new_wishlist_booking_user = "@<>@".join(map(str, current_wishlist_booking_user))
            new_wishlist_booking_user_id = "@<>@".join(map(str, current_wishlist_booking_user_id))
            new_wishlist_name = "@<>@".join(map(str, current_wishlist_name))
            new_wishlist_description = "@<>@".join(map(str, current_wishlist_description))

            # Обновляем данные о желаниях в базе данных
            c.execute(
                "UPDATE users SET wishlist_description = ?, wishlist_name = ?, wishlist_booking = ?, wishlist_booking_user = ?, wishlist_booking_user_id = ? WHERE user_id = ?",
                (new_wishlist_description, new_wishlist_name, new_wishlist_booking, new_wishlist_booking_user,
                 new_wishlist_booking_user_id, message.from_user.id))
            database.commit()
            database.close()
            bot.send_message(message.from_user.id, "Готово!")
            cmd_wishlist(message)

        # Если пользователь хочет удалить описание к желанию
        elif response in ("описание", "📎 описание"):
            database = sqlite3.connect("db_giftmate.db")
            c = database.cursor()
            # Получаем данные о текущих желаниях пользователя
            c.execute("SELECT wishlist_description FROM users WHERE user_id = ?", (message.from_user.id,))
            current_wishlist_description = c.fetchone()[0].split("@<>@")

            # Проверяем наличие описания
            if current_wishlist_description[number] == "":
                bot.send_message(message.from_user.id, "У этого желания нет описания.")
            else:
                # Удаляем данные об описании желания по указанному номеру
                current_wishlist_description[number] = ""
                new_wishlist_description = "@<>@".join(map(str, current_wishlist_description))

                # Обновляем данные об описании желания в базе данных
                c.execute("UPDATE users SET wishlist_description = ? WHERE user_id = ?",
                          (new_wishlist_description, message.from_user.id))
                database.commit()
                database.close()
                bot.send_message(message.from_user.id, "Готово!")
            cmd_wishlist(message)
        else:
            bot.send_message(message.from_user.id, "Пожалуйста, выберите действие из предложенного.")

    except (TypeError, sqlite3.Error) as e:
        print(f"Error with function delete_wish: {e}")
        bot.send_message(message.from_user.id, "<b>❗️ Произошла ошибка.</b> Повторите попытку", parse_mode='html')
        cmd_home(message)


# Обработка текста
@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "📝 Мой Список желаний":
        cmd_wishlist(message)

    elif message.text == "🔍 Найти Список желаний":
        cmd_find_wishlist(message)

    elif message.text == "➕ Добавить желание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        home = types.KeyboardButton("🔙 Главное меню")
        markup.add(home)
        bot.send_message(message.from_user.id, "Напишите то, что бы Вы хотели добавить в список желаний.",
                         reply_markup=markup)
        bot.register_next_step_handler(message, add_wish_name)

    elif message.text == "✏️ Изменить желание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        home = types.KeyboardButton("🔙 Главное меню")
        markup.add(home)
        bot.send_message(message.from_user.id, "Напишите номер желания, которого Вы бы хотели отредактировать.",
                         reply_markup=markup)
        bot.send_message(message.from_user.id, "✅4\n❌№4")
        bot.register_next_step_handler(message, edit_wish)

    elif message.text == "➖ Удалить желание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        home = types.KeyboardButton("🔙 Главное меню")
        markup.add(home)
        bot.send_message(message.from_user.id, "Напишите номер желания, которого Вы бы хотели удалить.",
                         reply_markup=markup)
        bot.send_message(message.from_user.id, "✅4\n❌№4")
        bot.register_next_step_handler(message, delete_wish)

    elif message.text == "🎁 Идеи для подарка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("💻 Технологии")
        btn2 = types.KeyboardButton("🍽 Кухня")
        btn3 = types.KeyboardButton("✨ Здоровье и красота")
        btn4 = types.KeyboardButton("👨‍🚀 Стиль и мода")
        btn5 = types.KeyboardButton("💪 Спорт и отдых")
        btn6 = types.KeyboardButton("🛋 Интерьер")
        btn7 = types.KeyboardButton("🎨 Творчество")
        btn8 = types.KeyboardButton("🎲 Развлечения")
        btn9 = types.KeyboardButton("🛠️ Своими руками")
        home = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, home)
        bot.send_message(message.from_user.id, '⬇ Выберите категорию.', reply_markup=markup)

    elif message.text == "💻 Технологии":
        send_random_items(message, technologies)
    elif message.text == "🍽 Кухня":
        send_random_items(message, kitchen)
    elif message.text == "✨ Здоровье и красота":
        send_random_items(message, healthAndBeauty)
    elif message.text == "👨‍🚀 Стиль и мода":
        send_random_items(message, styleAndFashion)
    elif message.text == "💪 Спорт и отдых":
        send_random_items(message, sportsAndRecreation)
    elif message.text == "🛋 Интерьер":
        send_random_items(message, interior)
    elif message.text == "🎨 Творчество":
        send_random_items(message, creativity)
    elif message.text == "🎲 Развлечения":
        send_random_items(message, entertainment)
    elif message.text == "🛠️ Своими руками":
        send_random_items(message, diy)

    elif message.text == "📌 Список команд":
        text = "<b>📝 Мой Список желаний</b> — команда, которая выводит список ваших желаний.\n\n" \
               "<b>➕ Добавить желание</b> — команда, которая позволяет вам добавлять новые желания в ваш список. Вы можете добавить название и описание к каждому желанию.\n\n" \
               "<b>✏️ Изменить желание</b> — команда, которая позволяет вам изменить название и/или описание уже существующего желания в вашем списке.\n\n" \
               "<b>➖ Удалить желание</b> — команда, которая позволяет вам удалить уже существующее желание или же его описание из вашего списка.\n\n" \
               "<b>🎁 Идеи для подарка</b> — команда, которая предоставляет идеи подарков по категориям.\n\n" \
               "<b>🔍 Найти Список желаний</b> — команда, которая позволяет вам найти список желаний другого пользователя, если вы знаете его номер телефона.\n\n" \
               "<b>🟢 Убрать бронирование</b> — команда, которая позволяет убрать бронирование на выбранное желание в списке другого пользователя.\n\n" \
               "<b>🔴 Забронировать желание</b> — команда, которая позволяет забронировать выбранное желание в списке другого пользователя."
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        home = types.KeyboardButton('🔙 Главное меню')
        markup.add(home)
        bot.send_message(message.from_user.id, text, parse_mode='html', reply_markup=markup)

    elif message.text == "🔙 Главное меню":
        cmd_home(message)

    else:
        msg = message.text.lower()
        if msg in ("привет", "привет!", "привет."):
            bot.send_message(message.from_user.id, "Привет!")
        elif msg in ("как дела", "как дела?", "как дела."):
            bot.send_message(message.from_user.id, "Хорошо!")
        elif msg in ("что делаешь", "что делаешь?", "что делаешь."):
            bot.send_message(message.from_user.id, "Создаю списки желаний.")


# Обработка фото
@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    photo_answer = [
        "Какая красивая картинка!",
        "Эта фотография идеально передает атмосферу момента.",
        "Это действительно уникальное изображение.",
        "Какой интересный объект на этой фотографии!",
        "Это точно искусство, а не просто фотография.",
        "Эта фотография - настоящее произведение искусства!"]
    bot.send_message(message.chat.id, photo_answer[random.randint(0, len(photo_answer))])


# Запуск на постоянное выполнение
bot.polling(none_stop=True)
