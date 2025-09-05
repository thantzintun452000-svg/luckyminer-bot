from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# BotFather ကရထားတဲ့ token ထည့်ပြီးသား
TOKEN = "8401563933:AAHg8-cST_r4W1HHxSHUpHjZacz9WdtVVlA"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 👋! Bot အဆင်ပြေပါတယ်!")

# main function
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()