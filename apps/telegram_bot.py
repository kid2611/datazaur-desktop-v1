

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update : Update, context : CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('1830061812:AAEs79TXPXr3CgxhilqSEjF1jYKs7_s5tmc')
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()



