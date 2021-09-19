import dotenv
import os
import gspread
import telebot
import requests
import json
from oauth2client.service_account import ServiceAccountCredentials
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from telebot import custom_filters

dotenv.load_dotenv()

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

API_KEY = os.getenv("API_KEY")  # your Token from @Botfather
my_id = os.getenv("my_id")  # your personal chat ID
analyst_id = os.getenv("analyst_id")  # personal chat ID of your analyst
creds_location = os.getenv("creds_location")
forms_url = os.getenv("forms_url")  # your URL to the Google Forms for feedback
# your URL to the Google Spreadsheet for analytics
spreadsheet_url = os.getenv("spreadsheet_url")

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "creds_location", scope)
client = gspread.authorize(creds)

database = client.open("YOGI BOT DATABASE").worksheet("DATABASE")
analytics_YOGI_BOT = client.open("ANALYTICS").worksheet("YOGI_BOT")

bot = telebot.TeleBot(API_KEY)


def german(message):
    cell = database.find(str(message.chat.id))
    r, c = cell.row, cell.col+1
    database.update_cell(r, c, 'de')
    bot.send_message(message.chat.id, "Language is set to German.")


def english(message):
    cell = database.find(str(message.chat.id))
    r, c = cell.row, cell.col+1
    database.update_cell(r, c, 'en')
    bot.send_message(message.chat.id, "Language is set to English.")


@bot.message_handler(commands=['start'])
def start(message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    K1 = KeyboardButton('GENERATE A YOGI SAYING 🎅🏻')
    K2 = KeyboardButton('LANGUAGE')
    K3 = KeyboardButton('WEBSITE')
    K4 = KeyboardButton('HELP')

    markup.row(K1)
    markup.row(K2, K3, K4)

    col = database.col_values(1)  # 3

    if str(message.chat.id) not in col:
        database.append_row([message.chat.id, 'en'])
        analytics_YOGI_BOT.update_acell('F10', str(
            len(database.col_values(1))-1).replace("'", " "))

    bot.send_message(message.chat.id, "Welcome to the YogiBot! 🍵\n\n\
Would you care for some tea along with some sayings and inspirational quotes? 💡", reply_markup=markup)
    start_count = analytics_YOGI_BOT.acell('F3').value
    analytics_YOGI_BOT.update_acell(
        'F3', str(int(start_count)+1).replace("'", " "))


@bot.message_handler(commands=['yogi'])
def yogi(message):

    cell = database.find(str(message.chat.id))
    r, c = cell.row, cell.col+1
    lang = database.cell(r, c).value

    if lang == 'de':
        saying = requests.get(
            url='https://poopjournal.rocks/YogiBot/API/v2/api.php?command=get_random_one&lng=de')
        saying = json.loads(saying.text.encode().decode(
            'utf-8-sig'))  # needed for this particular api
        bot.send_message(message.chat.id, saying[0]["saying"])

    elif lang == 'en':
        saying = requests.get(
            url='https://poopjournal.rocks/YogiBot/API/v2/api.php?command=get_random_one&lng=en')
        saying = json.loads(saying.text.encode().decode('utf-8-sig'))
        bot.send_message(message.chat.id, saying[0]["saying"])

    yogi_count = analytics_YOGI_BOT.acell('F4').value
    analytics_YOGI_BOT.update_acell(
        'F4', str(int(yogi_count)+1).replace("'", " "))


@bot.message_handler(text=['GENERATE A YOGI SAYING 🎅🏻'])
def text_filter(message):
    yogi(message)


@bot.message_handler(commands=['language'])
def language(message):

    mark_up = InlineKeyboardMarkup()
    B1 = InlineKeyboardButton(text='ENGLISH', callback_data='en')
    B2 = InlineKeyboardButton(text='GERMAN', callback_data='de')
    mark_up.row(B1, B2)
    bot.send_message(
        message.chat.id, "Please select a language 👇🏻", reply_markup=mark_up)

    language_count = analytics_YOGI_BOT.acell('F5').value
    analytics_YOGI_BOT.update_acell(
        'F5', str(int(language_count)+1).replace("'", " "))


@bot.message_handler(text=['LANGUAGE'])
def text_filter(message):
    language(message)


@bot.message_handler(commands=['website'])
def website(message):
    msg = 'Feel welcome to visit our [homepage](https\://poopjournal\.rocks/YogiBot/)\.🏠'
    bot.send_message(message.chat.id, msg, parse_mode='MarkdownV2')

    website_count = analytics_YOGI_BOT.acell('F6').value
    analytics_YOGI_BOT.update_acell(
        'F6', str(int(website_count)+1).replace("'", " "))


@bot.message_handler(text=['WEBSITE'])
def text_filter(message):
    website(message)


@bot.message_handler(commands=['help'])
def help(message):
    msg = 'Thanks for using the YogiBot.\n\n\
After starting the bot with /start you can generate a new saying by clicking the button or using the /yogi command. \
Switching the language is possible with /language. You can go to the homepage by sending /website. \
If you would like to contact me send /contact.\n\n\
Feedback is very appreaciated by filling out a Google form which the bot will send you after sending him /feedback. \
\n\nHave fun! 🥳'
    bot.send_message(message.chat.id, msg)

    help_count = analytics_YOGI_BOT.acell('F7').value
    analytics_YOGI_BOT.update_acell(
        'F7', str(int(help_count)+1).replace("'", " "))


@bot.message_handler(text=['HELP'])
def text_filter(message):
    help(message)


@bot.message_handler(commands=['contact'])
def contact(message):
    contact_info = '''
*CONTACT :*\n
Telegram: https://t\.me/Marvin\_Marvin\n
Mail: marvin@poopjournal\.rocks\n
Issue: https://github\.com/Crazy\-Marvin/SubwayTelegramBot/issues\n
Source: https://github\.com/Crazy\-Marvin/SubwayTelegramBot
'''
    bot.send_message(message.chat.id, contact_info, parse_mode='MarkdownV2')

    contact_count = analytics_YOGI_BOT.acell('F8').value
    analytics_YOGI_BOT.update_acell(
        'F8', str(int(contact_count)+1).replace("'", " "))


@bot.message_handler(commands=['feedback'])
def feedback(message):
    bot.send_message(message.chat.id, "{forms_url}")

    feedback_count = analytics_YOGI_BOT.acell('F9').value
    analytics_YOGI_BOT.update_acell(
        'F9', str(int(feedback_count)+1).replace("'", " "))


@bot.message_handler(commands=['logs'])
def logs(message):

    if message.chat.id == my_id or message.chat.id == analyst_id:

        bot.send_message(
            message.chat.id, f"Check out the *[ANALYTICS]({spreadsheet_url})* for the month\.", parse_mode="MarkdownV2", disable_web_page_preview=True)


bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.TextStartsFilter())


@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):

    data = call.data
    if data == 'en':
        english(call.message)
    elif data == 'de':
        german(call.message)


bot.polling()
