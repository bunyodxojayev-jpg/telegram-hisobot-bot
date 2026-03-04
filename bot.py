from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8710337110:AAHKd6fff-OVSzG7qk_u1LHl3yi2UGwlg04"

# Boshlang‘ich 3 bo‘lim
sections = {
    "Bolim1": "Bolim1 ga oid malumot",
    "Bolim2": "Bolim2 ga oid malumot",
    "Bolim3": "Bolim3 ga oid malumot",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(name, callback_data=name)] for name in sections.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bo‘limni tanlang:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=sections[query.data])

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
