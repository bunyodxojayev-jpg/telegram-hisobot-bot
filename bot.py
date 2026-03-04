import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# 20 ta bo'lim va ularning ma'lumotlari
sections = {
    "Bolim1": "Bolim1 ga oid malumotlar...",
    "Bolim2": "Bolim2 ga oid malumotlar...",
    "Bolim3": "Bolim3 ga oid malumotlar...",
    # ... shu tarzda 20 ta bo'lim qo'shishingiz mumkin
}

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton(name, callback_data=name)] for name in sections.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Bo‘limlardan birini tanlang:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    text = sections.get(query.data, "Bu bo‘lim uchun malumot yo‘q.")
    query.edit_message_text(text=text)

def main():
    updater = Updater(8710337110:AAHKd6fff-OVSzG7qk_u1LHl3yi2UGwlg04)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
