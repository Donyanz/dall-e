from telegram import Bot, InputFile, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, Updater, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler, CallbackContext
from config import TOKEN
from params import WELCOME ,WAIT
from function import dall_e ,set_the_size
from logger_setup import logger


def main():
    application = Application.builder().token(
        TOKEN).build()
    application.add_handler(CommandHandler("start", start , block=False))
    application.add_handler(MessageHandler(filters.TEXT , message_handler , block=False))

    application.run_polling()
    
async def start(update , context):
    await update.message.reply_text(WELCOME)    
    
async def message_handler(update , context):
    await update.message.reply_text(WAIT)
    message=update.message.text 
    result=await dall_e(message)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=result, caption=message)


    
if __name__ == "__main__":

    main()    