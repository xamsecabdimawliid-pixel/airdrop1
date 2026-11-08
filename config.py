import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID", "0"))

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "database/saib.db"
)

SCAN_INTERVAL_MINUTES = int(
    os.getenv("SCAN_INTERVAL_MINUTES", "30")
)

MIN_SECURITY_SCORE = int(
    os.getenv("MIN_SECURITY_SCORE", "70")
)

ALLOWED_GRADES = ["A+", "A", "B+"]

SUPPORTED_WALLETS = [
    "MetaMask",
    "Trust Wallet"
]

SUPPORTED_NETWORKS = [
    "Ethereum",
    "BNB Chain",
    "Arbitrum",
    "Optimism",
    "Polygon",
    "Solana",
    "Base"
]
