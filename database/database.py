import sqlite3
import os
from config import DATABASE_PATH

def get_connection():
    folder = os.path.dirname(DATABASE_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)

    return sqlite3.connect(DATABASE_PATH)

def initialize_database():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS airdrops (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                url TEXT UNIQUE NOT NULL,
                network TEXT,
                description TEXT,
                security_score INTEGER,
                grade TEXT,
                is_free INTEGER DEFAULT 0,
                status TEXT DEFAULT 'active',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS scan_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scanned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                found INTEGER DEFAULT 0
            )
        """)

def save_airdrop(item):
    with get_connection() as conn:
        cursor = conn.execute("""
            INSERT OR IGNORE INTO airdrops
            (name, url, network, description,
             security_score, grade, is_free)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            item["name"],
            item["url"],
            item.get("network", "Unknown"),
            item.get("description", ""),
            item["security_score"],
            item["grade"],
            int(item["is_free"])
        ))

        return cursor.rowcount > 0

def log_scan(found):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO scan_logs (found) VALUES (?)",
            (found,)
        )

def get_stats():
    with get_connection() as conn:
        total = conn.execute(
            "SELECT COUNT(*) FROM airdrops"
        ).fetchone()[0]

        free = conn.execute(
            "SELECT COUNT(*) FROM airdrops WHERE is_free=1"
        ).fetchone()[0]

        return {
            "total": total,
            "free": free
        }
