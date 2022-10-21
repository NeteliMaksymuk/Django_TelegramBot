import telebot
from telebot import types

from recipes.models import Profile, Recipes

from django_telegram_bot.settings import TOKEN


bot = telebot.TeleBot(TOKEN)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.sex = None


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Yes', 'No')
    msg = bot.reply_to(message, """\
                                    Hi there.Do you have a account?\n                                 
                                """, reply_markup=markup)
    bot.register_next_step_handler(msg, test)


def test(message):
    chat_id = message.chat.id
    if message.text == 'No':
        msg = bot.reply_to(message, """\
                                            What is your name?                                  
                                        """)
        bot.register_next_step_handler(msg, process_name_step)
    elif message.text == 'Yes':
        bot.send_message(chat_id, 'if you want to open menu send me \n/menu')
    else:
        print('ops')


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Male', 'Female', 'Co-ed')
        msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u'Male') or (sex == u'Female') or (sex == u'Co-ed'):
            user.sex = sex
        else:
            raise Exception("Unknown sex")

        types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(chat_id, 'Nice to meet you \n' + user.name + '\n Sex:' + user.sex)
        profile = Profile(name=user.name, last_name=message.from_user.last_name,
                          first_name=message.from_user.first_name, gender=user.sex,
                          telegram_username=message.from_user.username)
        profile.save()
        bot.send_message(chat_id, 'Send something to check if you are not a bot')
        bot.register_next_step_handler(msg, menu_bar)
    except Exception as e:
        bot.reply_to(message, 'OMG,you are already exist.\n send me to open menu \n /menu  ')


@bot.message_handler(commands=['menu'])
def menu_bar(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('About me', 'Recipes')
    msg = bot.reply_to(message, 'What is your next step', reply_markup=markup)
    bot.register_next_step_handler(msg, next_step)


def next_step(message):
    chat_id = message.chat.id
    if message.text == 'About me':

        b = Profile.objects.get(telegram_username=message.from_user.username)
        bot.send_message(chat_id,
                         '\nYour name: \n' + ' ' + str(b.name) +
                         '\nYour gender:\n' + ' ' + str(b.gender) +
                         '\nYour id:\n' + ' ' + str(b.id))
    elif message.text == 'Recipes':
        res = list()
        r = Recipes.objects.count()
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for i in range(r):

            res.append(Recipes.objects.all()[i].recipe_name)
            markup.add(Recipes.objects.all()[i].recipe_name)
        print(res)

        msg = bot.reply_to(message, 'What is your next step', reply_markup=markup)
        bot.register_next_step_handler(msg, next_step2)


def next_step2(message):
    chat_id = message.chat.id
    b = Recipes.objects.get(recipe_name=message.text)
    bot.send_message(chat_id, '\nRecipe name\n' + str(b.recipe_name) +
                     '\nDescription:\n' + str(b.description))


bot.infinity_polling()
