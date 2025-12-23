import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    ChatJoinRequestHandler,
    filters,
)

BOT_TOKEN = os.getenv("8299837542:AAF7XOeM1YLDN4c_qJXKWeFh2lyQFpzNNnM")

ADMIN_ID = 6487827700   # 🔴 put your Telegram numeric ID
AUTO_ACCEPT = True


def is_admin(update: Update):
    return update.effective_user and update.effective_user.id == ADMIN_ID


# ========= AUTO APPROVE JOIN REQUEST =========
async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if AUTO_ACCEPT:
        await update.chat_join_request.approve()


# ========= ADMIN PANEL =========
async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return

    keyboard = [
        ["✅ Auto Accept ON", "❌ Auto Accept OFF"],
        ["📝 Send message to bot"]
    ]

    await update.message.reply_text(
        "🛠 Admin Control Panel",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )


# ========= BUTTON HANDLER =========
async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global AUTO_ACCEPT

    if not is_admin(update):
        return

    text = update.message.text

    if text == "✅ Auto Accept ON":
        AUTO_ACCEPT = True
        await update.message.reply_text("✅ Auto-accept is ON")

    elif text == "❌ Auto Accept OFF":
        AUTO_ACCEPT = False
        await update.message.reply_text("❌ Auto-accept is OFF")

    elif text == "📝 Send message to bot":
        context.user_data["chat_mode"] = True
        await update.message.reply_text("✍️ Type anything, I will reply")


# ========= BOT CHAT MODE =========
async def bot_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return

    if context.user_data.get("chat_mode"):
        await update.message.reply_text(
            f"🤖 You said:\n\n{update.message.text}"
        )


# ========= MAIN =========
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(approve_request))
    app.add_handler(CommandHandler("panel", panel))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, admin_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot_chat))

    print("🤖 Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
