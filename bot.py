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

# ================= CONFIG =================

BOT_TOKEN = os.getenv("import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    ChatJoinRequestHandler,
    filters,
)

# ================= CONFIG =================

BOT_TOKEN = os.getenv("import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    ChatJoinRequestHandler,
    filters,
)

# ================= CONFIG =================

BOT_TOKEN = os.getenv("8299837542:AAF7XOeM1YLDN4c_qJXKWeFh2lyQFpzNNnM")  # 🔐 SAFE: token from environment

ADMIN_ID =  6487827700 # ✅ YOUR ADMIN ID
AUTO_ACCEPT = True

WELCOME_MESSAGE = (
    "👋 Welcome!\n\n"
    "You have been approved successfully ✅\n"
    "Please read the pinned rules and enjoy the community 🚀"
)

# =========================================


def is_admin(update: Update):
    return update.effective_user and update.effective_user.id == ADMIN_ID


# ========== AUTO APPROVE + WELCOME DM ==========
async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not AUTO_ACCEPT:
        return

    join_request = update.chat_join_request
    user = join_request.from_user

    # Approve join request
    await join_request.approve()

    # Send welcome DM
    try:
        await context.bot.send_message(
            chat_id=user.id,
            text=WELCOME_MESSAGE
        )
    except Exception as e:
        print("❌ Cannot send welcome DM:", e)


# ========== ADMIN PANEL ==========
async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return

    keyboard = [
        ["✅ Auto Accept ON", "❌ Auto Accept OFF"],
        ["📝 Talk to Bot"]
    ]

    await update.message.reply_text(
        "🛠 Admin Control Panel",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )


# ========== ADMIN BUTTON HANDLER ==========
async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global AUTO_ACCEPT

    if not is_admin(update):
        return

    text = update.message.text

    if text == "✅ Auto Accept ON":
        AUTO_ACCEPT = True
        await update.message.reply_text("✅ Auto-accept ENABLED")

    elif text == "❌ Auto Accept OFF":
        AUTO_ACCEPT = False
        await update.message.reply_text("❌ Auto-accept DISABLED")

    elif text == "📝 Talk to Bot":
        context.user_data["chat_mode"] = True
        await update.message.reply_text("✍️ Send any message, I will reply")


# ========== BOT CHAT MODE ==========
async def bot_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return

    if context.user_data.get("chat_mode"):
        await update.message.reply_text(
            f"🤖 You said:\n\n{update.message.text}"
        )


# ========== MAIN ==========
def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is missing. Set it in environment variables.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(approve_request))
    app.add_handler(CommandHandler("panel", panel))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, admin_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot_chat))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
")  # 🔐 SAFE: token from environment

ADMIN_ID = 6487827700   # ✅ YOUR ADMIN ID
AUTO_ACCEPT = True

WELCOME_MESSAGE = (
    "👋 Welcome!\n\n"
    "You have been approved successfully ✅\n"
    "Please read the pinned rules and enjoy the community 🚀"
)

# =========================================


def is_admin(update: Update):
    return update.effective_user and update.effective_user.id == ADMIN_ID


# ========== AUTO APPROVE + WELCOME DM ==========
async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not AUTO_ACCEPT:
        return

    join_request = update.chat_join_request
    user = join_request.from_user

    # Approve join request
    await join_request.approve()

    # Send welcome DM
    try:
        await context.bot.send_message(
            chat_id=user.id,
            text=WELCOME_MESSAGE
        )
    except Exception as e:
        print("❌ Cannot send welcome DM:", e)


# ========== ADMIN PANEL ==========
async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return

    keyboard = [
        ["✅ Auto Accept ON", "❌ Auto Accept OFF"],
        ["📝 Talk to Bot"]
    ]

    await update.message.reply_text(
        "🛠 Admin Control Panel",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )


# ========== ADMIN BUTTON HANDLER ==========
async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global AUTO_ACCEPT

    if not is_admin(update):
        return

    text = update.message.text

    if text == "✅ Auto Accept ON":
        AUTO_ACCEPT = True
        await update.message.reply_text("✅ Auto-accept ENABLED")

    elif text == "❌ Auto Accept OFF":
        AUTO_ACCEPT = False
        await update.message.reply_text("❌ Auto-accept DISABLED")

    elif text == "📝 Talk to Bot":
        context.user_data["chat_mode"] = True
        await update.message.reply_text("✍️ Send any message, I will reply")


# ========== BOT CHAT MODE ==========
async def bot_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return

    if context.user_data.get("chat_mode"):
        await update.message.reply_text(
            f"🤖 You said:\n\n{update.message.text}"
        )


# ========== MAIN ==========
def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is missing. Set it in environment variables.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(approve_request))
    app.add_handler(CommandHandler("panel", panel))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, admin_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot_chat))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
")  # 🔐 SAFE: token from environment

ADMIN_ID = 6487827700   # ✅ YOUR ADMIN ID
AUTO_ACCEPT = True

WELCOME_MESSAGE = (
    "👋 Welcome!\n\n"
    "You have been approved successfully ✅\n"
    "Please read the pinned rules and enjoy the community 🚀"
)

# =========================================


def is_admin(update: Update):
    return update.effective_user and update.effective_user.id == ADMIN_ID


# ========== AUTO APPROVE + WELCOME DM ==========
async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not AUTO_ACCEPT:
        return

    join_request = update.chat_join_request
    user = join_request.from_user

    # Approve join request
    await join_request.approve()

    # Send welcome DM
    try:
        await context.bot.send_message(
            chat_id=user.id,
            text=WELCOME_MESSAGE
        )
    except Exception as e:
        print("❌ Cannot send welcome DM:", e)


# ========== ADMIN PANEL ==========
async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return

    keyboard = [
        ["✅ Auto Accept ON", "❌ Auto Accept OFF"],
        ["📝 Talk to Bot"]
    ]

    await update.message.reply_text(
        "🛠 Admin Control Panel",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )


# ========== ADMIN BUTTON HANDLER ==========
async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global AUTO_ACCEPT

    if not is_admin(update):
        return

    text = update.message.text

    if text == "✅ Auto Accept ON":
        AUTO_ACCEPT = True
        await update.message.reply_text("✅ Auto-accept ENABLED")

    elif text == "❌ Auto Accept OFF":
        AUTO_ACCEPT = False
        await update.message.reply_text("❌ Auto-accept DISABLED")

    elif text == "📝 Talk to Bot":
        context.user_data["chat_mode"] = True
        await update.message.reply_text("✍️ Send any message, I will reply")


# ========== BOT CHAT MODE ==========
async def bot_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return

    if context.user_data.get("chat_mode"):
        await update.message.reply_text(
            f"🤖 You said:\n\n{update.message.text}"
        )


# ========== MAIN ==========
def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is missing. Set it in environment variables.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(approve_request))
    app.add_handler(CommandHandler("panel", panel))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, admin_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot_chat))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
