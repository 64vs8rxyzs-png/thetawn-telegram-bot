import logging
import os
import telegram.ext as ext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
from keep_alive import start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    keyboard = [
        [InlineKeyboardButton("Modalités de Commandes", callback_data="modalites")],
        [InlineKeyboardButton("Contact", url="https://t.me/thetawn")],
        [InlineKeyboardButton("Telegram", url="https://t.me/thetawn")],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = "Bienvenue chez THE TAWN! 👋\n\nContactez-nous pour plus d'informations."
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=welcome_text,
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "modalites":
        modalites_text = """📋 Modalités de Commande – THE TAWN

⏱️ Horaires : 10h - 00h
📍 Meet-up : 10h - 00h
🚚 Livraison : BIENTOT DISPONIBLE
        await query.edit_message_text(text=modalites_text, parse_mode="Markdown")

if __name__ == '__main__':
    if not TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN not found.")
        exit(1)

    # Start keep-alive server
    start()
    print("Keep-alive server started on port 8080")

    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("Bot is running...")
    application.run_polling()
