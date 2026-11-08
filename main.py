import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from telegram.bot import build_app
from engine.scanner import scan_and_send
from config import SCAN_INTERVAL_MINUTES


async def post_init(application):
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        lambda: asyncio.create_task(
            scan_and_send(application)
        ),
        "interval",
        minutes=SCAN_INTERVAL_MINUTES,
        id="saib_scan",
        max_instances=1,
        coalesce=True
    )

    scheduler.start()
    application.bot_data["scheduler"] = scheduler

    print("SAIB scheduler started.")


async def post_shutdown(application):
    scheduler = application.bot_data.get("scheduler")

    if scheduler and scheduler.running:
        scheduler.shutdown(wait=False)


def main():
    app = build_app()

    app.post_init = post_init
    app.post_shutdown = post_shutdown

    print("SAIB Telegram Bot is starting...")
    app.run_polling()


if __name__ == "__main__":
    main()
