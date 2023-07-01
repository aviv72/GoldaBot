# bot nane - Goldabot
# username - Shaibaruchbot
import os

import telegram

PORT = int(os.environ.get('PORT', 8443))
import logging
from telegram import Update, ForceReply
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Application

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\ , Golda ia here',
        reply_markup=ForceReply(selective=True),
    )


async def conspiracy(update: Update, context: CallbackContext) -> None:
    if "קונספירציה" in update.message.text:
        await update.message.reply_text("הידעת שאין דבר כזה קורונה")


async def harel_sticker(update: Update, context: CallbackContext):
    await context.bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgQAAxkBAAEDxhhh9bI172aGlttQVcm7-R0tTTaoQwAC6QsAAmjWsVOpG1FrekkatiME')


async def itzik(update: Update, context: CallbackContext) -> None:
    await context.bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgQAAxkBAAEDx_Jh-Etq9kzc7DVxbKbSIp3gF3-l7AACBA0AAnw5wFP5fntP-dR4RyME')


async def taxi(update: Update, context: CallbackContext) -> None:
    await context.bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgQAAxkBAAED3DBiAl8Dpq8eWNLcodK2fb5R4YVyAQACTQwAAqt2EFAVU-jjlxsgeiME')


async def covid(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("עבדו עלינו! תשאלו אפילו את @cykabylat2020")


async def maor(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("מאור אלון בן זונה גדול! תשאלו אותו @Maor426")


def main() -> None:
    """Start the bot."""
    # updater = Updater(TOKEN)
    # dispatcher = updater.dispatcher

    TOKEN = os.environ("TOKEN")
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()


    application.add_handler(MessageHandler(telegram.ext.filters.Regex('harel|ערל|Harel|הראל'), harel_sticker))
    application.add_handler(MessageHandler(telegram.ext.filters.Regex('Maor|מאור|maor'), maor))
    application.add_handler(MessageHandler(telegram.ext.filters.Regex('itzik|איציק'), itzik))
    application.add_handler(MessageHandler(telegram.ext.filters.Regex('Taxi|taxi|מונית|טקסי'), taxi))
    application.add_handler(MessageHandler(telegram.ext.filters.Regex('corona|קורונה|covid'), covid))
    # application.add_handler(MessageHandler(telegram.ext.filters.Regex & ~telegram.ext.filters.Command, conspiracy))

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("itzik", filters=telegram.ext.filters.Regex('itzik|איציק'), callback=itzik))
    application.add_handler(CommandHandler("taxi", filters=telegram.ext.filters.Regex('Taxi|taxi|מונית|טקסי'), callback=taxi))
    application.add_handler(CommandHandler("harel", filters=telegram.ext.filters.Regex('harel|ערל|Harel|הראל'), callback=harel_sticker))
    application.add_handler(CommandHandler("maor", filters=telegram.ext.filters.Regex('Maor|מאור|maor'), callback=maor))
    application.add_handler(CommandHandler("corona", filters=telegram.ext.filters.Regex('corona|קורונה|covid'), callback=covid))


    # Run the bot until the user presses Ctrl-C
    application.run_polling()

    # Start the Bot
    # updater.start_webhook(listen="0.0.0.0",
    #                       port=int(PORT),
    #                       url_path=TOKEN,
    #                       webhook_url='https://mighty-anchorage-88413.herokuapp.com/' + TOKEN)
    #
    # updater.idle()


if __name__ == '__main__':
    main()
