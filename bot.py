import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 6487827700


# ───────── START COMMAND ─────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("➕ Add Bot", callback_data="add_bot")],
        [InlineKeyboardButton("🤖 Show My Bots", callback_data="show_bots")],
        [InlineKeyboardButton("🌍 Language", callback_data="language")],
        [InlineKeyboardButton("⚙️ Settings", callback_data="settings")],
    ]

    await update.message.reply_text(
        "👋 Hello!\n\n"
        "I can:\n"
        "1. Help you manage auto-accept bots\n"
        "2. Show your bots\n"
        "3. Provide settings & language\n\n"
        "Choose an option below 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ───────── CALLBACK HANDLER ─────────
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "add_bot":
        await query.edit_message_text(
            "➕ *Add Bot*\n\n"
            "Send me your bot token.\n"
            "_(Example: 123456:ABC...)_",
            parse_mode="Markdown"
        )

    elif query.data == "show_bots":
        await query.edit_message_text(
            "🤖 *Your Bots*\n\n"
            "You haven’t added any bots yet.",
            parse_mode="Markdown"
        )

    elif query.data == "language":
        keyboard = [
            [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton("🇮🇳 Hindi", callback_data="lang_hi")]
        ]
        await query.edit_message_text(
            "🌍 Select language:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "settings":
        await query.edit_message_text(
            "⚙️ *Settings*\n\n"
            "More options coming soon.",
            parse_mode="Markdown"
        )

    elif query.data == "lang_en":
        await query.edit_message_text("✅ Language set to English")

    elif query.data == "lang_hi":
        await query.edit_message_text("✅ भाषा हिंदी सेट की गई")


# ───────── MAIN ─────────
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler))

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
