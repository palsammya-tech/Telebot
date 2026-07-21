import logging
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ---------- CONFIG ----------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "PUT_YOUR_TOKEN_HERE")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "@yourchannelusername")  # or -1001234567890
# -----------------------------

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Welcome!\n\n"
        "Just send me the name of a movie you want, and I'll post the request "
        "to the channel."
    )


async def handle_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    movie_title = update.message.text.strip()

    if not movie_title:
        return

    username = f"@{user.username}" if user.username else user.first_name

    post_text = (
        f"🎬 *Movie Request*\n\n"
        f"*Title:* {movie_title}\n"
        f"*Requested by:* {username}"
    )

    try:
        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=post_text,
            parse_mode="Markdown",
        )
        await update.message.reply_text(
            f"✅ Your request for \"{movie_title}\" was posted to the channel!"
        )
    except Exception as e:
        logger.error(f"Failed to post to channel: {e}")
        await update.message.reply_text(
            "⚠️ Something went wrong posting your request. "
            "Make sure the bot is an admin in the channel."
        )


def main():
    if BOT_TOKEN == "PUT_YOUR_TOKEN_HERE":
        raise RuntimeError("Set the BOT_TOKEN environment variable or edit the script.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_request))

    logger.info("Bot started. Press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
