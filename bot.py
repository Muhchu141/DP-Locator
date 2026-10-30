from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8323610116:AAH5Lp5gYFyQDnF5Gvmwp-5k-UQX58t4qGI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Kobaa DP Bot is online.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()