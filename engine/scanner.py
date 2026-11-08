from engine.discovery import discover_all
from engine.security import check_url, calculate_security_score
from engine.free_filter import check_free_airdrop
from engine.grading import calculate_grade
from database.database import save_airdrop, log_scan
from telegram.messages import format_airdrop
from telegram.buttons import website_button
from config import ADMIN_USER_ID, MIN_SECURITY_SCORE


async def scan_and_send(application):
    candidates = discover_all()
    sent = 0

    for item in candidates:
        url_ok, reason = check_url(item.get("url", ""))

        if not url_ok:
            print("Rejected URL:", reason)
            continue

        score = calculate_security_score(
            item.get("official_source") is True,
            item.get("domain_verified") is True,
            item.get("no_seed_request") is True,
            item.get("no_unlimited_approval") is True,
            item.get("contract_verified") is True
        )

        if score < MIN_SECURITY_SCORE:
            continue

        if not check_free_airdrop(item):
            continue

        quality_score = item.get("quality_score", 0)
        grade = calculate_grade(quality_score)

        if grade not in ["A+", "A", "B+"]:
            continue

        item["security_score"] = score
        item["grade"] = grade

        if not save_airdrop(item):
            continue

        try:
            await application.bot.send_message(
                chat_id=ADMIN_USER_ID,
                text=format_airdrop(item),
                reply_markup=website_button(item["url"])
            )
            sent += 1

        except Exception as error:
            print("Telegram send error:", error)

    log_scan(sent)
    return sent
