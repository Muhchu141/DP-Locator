from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8323610116:AAFvSm90Sj160XvM6BP6bkhxP0c-nC9Pxd0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Kobaa DP Bot is online.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()