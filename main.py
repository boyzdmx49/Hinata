import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hey {update.effective_user.first_name}, I'm Kenzy! Ready to fight or flirt!")

async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sending virtual hugs and love to you!")

async def slap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{update.effective_user.first_name} ne kisi ko zor ka slap de diya!")

async def cry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kenzy is crying... but stronger than ever.")

async def gaali(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Oye! Gaali kam, pyaar zyada!")

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("love", love))
app.add_handler(CommandHandler("slap", slap))
app.add_handler(CommandHandler("cry", cry))
app.add_handler(CommandHandler("gaali", gaali))

print("Kenzy Bot is live...")
app.run_polling()
