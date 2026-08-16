from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context):
    name = update.effective_user.first_name
    await update.message.reply_text(f"🤍 أهلاً يا {name}!\n\nأنا بوت مستر نبض 🧪\nتم استلام سؤالك وهرد عليك في أقرب وقت")

async def reply(update: Update, context):
    name = update.effective_user.first_name
    await update.message.reply_text(f"وصلني سؤالك يا {name} ❤️\nمستر نبض هيرد عليك قريب إن شاء الله")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.run_polling()
