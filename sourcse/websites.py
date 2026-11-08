import requests
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

HEADERS = {
    "User-Agent": "SAIB-AirdropResearchBot/1.0"
}

def fetch_rss(feed_url):
    try:
        response = requests.get(
            feed_url,
            headers=HEADERS,
            timeout=20
        )
        response.raise_for_status()

        root = ET.fromstring(response.content)
        items = []

        for entry in root.findall(".//item"):
            name = entry.findtext("title", "").strip()
            url = entry.findtext("link", "").strip()
            description = entry.findtext(
                "description", ""
            ).strip()

            if not name or not url:
                continue

            items.append({
                "name": name,
                "url": url,
                "description": description,
                "network": "Unknown",
                "gas_required": None,
                "deposit_required": None,
                "investment_required": None,
                "paid_subscription_required": None,
                "free_verified": False,
                "exchange_kyc_required": None,
                "security_score": 0
            })

        return items

    except Exception as error:
        print("RSS error:", error)
        return []


def discover_airdrops():
    """
    Ku dar RSS feed URLs la hubiyey.
    RSS item la helay ma aha Airdrop la xaqiijiyey.
    """
    return []
