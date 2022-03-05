from config import token

from telegram.ext import Updater, CommandHandler


def start(update, context):
    context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text="Hello " "{yourname}, " "Welcome on sillytuktuk bot".format(
            yourname=update.effective_user.full_name))


updater = Updater(token)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
