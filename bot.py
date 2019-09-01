from config import TOKEN
from glossary import GLOSSARY
import glossary_functions as g
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

d = GLOSSARY
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start_callback(update, context):
    update.message.reply_text("Hi, I'll help you to prepare to ISTQB test! \n"
                              "Use /help for details")


def gives_help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Here's what I can do: \n"
                                  "/get, to get random Glossary statement \n" 
                                  "/search [statement], to get particular Glossary statement")


def send_random_item(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=g.get_random_item())


def search_and_send(update, context):
    user_says = " ".join(context.args)
    update.message.reply_text(g.search_by_key(user_says))


def send_list_of_statements(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=g.get_keys_list())


def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Don't know that command=(")


dispatcher.add_handler(CommandHandler("start", start_callback))
dispatcher.add_handler(CommandHandler('get', send_random_item))
dispatcher.add_handler(CommandHandler('help', gives_help))
dispatcher.add_handler(CommandHandler("search", search_and_send))
dispatcher.add_handler(CommandHandler("list", send_list_of_statements))

dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()


if __name__ == '__main__':
    pass
