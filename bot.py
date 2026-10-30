from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8323610116:AAG4A3YiZyn0VYmckdCH8oEbr-5bTf-n0qo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Kobaa DP Bot is online.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()