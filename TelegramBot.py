from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import yaml
import asyncio

# 🧠 Import your async main function
from agent import main  # make sure main(input_text) is async

# 🔁 Handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="Analyzing... 🧠")

    try:
        final_answer = await main(user_input)
        await context.bot.send_message(chat_id=chat_id, text=final_answer)
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"❌ Error: {e}")

# 🏁 Run the bot
if __name__ == '__main__':
    import os
    from dotenv import load_dotenv

    load_dotenv()
    
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # or hardcode

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()
