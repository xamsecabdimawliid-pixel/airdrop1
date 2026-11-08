from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from config import BOT_TOKEN, ADMIN_USER_ID
from telegram.buttons import website_button
from database.database import get_stats
from engine.scanner import scan_and_send


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
🇸🇴 KU SOO DHAWOOW SAIB

Somali Airdrop Intelligence Bot 🚀

Waxaan kuu raadinaynaa Airdrops:
🏆 A+ / A / B+
🛡️ Security screening
💰 FREE opportunities
🌐 Official project links

Commands:
/start - Bilow
/stats - Tirakoob
/scan - Baadh hadda
/help - Caawimaad
"""
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "SAIB wuxuu soo gudbiyaa fursado la baaray. "
        "Waligaa ha dirin seed phrase ama private key."
    )


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_stats()

    await update.message.reply_text(
        f"📊 SAIB STATS\n\n"
        f"Total Airdrops: {data['total']}\n"
        f"Free verified: {data['free']}"
    )


def is_admin(update):
    return (
        update.effective_user
        and update.effective_user.id == ADMIN_USER_ID
    )


async def scan_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        await update.message.reply_text(
            "⛔ Amarkan waxaa isticmaali kara Admin-ka oo keliya."
        )
        return

    await update.message.reply_text("🔎 Baadhista waa bilaabatay...")

    count = await scan_and_send(context.application)

    await update.message.reply_text(
        f"✅ Baadhistu way dhammaatay.\n"
        f"Fursado cusub: {count}"
    )


def build_app():
    if not BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN lama dejin.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("scan", scan_command))

    return app
