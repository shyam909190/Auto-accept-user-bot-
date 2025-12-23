import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.chat_join_request.approve()
        print(f"Approved user: {update.chat_join_request.from_user.id}")
    except Exception as e:
        print("Error approving user:", e)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(approve_request))

    print("🤖 Auto-approve bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
