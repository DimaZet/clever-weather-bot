import logging
import os

from telegram.ext import CommandHandler
from telegram.ext import Updater

from decoder import Decoder
from forecasting import Weather

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

updater = Updater(token=os.environ['BOT_TOKEN'], use_context=True)
dispatcher = updater.dispatcher

decoder = Decoder()
weather = Weather()


def whats_the_weather(update, context):
    if context.args:
        address = ' '.join(context.args)
        coords = decoder.decode(address)
        avg, feel = weather.get_weather(**coords)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="avg temperature is {}, feels like {}".format(avg, feel)
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="please write address with"
        )


start_handler = CommandHandler('weather', whats_the_weather)
dispatcher.add_handler(start_handler)

updater.start_polling()
