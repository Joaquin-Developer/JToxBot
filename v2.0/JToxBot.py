#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
# Functional BOT (25/01/2021) - Joaquin Parrilla

import logging, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
token = os.environ["TOKEN_TELEGRAM_BOT"]

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    # Send a message when the command /start is issued.
    update.message.reply_text("Hola, soy ToxBot, el BOT mas pro que existe :v")

def help_command(update, context):
    # Send a message when the command /help is issued.
    update.message.reply_text(get_help_message())

def answer_weather():
    pass

def echo(update, context):
    # Echo the user message.
    update.message.reply_text(update.message.text)

def get_help_message():
    return open("/home/joaquin/Documentos/ProyectosPersonales/BOT_Telegram_Python/bot_info.txt").read()

def reply_message(update, context):
    print(update.message.text)
    if (update.message.text.lower().find("hola") >= 0):
        update.message.reply_text("Hola we")
    elif (update.message.text != "help" and update.message.text != "start"):
        update.message.reply_text("gei")

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("clima", answer_weather))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ayuda", help_command))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
