import logging
import os

from telegram.ext import CommandHandler
from telegram.ext import Updater

from forecasting import ForecastingService

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

updater = Updater(token=os.environ['BOT_TOKEN'], use_context=True)
dispatcher = updater.dispatcher

helper = ForecastingService()


def whats_the_weather(update, context):
    if context.args:
        try:
            r = helper.complex_forecast_on_tomorrow(' '.join(context.args))
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Tomorrow it will be {} degrees, it feels like {}, it's {} outside. Take your {}".format(
                    r['temp_avg'], r['feels_like'], r['condition'].replace('-', ' '), r['take']
                )
            )
        except ValueError:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Wrong address"
            )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Please write address with command"
        )


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Send me: /weather your address"
    )


weather_handler = CommandHandler('weather', whats_the_weather)
dispatcher.add_handler(weather_handler)

start_handler = CommandHandler('start', help)
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

updater.start_polling()
