import logging
import os

from telegram.ext import CommandHandler
from telegram.ext import Updater

from helper import Helper

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

updater = Updater(token=os.environ['BOT_TOKEN'], use_context=True)
dispatcher = updater.dispatcher

helper = Helper()


def whats_the_weather(update, context):
    if context.args:
        recommendations = helper.complex_forecast_on_tomorrow(' '.join(context.args))
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=recommendations
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="please write address with command"
        )


weather_handler = CommandHandler('weather', whats_the_weather)
dispatcher.add_handler(weather_handler)

updater.start_polling()
