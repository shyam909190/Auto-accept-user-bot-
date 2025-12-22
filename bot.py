from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes
import os
import sys

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
ADMIN_ID = os.getenv("ADMIN_ID")

if not BOT_TOKEN or not WEBHOOK_URL:
    print("❌ BOT_TOKEN or WEBHOOK_URL missing")
    sys.exit(1)

async def approve_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    await update.chat_join_request.approve()

    if ADMIN_ID:
        await context.bot.send_message(
            chat_id=int(ADMIN_ID),
            text=f"✅ Approved: {user.first_name} ({user.id})"
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(ChatJoinRequestHandler(approve_join))

print("🤖 Bot started successfully")

app.run_webhook(
    listen="0.0.0.0",
    port=10000,
    webhook_url=WEBHOOK_URL
)
