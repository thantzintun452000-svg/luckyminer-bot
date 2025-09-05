from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# BotFather ကယူထားတဲ့ token ထည့်ပါ
TOKEN = "YOUR_BOT_TOKEN_HERE"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 👋! Bot အဆင်ပြေပါတယ်!")

# main function
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()