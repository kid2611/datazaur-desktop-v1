from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os


class TelegramBot:
    def __init__(self, backend):
        self.backend = backend
        self.updater = Updater(os.environ.get('TELEGRAM_API_KEY'))
        self.activated = False

    def check_condition(self):
        pass

    def send_message(self):
        pass


    def set_alert(self, name, conditions):
        self.updater.dispatcher.add_handler(CommandHandler(name, self.send_message))


    def activate_bot(self):
        self.updater.start_polling()
        self.updater.idle()
        self.activated = True

    def deactivate_bot(self):
        self.updater.stop()
        self.activated = False


def hello(update : Update, context : CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('1830061812:AAEs79TXPXr3CgxhilqSEjF1jYKs7_s5tmc')
updater.dispatcher.add_handler(CommandHandler('alert', hello))

updater.start_polling()
updater.idle()



