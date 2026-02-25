import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Приветствую! В этом боте вы можете получить множество призов, "
        "начиная от звезд, заканчивая редкими коллекционными подарками!\n\n"
        "Чтобы начать — нажмите на кнопку «Сыграть!».\n\n"
        "Для получения дополнительной информации о проекте пройдите в его официальный ТГК: "
        "https://t.me/stepbystepdelision"
    )

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("❌ TELEGRAM_BOT_TOKEN не задан в Variables!")
        raise RuntimeError("TELEGRAM_BOT_TOKEN не задан в Variables!")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    logger.info("✅ Бот запущен — ждём /start")
    app.run_polling()

if __name__ == "__main__":
    main()
