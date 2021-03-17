import os 
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

def start(update, context):

    update.message.reply_text('Hola bienvenidx a ClimaArgBot!')

if __name__ == '__main__':
    # load env variables
    load_dotenv()

    telegram_token = os.getenv('TELEGRAM_TOKEN')

    updater = Updater(token=telegram_token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()