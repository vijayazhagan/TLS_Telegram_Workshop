
# Imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

# Variables
updater = Updater(token='1048212954:AAFFjUvud5-7neBPa98w6DEgRg58JDrMcyQ', use_context=True)
dispatcher = updater.dispatcher

# Functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Rayappan ah? Michael ah? Bigileeeyyy!")
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Verithanam Verithanam!")
def setDate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Not trying to flirt but your bdae pls?")
def Horoscope(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="What you should do today_____")

# Main
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

setDate_handler = CommandHandler('setDate', setDate)
dispatcher.add_handler(setDate_handler)

Horoscope_handler = CommandHandler('Horoscope', Horoscope)
dispatcher.add_handler(Horoscope_handler)

updater.start_polling()
print('Bot is Working')