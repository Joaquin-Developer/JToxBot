# pylint: disable=missing-function-docstring
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import json
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# from command_functions import weather_info, search_wikipedia  # custom modules
from modules import search_wikipedia, weather_info

# from modules import translator


# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

logger = logging.getLogger(__name__)
token = os.environ["TOKEN_TELEGRAM_BOT"]


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    # first_name = update_object.get("message").get("chat").get("first_name")
    # print(first_name)
    greeting_message = read_greetings()
    update.message.reply_text(greeting_message.format(update.message.chat.first_name))
    # update.message.reply_text("Hola, soy ToxBot, el BOT mas pro que existe :v")


def help_command(update, context):
    update.message.reply_text(get_help_message())


def answer_weather(update, context):
    text = update.message.text
    country = text[7 : len(text)]

    if not country.isspace() and len(country) != 0:
        data = weather_info.get_weather(country)
        update.message.reply_text(data)
    else:
        update.message.reply_text("Forma de úso: /clima [ciudad]. Ejemplo: /clima Montevideo")


def wikipedia_search_pages(update, context):
    search = update.message.text[6 : len(update.message.text)]

    if len(search) != 0:
        string_pages = search_wikipedia.search_pages(search)
        if string_pages != None:
            update.message.reply_text(string_pages)
        else:
            # error in wikipedia library
            update.message.reply_text("No pude procesar tu búsqueda :(\n\nTox.")
    else:
        # user typed command error:
        update.message.reply_text("Forma de úso: /wiki [búsqueda].\n Ejemplo: /wiki Uruguay\n\nTox.")


def wikipedia_get_page(update, context):
    generic_exception = Exception("Forma de úso: /page [title]➡[nro_pagina]")
    search_exception = Exception("¡Ups! Se produjo un error interno y no pude procesar tu búsqueda\n\nTox.")
    try:
        search_params = update.message.text[6 : len(update.message.text)].split("➡")

        if (
            len(search_params) == 2
            and len(search_params[0]) != 0
            and len(search_params[1]) != 0
            and search_params[1].isdigit()
        ):

            title = search_params[0]
            nro_page = int(search_params[1])
            result_page = search_wikipedia.get_page(title, nro_page)
            if not result_page:
                raise search_exception

        else:
            raise generic_exception
    except Exception as e:
        update.message.reply_text(e)
    else:
        update.message.reply_text(result_page)


def echo(update, context):
    # Echo the user message.
    update.message.reply_text(update.message.text)


def get_help_message():
    return open(os.environ["PP_ROUTE"] + "/BOT_Telegram_Python/bot_info.txt").read()


def read_greetings():
    json_greetings = open(os.environ["PP_ROUTE"] + "/BOT_Telegram_Python/v2.0/data/greetings_messages.json").read()
    greetings_data = json.loads(json_greetings)
    random_index = random.randint(0, len(greetings_data) - 1)
    return greetings_data[random_index].get("message")


def reply_message(update, context):
    if update.message.text.lower().find("hol") >= 0:
        update.message.reply_text("Hola we")
    # elif (update.message.text != "help" and update.message.text != "start"):
    else:
        random_answers = ["me invocaste wey", "no toy", "ke", "zzzz", ":v", ":)", "¿ke kieres ahora?", "me juí"]
        index = random.randint(0, len(random_answers) - 1)
        update.message.reply_text(random_answers[index])


def get_updater():
    return Updater(token, use_context=True)


def add_handlers(dp) -> None:
    dp.add_handler(MessageHandler(Filters.regex("clima"), answer_weather))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ayuda", help_command))
    dp.add_handler(MessageHandler(Filters.regex("wiki"), wikipedia_search_pages))
    dp.add_handler(CommandHandler("page", wikipedia_get_page))
    # dp.add_handler(MessageHandler(Filters.regex("wikipage"), ))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))


def main():
    updater = get_updater()
    dp = updater.dispatcher
    add_handlers(dp)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
