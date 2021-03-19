import os 
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
import requests

def start(update, context):
    username = update.message.from_user.username
    update.message.reply_text(f'Hola {username} bienvenidx a ClimaArgBot!')

def getTemperature(update, context):
    user_msg = update.message.text
    # improve this
    city = user_msg[13:]
    update.message.reply_text(f'Buscando temperatura de {city}...')

    # weather api call
    weather_api_url = os.getenv('WEATHER_API_URL')
    weather_api_key = os.getenv('WEATHER_API_KEY')

    response = requests.get(f'{weather_api_url}weather?q={city}&&appid={weather_api_key}&units=metric&lang=es')
    response_json = response.json()

    main_weather = response_json['main']

    current_temp = round(main_weather['temp'], 1)

    update.message.reply_text(f'La temperatura actual de {city} es de {current_temp}˚C')


if __name__ == '__main__':
    # load env variables
    load_dotenv()

    telegram_token = os.getenv('TELEGRAM_TOKEN')

    updater = Updater(token=telegram_token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('temperatura', getTemperature))

    updater.start_polling()
    updater.idle()