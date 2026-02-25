import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Логирование — без него ты не поймёшь, где сломалось
logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# /start — ТОЧНО по твоему тексту, без кнопок, без лишнего
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Приветствую! В этом боте вы можете получить множество призов, "
        "начиная от звезд, заканчивая редкими коллекционными подарками!\n\n"
        "Чтобы начать — нажмите на кнопку «Сыграть!».\n\n"
        "Для получения дополнительной информации о проекте пройдите в его официальный ТГК: "
        "https://t.me/stepbystepdelision"
    )

def main() -> None:
    # Токен БЕРЁТСЯ ТОЛЬКО ИЗ ПЕРЕМЕННОЙ ОКРУЖЕНИЯ — НИКОГДА не в коде!
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        # Railway сразу покажет эту ошибку в логах — не пропустишь
        raise RuntimeError("TELEGRAM_BOT_TOKEN не задан в Variables!")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    logger.info("✅ Бот запущен — ждём /start")
    app.run_polling(allowed_updates=Update.ALL_TYPES)   # Railway ДЕРЖИТ процесс 24/7

if __name__ == "__main__":
    main()