import os
from telegram import Bot
from telegram.ext import Updater, ChatJoinRequestHandler

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

def approve_join(update, context):
    user = update.chat_join_request.from_user
    update.chat_join_request.approve()

    if ADMIN_ID:
        context.bot.send_message(
            chat_id=int(ADMIN_ID),
            text=f"✅ Approved: {user.first_name} ({user.id})"
        )

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(ChatJoinRequestHandler(approve_join))

print("🤖 Bot started successfully (v13 polling)")

updater.start_polling()
updater.idle()
