import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ChatJoinRequestHandler,
)

# ===== CONFIG =====
BOT_TOKEN = os.getenv("8299837542:AAF7XOeM1YLDN4c_qJXKWeFh2lyQFpzNNnM")   # DO NOT CHANGE
ADMIN_ID = 6487827700
# ==================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "This bot automatically accepts join requests.\n"
        "You will be approved instantly."
    )

async def welcome_dm(context: ContextTypes.DEFAULT_TYPE, user_id: int):
    try:
        await context.bot.send_message(
            chat_id=user_id,
            text=(
                "✅ Welcome!\n\n"
                "Your request has been approved.\n"
                "Enjoy the channel 🚀"
            ),
        )
    except:
        pass

async def accept_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = update.chat_join_request
    await req.approve()
    await welcome_dm(context, req.from_user.id)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatJoinRequestHandler(accept_request))

    print("🤖 Bot started successfully")
    app.run_polling()

if __name__ == "__main__":
    main()
